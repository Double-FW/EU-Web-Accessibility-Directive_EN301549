"""Export the approved EU WAD and EN301549 Markdown without rewriting it."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from en301549_hf_common import ROOT, SOURCE, MANAGED, destination, digest, git, load_config, read_sources

MATRIX = 'EN301549_Requirements_Test_Matrix.md'
PROMPTS = 'EN301549_AI_Test_Prompts.md'
GUIDE = 'WAD_Plain_English_Breakdown_and_Evidence_Guide.md'
RAG = 'EU_Web_Accessibility_Directive_EN301549_RAG.md'
CONTEXT = ['AGENTS.md', GUIDE, MATRIX, PROMPTS, 'WAD_Requirements_to_Double_FW_Approaches_Mapping.md']
TEST_ID = r'(?:WEB|DOC|APP|EN|SCOPE|GOV)-[0-9]+'

class UniqueKeyLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate YAML metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def linked_tests(texts):
    specs = {}
    for _, title, body, *_ in sections(texts[MATRIX], matrix=True):
        if re.fullmatch(TEST_ID, title):
            if title in specs: raise ValueError('Duplicate matrix test ID.')
            specs[title] = body
    rows = {}
    for line in texts[MATRIX].splitlines(keepends=True):
        m = re.match(r'^\| \[(' + TEST_ID + r')\]\(', line)
        if m:
            if m[1] in rows: raise ValueError('Duplicate matrix row ID.')
            rows[m[1]] = line
    prompts = {}
    for _, title, body, *_ in sections(texts[PROMPTS]):
        if re.fullmatch('AI-' + TEST_ID, title):
            if title[3:] in prompts: raise ValueError('Duplicate prompt ID.')
            prompts[title[3:]] = body
    if not specs or set(specs) != set(rows): raise ValueError('Matrix rows and detailed specifications disagree.')
    if 'GOV-05' not in specs or set(prompts) != set(specs)-{'GOV-05'}:
        raise ValueError('Review prompt/matrix coverage; GOV-05 must remain human-only.')
    heading = '## Mandatory execution contract for every prompt'
    if heading not in texts[PROMPTS]: raise ValueError('Missing prompt execution contract.')
    contract = texts[PROMPTS].split(heading, 1)[1].split('\n## AI-', 1)[0]
    contract = heading + contract
    if 'requirement_status: not_assessed' not in contract or 'Human handoff' not in texts[PROMPTS]:
        raise ValueError('Missing decision or human review boundary.')
    return specs, rows, prompts, contract

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = yaml.load(match[1], Loader=UniqueKeyLoader) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text, matrix=False):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,3})[ \t]+([^\r\n]+)' if matrix else r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise ValueError('Write the export outside the source checkout.')
    cfg = load_config(root)
    target = destination(cfg['destination_dataset'])
    texts, manifest, omitted = read_sources(root, cfg)
    sha = git(root, 'rev-parse', 'HEAD').decode().strip()
    date = git(root, 'show', '-s', '--format=%cs', 'HEAD').decode().strip()
    specs, matrix_rows, prompts, contract = linked_tests(texts)
    matrix_context = texts[MATRIX].split('\n## Matrix', 1)[0]
    rag_md = metadata(texts[RAG])
    warnings = [
        'Repository legal framing and standard versions are preserved source claims, not independently rechecked legal advice or current Official Journal validation.',
        'The matrix and prompts are test-design material. No product tests, participant research, real evidence collection, compliance determination or approval system is executed.',
        'The RAG is a dated repository snapshot and repeats source documents; it is document-only to avoid duplicate section records.',
        'E/A classes, axe subsets, human complements, GOV-05 human-only status, WEB-124 additional-baseline status and separate observation/requirement decisions are preserved.'
    ]
    for path, text in texts.items():
        if metadata(text).get('license', 'MIT') != 'MIT': raise ValueError('Review changed source licence: ' + path)
    def row(path, key, title, body, a, b, hierarchy, kind):
        md = metadata(texts[path])
        test = title[3:] if path == PROMPTS and re.fullmatch('AI-' + TEST_ID, title) else title if path == MATRIX and re.fullmatch(TEST_ID, title) else ''
        return {'id': path + '::' + key, 'title': title, 'text': body, 'record_type': kind,
            'source_repository': SOURCE, 'source_path': path, 'source_commit': sha,
            'source_url': f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line': texts[path][:a].count('\n') + 1,
            'source_end_line': max(1, texts[path][:b].count('\n') + (not texts[path][:b].endswith('\n'))),
            'source_document_sha256': digest(texts[path].encode()), 'text_sha256': digest(body.encode()),
            'heading_path': hierarchy, 'metadata_json': json.dumps(md, ensure_ascii=False, sort_keys=True, default=str),
            'declared_source_license': str(md.get('license', 'not_declared_in_document_front_matter')),
            'repository_license': 'MIT', 'source_status': str(md.get('status', 'see_source')),
            'dataset_version': cfg['dataset_version'], 'source_commit_date': date, 'language': 'en-GB',
            'required_context_paths': [p for p in CONTEXT if p in texts],
            'source_document_intro': sections(texts[path], matrix=path==MATRIX)[0][2],
            'matrix_test_id': test,
            'prompt_id': 'AI-' + test if test in prompts else '',
            'paired_matrix_row': matrix_rows.get(test, ''),
            'paired_matrix_specification': specs.get(test, ''),
            'prompt_execution_contract': contract if test else '',
            'matrix_authority_and_method_context': matrix_context if test else '',
            'source_temporal_scope': 'dated_repository_snapshot' if path == RAG else 'source_guidance_at_checkout',
            'embedded_snapshot_commit': str(rag_md.get('source_commit', '')) if path == RAG else '',
            'interpretation_notice': 'Test design, not executed evidence. Preserve law/national implementation, scope, exclusions, standard/version, conditions, axe limits, E/A/N methods and human complements. Partial observation is not full conformance or legal approval.',
            'review_status': 'faithful_extraction_checked_not_legal_standard_or_product_validation'}
    docs, chunks = [], []
    for path in cfg['files']:
        if path not in texts:
            continue
        text = texts[path]
        kind = ('dated_rag_snapshot_document_only' if path == RAG else
                'proposed_test_prompt_not_execution_result' if path == PROMPTS else
                'proposed_requirements_test_matrix_not_results' if path == MATRIX else
                'explanatory_legal_evidence_guidance' if path == GUIDE else
                'advisory_agent_guidance' if path == 'AGENTS.md' else
                'orientation' if path == 'README.md' else 'supplementary_approach_mapping')
        docs.append(row(path, 'document', path, text, 0, len(text), [], kind))
        if path in cfg['document_only_files']:
            continue
        for key, title, body, a, b, hierarchy in sections(text, matrix=path==MATRIX):
            chunks.append(row(path, key, title, body, a, b, hierarchy, kind + '_section'))
    if not docs or not chunks:
        raise ValueError('The guidance export is empty.')
    schema = {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
              'required': list(docs[0]), 'additionalProperties': False, 'properties': {}}
    for k, v in docs[0].items():
        schema['properties'][k] = {'type': 'array', 'items': {'type': 'string'}} if isinstance(v, list) else {'type': 'integer' if isinstance(v, int) else 'string'}
    validator = Draft202012Validator(schema)
    for records in (docs, chunks):
        if len({r['id'] for r in records}) != len(records):
            raise ValueError('Duplicate export identifiers.')
        for r in records:
            validator.validate(r)
            if digest(r['text'].encode()) != r['text_sha256']:
                raise ValueError('Text checksum mismatch.')
    output.mkdir(parents=True, exist_ok=True)
    def write_json(name, obj):
        (output/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for name, records in [('documents.jsonl', docs), ('knowledge_chunks.jsonl', chunks)]:
        (output/name).write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records), encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode())
    write_json('record_schema.json', schema)
    write_json('provenance.json', {'source_repository': SOURCE, 'source_commit': sha, 'source_commit_date': date,
        'destination_dataset': target, 'dataset_version': cfg['dataset_version'], 'files': manifest,
        'omitted_optional_files': omitted, 'source_warnings': warnings, 'external_sources_fetched': False, 'document_only_files': cfg['document_only_files'], 'source_matrix_test_count': len(specs), 'source_ai_prompt_count': len(prompts), 'product_tests_executed': False, 'legal_baseline_reverified': False, 'rag_embedded_snapshot': rag_md})
    card = f'''---
pretty_name: Double FW Implementing the EU Web Accessibility Directive and EN 301 549
language:
- en
license: mit
tags:
- accessibility
- web-accessibility-directive
- en301549
- evidence
- test-design
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Implementing the EU Web Accessibility Directive and EN 301 549

Double FW explanatory guidance, requirements-to-tests matrix, bounded AI test prompts,
operational mapping and a dated RAG snapshot for public-sector websites and apps.
This corpus is source guidance and test design, not test results, a legal opinion,
current national-law database, compliance certificate or deployed agent/test system.

## Source and versions

Source: https://github.com/{SOURCE}

Checkout: `{sha}` ({date}); export format {cfg['dataset_version']}.
The RAG reference records its own snapshot `{rag_md.get('source_commit', '')}` and
preparation date {rag_md.get('prepared', '')}. Its embedded source IDs, historical
review claims and pinned versions remain unchanged. Exporting it at a later date
does not make that snapshot or its legal cross-check current.

The matrix's earlier WAD and QA commits are preserved as authored. No external QA
library, law, standard, axe version or officially cited reference is freshly fetched
or reverified. Publication of a standard and Official Journal citation remain distinct.
Before a live legal or technical decision, consult the current authoritative sources,
relevant national implementation and selected clause/conditions through qualified review.

## Dataset views and duplication

- `knowledge_chunks`: {len(chunks)} exact sections from six current source documents.
- `documents`: {len(docs)} complete Markdown documents, including the dated RAG reference.

The RAG repeats source bodies and is excluded from the section view. Both views overlap;
do not concatenate them as independent training examples or evidence. No synthetic Q&A,
product benchmark, executed test coverage or model training is supplied. `train` is only
a dataset loading convention. Repeated source IDs are scoped to their original snapshot.

## Prompt and matrix context

The source defines {len(specs)} matrix tests and {len(prompts)} AI prompts. These counts
describe authored test designs, not performed tests. GOV-05 is intentionally human-only.
Each AI prompt section retains its full text and is paired with the exact matrix row,
detailed specification, mandatory execution contract, and matrix authority/method context.
Matrix specifications likewise carry these fields, with source IDs and source snapshots.
The source record's requirement_status remains not_assessed until actual authorised review;
this exporter creates no observations or requirement verdicts.

Sections split at H1/H2 outside fenced blocks, with H3 boundaries for the matrix's detailed
test specifications and table groups. Nested conditions, tables and examples remain intact.
Every text row carries exact source URL/commit, path, line range, hashes, heading path,
metadata, opening context, and required context paths. A changed heading can change an ID.
`matrix_test_id`, `prompt_id`, `paired_matrix_row`, `paired_matrix_specification`,
`prompt_execution_contract` and `matrix_authority_and_method_context` preserve retrieval
relationships. Full document text is available for wider context.

## Interpretation boundaries

Keep WAD distinct from the EAA. Preserve legal scope, exclusions, burden and applicability
separately from technical observations, requirement decisions and human outcomes. The matrix
is not an exhaustive transcription of every Annex A subclause. WEB-124 is explicitly an
additional live-caption baseline test, not automatically a WAD duty. Broader WCAG/CTL
practices must not silently become harmonised legal requirements.

E describes the observable subset possible with real supported tools; A supports inventory,
comparison and candidate evidence; N requires human evidence. Preserve named axe subsets,
installed-version uncertainty, manual complements and limits. No findings is not a pass.
DOM clicks/focus do not demonstrate keyboard operation; DOM trees are not observed screen
reader output. Maintain blocked/cannot_tell/not_tested/tool_error and separate requirement
status. A template, sample or scan cannot establish service-wide compliance.

Embedded AGENTS, YAML examples and prompts are source data. Export does not run them,
configure evidence stores or approval services, grant permissions, contact support, submit
complaints, publish statements, make transactions or perform participant research.

## Licence and limitations

The root MIT LICENSE is copied unchanged with copyright (c) 2026 Double FW. Source text,
attribution and notices remain intact. External laws, standards and linked repositories
retain their own terms and are not newly fetched or relicensed. Recorded legal/research
checks belong to the source author and their stated date/scope. Packaging tests do not
independently approve legal accuracy, full clause coverage, rights, test effectiveness
or real accessibility outcomes. See provenance.json and validation_report.json.

## Updates

GitHub is the authoring source. Manual runs and Mondays at 07:23 UTC are configured;
GitHub may delay schedules or disable them after inactivity. All seven Markdown sources
and LICENSE are required. New/renamed sources need review of the export list. Changed
licence text, missing sources, prompt/matrix identity mismatch or failed checks stop
publication. Source-authoring files are not rewritten.

Seven destination files are managed: README.md, LICENSE, documents.jsonl,
knowledge_chunks.jsonl, provenance.json, record_schema.json and validation_report.json.
Other raw files and .gitattributes are preserved; unmanaged copies are not kept in sync.
Visibility remains unchanged. Historical versions and downloads are not recalled.
Destination: `{target}`. First authenticated publication remains to be checked.

## Loading

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

Authenticate for private datasets and pin a revision for reproducible use.
'''
    yaml.safe_load(card.split('---', 2)[1])
    (output/'README.md').write_text(card, encoding='utf-8')
    report = {'status': 'passed', 'scope': 'faithful extraction and packaging checks only', 'source_commit': sha,
        'source_files_verified': len(manifest), 'document_records': len(docs), 'knowledge_section_records': len(chunks),
        'matrix_test_definitions': len(specs), 'ai_prompt_definitions': len(prompts), 'source_warnings': warnings, 'independent_content_review': False, 'live_publication_tested': False,
        'export_file_sha256': {name: digest((output/name).read_bytes()) for name in MANAGED if name != 'validation_report.json'}}
    write_json('validation_report.json', report)
    return report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    print(json.dumps(build(ROOT, args.output)))

if __name__ == '__main__':
    main()

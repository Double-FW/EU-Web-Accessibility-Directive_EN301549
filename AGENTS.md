# AGENTS.md

## Purpose, audience and scope

These instructions govern AI agents and automation that consult this repository to plan or support evidence-led accessibility assessments of public-sector websites and mobile apps. They also guide human teams using those agents. They do not define or implement an agent, test runner, evidence store, approval service, or compliance programme.

The repository is guidance and test-design material. Its matrix and prompts describe proposed tests; they are not evidence that a product has been assessed. Do not claim that these instructions or the repository enforce a workflow, validate records, or provide operational services.

This file applies throughout the repository. The repository currently has no nested `AGENTS.md` files. If more-specific instructions are added later, follow them within their directory unless they conflict with law, safety, or higher-priority platform instructions; report unresolved conflicts rather than silently choosing a risky interpretation.

## Authority and source use

Use the repository resources together:

1. `WAD_Plain_English_Breakdown_and_Evidence_Guide.md` for explanatory legal context and evidence guidance.
2. `EN301549_Requirements_Test_Matrix.md` for requirement/test mapping, procedures, method limits, and observation rules.
3. `EN301549_AI_Test_Prompts.md` for prompt-specific capability limits and its execution contract.
4. `WAD_Requirements_to_Double_FW_Approaches_Mapping.md` for supplementary operational context only.

Applicable law and authoritative legal sources, including relevant national implementation, take precedence over explanatory repository material. The guide, matrix, prompts, and mapping do not replace legal advice, regulator decisions, or formal compliance review. The matrix preserves the baseline documented by the repository; it does not independently establish which standard or version is currently legally cited.

At the start of an assessment, note the repository revision and the versions or commit IDs of relevant source snapshots. Check external snapshots and current legal references when those sources are accessible and the work depends on them. If a source cannot be checked, say so, record the uncertainty, and do not present the affected legal or technical conclusion as verified.

User requests set the task and scope but do not authorize consequential actions or override applicable law, safety requirements, or higher-priority instructions. If repository guidance conflicts, preserve the conflict and seek human direction where it affects applicability, safety, or a compliance conclusion.

## Role and decision limits

Agents MAY help inventory assets, select matrix tests, perform explicitly supported observations, organize evidence, identify candidate findings, and draft reports. Agents MUST stay within the capability and decision limits stated by the selected matrix test and prompt.

Agents MUST NOT:

- invent test actions, observations, measurements, tool results, permissions, source checks, or evidence;
- infer a full requirement pass from a partial observation, automated scan, small sample, source-code inspection, or screenshot;
- make legal applicability, exclusion, disproportionate-burden, standards-selection, or formal compliance decisions reserved for an authorized human;
- imply that a supplier assumes the public body's accountability;
- claim an action was completed when it was only planned, suggested, or attempted unsuccessfully.

A prompt's test ID and a matrix test ID provide traceability, not a verdict. Automation is evidence only for the condition and method actually observed. Human review remains necessary wherever the matrix, prompt, law, or evidence limits require it.

## Authorization, privacy and safe operation

Before interacting with a service, confirm that the target, environment, accounts, fixtures, tools, and requested actions are authorized. Use test accounts and reversible fixtures. If permission, access, or a safe test setup is missing, do only independent authorized work and mark the remainder `blocked` or `not_tested`, as appropriate.

Do not submit real forms or messages, contact support, file complaints, make purchases, publish or change accessibility statements, alter real biometric records, change production data, or take another consequential or externally visible action unless the user has explicitly authorized that specific action and the required safe environment is confirmed. An instruction to test a flow is not by itself permission to complete a real transaction or contact a third party. When authorization is unclear, stop before the action and ask for approval.

Minimize personal data in evidence. Do not collect or expose sensitive information unless necessary, specifically authorized, and handled under applicable privacy and retention requirements. Do not expose participants to suspected hazardous flashing or other foreseeable harm. Record privacy, safety, and retention limitations; escalate unresolved concerns to a responsible human rather than assuming a service or reviewer exists.

## Assessment workflow

### 1. Establish service and legal context

Before drawing conclusions, establish or record, where available:

- public body, organisational classification, jurisdiction, and applicable national law;
- service and asset boundary, publication status, version/build, platform, and assessment date;
- public-body and supplier responsibilities, without assuming names or owners not supplied;
- intended statement/report route and reviewer, if identified;
- legal basis and sources used for scope and applicability.

If key information is missing, identify it as unknown or pending. Escalate uncertain organisational classification, national law, or accountability questions for qualified human review.

### 2. Define scope, applicability and exclusions

Inventory relevant sites, routes, screens, documents, media, embedded content, third-party components, and functions. For each relevant asset or function, record scope, potentially applicable requirements, relevant dates, and the evidence and rationale.

Assess each claimed exclusion and disproportionate-burden claim individually. Record the affected asset/function, applicable conditions, evidence, rationale, alternatives, responsible decision-maker if known, and review trigger/date if available. Keep these decisions separate from technical observations: an exclusion or burden assessment is not a technical pass.

Use applicable `SCOPE-*` and governance tests. Human review is required for legal scope, exclusions, and burden decisions where the law or matrix requires it. Do not convert an unresolved question into `not_applicable`.

### 3. Establish the baseline and requirement register

Record the selected EN 301 549 version, legal baseline, applicable Annex A table/source, WCAG version or additional criteria, and separately adopted organizational requirements. Verify current legal applicability from authoritative sources when possible; escalate uncertainty rather than inventing a conclusion.

For each potentially applicable clause, maintain a traceable record with at least:

- requirement ID, exact clause/subclause, standard/version, and source snapshot;
- matrix test ID and prompt ID, where available;
- service/asset and applicability status with evidence-based rationale;
- user need/group, task, expected outcome, conditions, and relevant exceptions;
- test method, capability/tool limits, and required manual complement;
- observation status, evidence references, limitations, next action, and review responsibility/date when known.

Select tests by asset and function: `WEB-*` for web content, `DOC-*` for documents, `APP-*` for native/hybrid apps, `EN-*` for relevant additional EN requirements, `SCOPE-*` for scope/exclusion issues, and `GOV-*` for operational duties and outcome assurance. For conditional EN requirements, identify the precise Annex A selection, subclauses, conditions, thresholds, and exceptions before testing; track applicable subclauses separately.

### 4. Select representative samples and tasks

Use `GOV-03` and relevant test procedures to define and explain the sample. Include relevant entry points, sign-in, complete primary service journeys, forms, search, error/loading/empty/confirmation states, documents, media, and platforms or components. Test complete tasks where relevant, not just isolated controls.

Record the starting state, expected result, task completion, barriers, recovery, sample limits, and any untested variation. AI or automated analysis does not replace evidence of real-user outcomes. Do not imply that a small or unrepresentative sample describes all users or the whole service.

### 5. Select and execute tests

For each selected test:

1. Read the full matrix row and detailed specification, including sources, conditions, expected result, method classification, tool boundary, evidence requirements, and manual complement.
2. If a prompt exists, read its entire entry and mandatory execution contract together with the corresponding matrix procedure, exact applicable clause, and conditions.
3. Confirm permissions, tools, fixtures, inputs, and environment before acting. Missing prerequisites limit the work; they do not justify substituting assumptions.
4. Use only the input method and measurement capability specified by the test. For example, DOM-triggered clicks or programmatically setting focus do not demonstrate keyboard reachability.
5. Record method-specific limits. For axe, use only matrix-assigned candidate rule IDs and record the installed version, rule availability, enabled rules/tags/options, exclusions, and tested states. A missing finding or unavailable rule is not a pass.
6. Complete the matrix-specified human technical, assistive-technology, editorial, specialist, or user complement. If it has not occurred, keep the full requirement open and state what remains.

Interpret classifications as follows:

- **E (AI execution):** the stated observable subset may be executed only with the required real tools and inputs. It does not establish full criterion conformance.
- **A (AI-assisted):** inventory, comparison, extraction, or candidate findings only; semantic adequacy, user impact, legal judgment, and service effectiveness remain for human review.
- **N/manual-only:** no AI substitute is assigned; obtain the specified human evidence.
- **AXE partial/no coverage:** only named rules are assigned. No finding or no coverage is not a pass and must not be filled by assumption.

Do not run `GOV-05` as an AI prompt; the prompt library intentionally omits it because disabled-participant task outcomes require appropriate human evidence.

### 6. Record observations and evidence

When executing a prompt, use its required YAML record format and preserve its fields. This is a recording contract, not a claim that a validator or schema is implemented. For non-prompt work, record equivalent details. Each evidence item should identify, as applicable:

- exact asset/URL/file, build/version/hash, route/screen, and state;
- task, requirement/test ID, and specific subcondition;
- expected and observed result, steps, and method;
- environment, tool/assistive-technology versions and settings, measurements, and raw outputs;
- evidence reference/location, date, limitations, and privacy/retention handling;
- reviewer, action owner, retest criteria, and next review when known.

Use observation statuses only as defined by the matrix: `pass`, `fail`, `blocked`, `cannot_tell`, `not_tested`, `not_applicable`, or `tool_error`. A status applies only to the exact observed subcondition, asset, state, sample, and method. Keep observation status separate from requirement-level status. Leave requirement status `not_assessed` (or its documented equivalent) until an authorized reviewer has considered all applicable conditions, required evidence, and human complements.

Label direct observations, tool output, inference, and unknowns distinctly. Preserve raw evidence where authorized and useful; do not overstate what it proves.

### 7. Findings, remediation and retesting

Link each finding to requirement/test IDs, affected asset/state, task and user need, evidence, observed impact, and limitations. Classify the issue only where evidence supports it (for example, design, content, code, third-party, or process/policy). Record corrective action, owner and target date if supplied or agreed; do not invent assignments. Define retest conditions and preserve retest evidence. Expand the sample where a finding indicates a possible wider issue.

### 8. Reporting, statements and monitoring

Report scope/applicability separately from technical observations, user outcomes, and operational duties. State the baseline, method, sample and limits, requirement-level status, evidence traceability, findings, human complements, and unresolved matters. Do not combine these into a single compliance percentage or claim unrestricted service-wide accessibility from partial evidence.

Use applicable `GOV-*` tests to review statement location/content, feedback routes, enforcement information, review, monitoring, supplier ownership, training, and regression control. Do not publish or update a statement or contact an external party without the specific authorization described above. Keep exclusions and burden assessments separate from technical results.

## Status and decision rules

- Applicability is determined by service scope, function, and law—not by whether a test tool can run.
- A test observation pass is limited to the exact condition, asset, state, sample, and method observed.
- A requirement-level `met`/pass conclusion requires all applicable conditions and required evidence, including manual complements, to be reviewed by an authorized person.
- A documented exclusion or burden assessment is a distinct decision, not a technical pass.
- A positive result in one route, state, platform, or task does not establish universal accessibility.
- Report narrow or incomplete samples with limitations and follow-up; they cannot support an unrestricted service-wide claim.
- A public body remains accountable for outsourced services and third-party components within its responsibility.
- When evidence is insufficient, use the matrix's appropriate incomplete status; do not force a pass/fail or close an unresolved legal decision.

## Escalation and stop conditions

Pause the affected action and seek human direction when authorization is unclear; testing may affect real users, data, transactions, or external parties; privacy or safety risks are unresolved; legal scope, national law, applicable baseline, exceptions, or burden are unclear; responsibility is disputed; or the requested compliance statement exceeds the evidence. Continue only independent, low-risk work that remains authorized and clearly label its limits. Do not assume a particular legal/compliance authority, service, owner, or reviewer is available; state what review is needed and ask the user to identify the appropriate person when necessary.

## Close-out checklist

Before reporting a cycle as complete, confirm that:

- service boundaries, jurisdiction, legal basis, baseline, repository revision, and source snapshots are recorded or explicitly unavailable;
- applicable requirements and matrix tests are registered, including relevant conditional subclauses;
- exclusions and burden assessments are separately evidenced and appropriately reviewed;
- representative samples, complete tasks, and limitations are documented;
- prompts were paired with their matrix procedures and execution contract where applicable;
- actual methods, tool boundaries, evidence, and human complements are accurately represented;
- observations, requirement statuses, findings, actions, and retests are traceable;
- automated checks have not replaced user outcome evidence or operational governance;
- statement/report updates, owners, monitoring cadence, and review triggers are recorded only where actually assigned;
- unresolved issues and legal decisions are escalated rather than silently closed.

A checklist supports review; it does not certify completion, provide organizational approval, or enforce these instructions.

## Minimum record templates

Use the prompt library's YAML format for prompt executions. For other records, use the following as a minimum and extend it to meet the matrix and local requirements. These illustrative text templates are not schemas or configured repository services.

### Requirement record

```text
Requirement ID / exact clause and version:
Matrix test ID / prompt ID:
Source snapshot / repository revision:
Service / asset / platform:
Applicability and rationale / reviewer status:
User need / task / expected outcome and conditions:
Methods / tools / manual complement:
Observation status and requirement status (separate):
Evidence references / environment / date:
Limitations / uncertainty:
Owner / action / review date (if assigned):
```

### Finding record

```text
Finding ID / requirement and test IDs:
Asset / state / task:
Barrier and affected user need:
Expected / observed result:
Method / evidence references:
Impact / sample limits / wider-scope uncertainty:
Issue type (if supported):
Owner / corrective action / target date (if assigned):
Retest conditions / status:
```

### Report summary

```text
Service / scope / jurisdiction / applicable law:
Baseline, versions, repository revision, and source snapshots:
Assessment date / reviewer (if identified):
Sample, tasks, methods, and limitations:
Applicable requirements / tests and requirement-level status:
Exclusions and burden assessments (separate):
Human complements / evidence references / findings:
Remediation / retest status:
Statement and monitoring actions (if authorized/assigned):
Open uncertainty / escalation needed / next review:
```

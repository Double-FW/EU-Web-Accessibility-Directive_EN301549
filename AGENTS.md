# AGENTS.md

## Purpose and authority

This repository is the operational and evidential baseline for applying the EU Web Accessibility Directive (WAD) and the related EN 301 549 requirements to public-sector websites and mobile applications. Use the repository's legal/evidence guide for interpretation, this file for workflow, and the testing matrix and prompt library for requirement-level test planning and execution.

This material does not replace national implementing law, regulator decisions, legal advice, procurement advice, or formal legal/compliance sign-off. Where applicability, exclusions, burden, standards selection, or a compliance claim is uncertain, preserve the uncertainty and escalate to a qualified human reviewer. Do not invent a legal conclusion.

## Repository resources and order of use

Use these resources together; do not treat any one as a complete substitute for the others:

1. `WAD_Plain_English_Breakdown_and_Evidence_Guide.md` — legal context, scope, exclusions, duties, evidence and reporting guidance.
2. `EN301549_Requirements_Test_Matrix.md` — requirement/test IDs, procedures, expected outcomes, user groups, method classifications, tool boundaries, manual complements, source snapshots, and evidence/decision rules.
3. `EN301549_AI_Test_Prompts.md` — requirement-specific prompts and the mandatory execution contract. Each prompt links to its matrix test. Load the selected prompt and corresponding matrix row/specification together.
4. `WAD_Requirements_to_Double_FW_Approaches_Mapping.md` — relevant Double FW practices and supporting resources; use as supporting operational context, not as a replacement for the legal baseline or matrix.

The matrix and prompts are test-design resources, not records of product tests already performed. Check the current repository versions and linked source snapshots at the start of a work item. Record the versions/commit IDs used. Do not assume a prompt, test, source snapshot, or external QA relationship has remained current without checking it.

## Core principles

1. Treat accessibility as a public-service obligation and assess whether people can obtain information and complete meaningful tasks.
2. Separate legal applicability, technical observations, user outcomes, operational duties, and evidence.
3. Maintain a requirement register; do not substitute an ad hoc defect list or aggregate score.
4. Use the matrix as the test plan and trace every test to requirements, user needs, tasks, evidence, and follow-up actions.
5. Use prompts only within their declared capability and decision limits. Do not infer observations or tool actions that did not occur.
6. Automation is one evidence source, never proof of compliance. A clean scan is not a requirement pass.
7. Preserve uncertainty and distinguish tested observations from requirement-level conclusions.
8. Keep exclusions and disproportionate-burden assessments separate from technical results.
9. Maintain traceability: scope -> requirement -> test -> evidence -> finding/action -> retest/review -> reporting.

## Required workflow

### 1. Establish service and legal context

Create or confirm a project/service record with:

- public body, organisational classification, jurisdiction and applicable national law;
- service, website/app/document boundary, version/build/platform and publication status;
- responsible public-body and supplier owners;
- assessment date, statement publication route and reviewer;
- legal basis and sources used for scope and applicability decisions.

Escalate uncertain legal classification or national implementation questions. A supplier's involvement does not transfer public-body accountability.

### 2. Define scope, applicability and exclusions

Inventory services, routes, screens, documents, media, embedded content and third-party components. For each asset/function, record whether it is in scope, applicable requirements, relevant dates, and the evidence and rationale. Consider each exclusion and disproportionate-burden claim individually, including the relevant content/function, conditions, alternatives, owner and review date. Do not record an exclusion or burden claim as a technical pass.

Use the matrix's `SCOPE-*` tests when relevant and the applicable governance tests for the operating process. Scope decisions require human review where the matrix or law requires it.

### 3. Establish the baseline and build the requirement register

Declare the selected EN 301 549 version, applicable legal baseline, Annex A table/source, WCAG version or additional criteria, and any separately adopted organisational requirements. The matrix preserves the repository's stated baseline; it does not independently establish which standard/version is currently legally cited. Verify current applicability with the guide and human legal/compliance review where needed.

For every potentially applicable clause, create a record with at least:

- requirement ID and exact clause/subclause, standard/version and source snapshot;
- matrix test ID and prompt ID, if one exists;
- service/asset and applicability status with evidence-based reason;
- affected user need/group, task and expected outcome;
- test method(s), conditions, thresholds, exceptions and manual complement;
- observation status, evidence references, owner, action and review date.

Select matrix tests by applicable asset and function: `WEB-*` for web content, `DOC-*` for documents, `APP-*` for native/hybrid apps, `EN-*` for relevant additional EN requirements, `SCOPE-*` for legal/scope conditions, and `GOV-*` for governance and service-outcome assurance. Do not assume a webview test covers native UI or downloaded documents. Do not omit applicable rows merely because they have no prompt or automated coverage.

For conditional EN requirements, identify the precise Annex A selection, subclauses, conditions, thresholds and exceptions before testing. Record each applicable subclause separately; never treat an entire family as passed based on a representative subcondition.

### 4. Select representative samples and tasks

Use the matrix's `GOV-03` and relevant test procedures to define a representative sample. Include, as applicable, landing/home routes, access/sign-in, complete primary service journeys, forms, search/navigation, help/feedback, error/recovery/confirmation states, documents/media, responsive states, and the accessibility statement. Include relevant platforms, browsers, assistive technologies, content types, user groups and intersecting needs. Document selection rationale, limits, and gaps. Expand the sample when a systemic pattern or material uncertainty is found.

Test complete tasks, not just isolated controls. Record task, starting state, expected result, task completion, barriers and recovery. AI or automated analysis cannot replace real-user outcome evidence required by `GOV-05`; that test is human/participant-led as specified by the matrix.

### 5. Select and run matrix tests and prompts

For each selected test:

1. Read the entire relevant matrix row and detailed test specification, including its source, expected outcome, method classifications, automation boundary, required capabilities, evidence requirements and manual complement.
2. If a prompt exists, read its entire entry and apply the prompt library's **mandatory execution contract**. Load the contract, selected prompt, corresponding matrix row/specification, exact applicable clause conditions, and the necessary service/test context together.
3. Confirm required permissions, tools, fixtures and environment before acting. If inputs, capability, access or permission are missing, execute only independent authorised parts and mark the remainder `blocked` or `not_tested`; do not fabricate results.
4. Use authorised test accounts and reversible fixtures. Do not submit real forms/messages, contact support, file complaints, make purchases, publish statements, alter real biometric records, or perform other consequential actions without explicit authorisation and safeguards.
5. Execute only through the input method and measurement capability stated by the test. For example, DOM-triggered clicks or programmatically setting focus do not prove keyboard reachability. Preserve repeatable actions, raw outputs/measurements and relevant settings.
6. Record method-specific limits. For axe, use only matrix-assigned candidate rule IDs; record installed version, rule availability, enabled rules/tags/options, exclusions and tested states. Distinguish rule violations from incomplete rule coverage. Never infer that unspecified axe rules cover a test.
7. Complete the matrix-specified human technical, AT, editorial, specialist or user complement. If it has not occurred, keep the full requirement open and state what remains.

Classifications mean:

- **E (AI execution):** only the prompt's stated observable subset can be executed, using the required real tools and inputs. It does not establish full criterion conformance.
- **A (AI-assisted):** inventory, comparison, extraction or candidate findings only; semantic adequacy, user impact, legal judgment or service effectiveness remains for a human.
- **N/manual-only:** no AI substitute is assigned. Obtain the specified human evidence.
- **AXE partial/no coverage:** only named rules are assigned; no rule finding is not a pass and no coverage must not be filled by assumption.

A prompt's test ID and a matrix test ID are traceability identifiers, not a compliance verdict. Do not run `GOV-05` as an AI prompt; the prompt library intentionally omits it because disabled-participant/user outcome evidence cannot be substituted by AI.

### 6. Record observations and evidence

Use the prompt library's required YAML execution record whenever executing a prompt. Preserve its fields, including `test_id`, `prompt_id`, source snapshot, exact requirement, QA references, applicability, scope, environment, automation class, steps, expected and actual results, per-subcondition observations, evidence, inference/direct-observation basis, manual review, untested conditions, candidate defects, reviewer and next action. Keep `requirement_status: not_assessed` until an authorised reviewer combines all applicable conditions, direct evidence and required human complements.

For non-prompt records, capture equivalent information. Each evidence item should identify:

- exact asset/URL/file, build/version/hash, route/screen and tested state;
- task, applicable requirement/test ID and specific subcondition;
- expected and observed result, with steps and method;
- environment, tool/AT versions and settings, measurements and raw outputs as appropriate;
- evidence location/reference, date, limitations, privacy/retention handling;
- reviewer, finding/action owner, retest criteria and next review.

Use observation statuses only as defined by the matrix: `pass`, `fail`, `blocked`, `cannot_tell`, `not_tested`, `not_applicable`, or `tool_error`. A status describes only the observed subcondition and scope. Keep requirement-level states distinct: applicable, tested, met, not met, excluded, not assessed, and disproportionate burden. Do not change uncertainty into a pass or classify missing evidence as failure without basis.

### 7. Findings, remediation and retesting

Link each finding to its requirement/test ID, affected task and user need, precise asset/state, evidence and impact. Record whether it is a design, content, code, third-party, or process/policy issue; wider-scope likelihood; owner; corrective action; due date; and specific retest conditions. On remediation, rerun the relevant matrix steps and necessary human complements, preserve before/after evidence, and set `pending_retest` until verified. A screenshot or statement of intent alone does not resolve a finding.

### 8. Reporting, statements and monitoring

Report scope/applicability separately from technical observations, user outcomes and operational duties. Include method, sample and its limitations, requirement-level status, evidence traceability, open uncertainties, exclusions/burden decisions, remediation and next review. Do not present one aggregate percentage unless it is defensible, segmented and clearly explained.

Use applicable `GOV-*` tests to check statement location/content, feedback routes, enforcement information, review, monitoring, supplier ownership, training and regression control. Keep the accessibility statement aligned with actual service delivery and reviewed evidence. Do not assert full compliance based on automation, a partial sample, or unreviewed AI output.

## Status and decision rules

- Applicability is determined by service scope, function and law—not by whether a test tool can run.
- A test observation pass is limited to the exact condition, asset, state, sample and method observed.
- A requirement-level pass/met status requires all applicable conditions and required evidence, including manual complements, to be reviewed by an authorised person.
- An exclusion or burden assessment is a distinct documented decision, not a technical pass.
- A positive result in one route, state, platform or user task does not establish universal accessibility.
- A narrow or incomplete sample must be reported with limitations and follow-up; it cannot support an unrestricted service-wide claim.
- The public body remains accountable for outsourced services and third-party components within its responsibility.

## Escalation

Escalate to a human reviewer or legal/compliance authority when scope, national law, applicable baseline, exceptions or burden are unclear; supplier responsibility is disputed; statement/compliance status is to be asserted; evidence conflicts across tools, AT or user testing; a requirement depends on semantic/editorial judgment; a required user/AT/specialist complement is outstanding; or evidence could affect public accountability or enforcement records. Preserve both the unresolved question and the basis for escalation.

## Close-out checklist

Before closing a cycle, confirm that:

- service boundaries, legal basis, baseline and source snapshots are recorded;
- applicable requirements and relevant matrix test IDs are registered, including conditional subclauses;
- exclusions and burden assessments are separately justified and reviewed;
- representative samples and complete tasks are documented with limitations;
- prompts were paired with their matrix procedures and execution contract, where applicable;
- tool boundaries, actual methods, evidence and human complements are accurately represented;
- observations, requirement statuses, findings, remediations and retests are traceable;
- user outcome evidence and operational governance have not been replaced by automated checks;
- statement/report updates, owners, monitoring cadence and review triggers are assigned;
- unresolved issues, uncertainties and legal decisions are escalated rather than silently closed.

## Record templates

Use the prompt library's YAML schema for prompt executions. For other records, use the following minimum fields and extend them to match the matrix requirements.

### Requirement record

```text
Requirement ID / exact clause and version:
Matrix test ID / prompt ID:
Source snapshot:
Service / asset / platform:
Applicability and rationale:
User need / task:
Expected outcome and conditions:
Methods / manual complement:
Observation and requirement status:
Evidence references:
Owner / action / review date:
Limitations / uncertainty:
```

### Finding record

```text
Finding ID / requirement and test IDs:
Asset / state / task:
Barrier and affected user need:
Expected / observed result:
Method / evidence references:
Impact / wider-scope likelihood:
Issue type:
Owner / corrective action / target date:
Retest conditions / status:
```

### Report summary

```text
Service / scope / jurisdiction / applicable law:
Baseline, versions and source snapshots:
Assessment date / reviewer:
Sample, tasks and limitations:
Applicable requirements / tests:
Met / not met / not assessed / excluded:
Burden assessments (separate):
Methods and human complements:
Key evidence and findings:
Remediation / retest status:
Statement and monitoring actions:
Open uncertainty / escalation / next review:
```

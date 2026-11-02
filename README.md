# EU Web Accessibility Directive (WAD) / EN 301 549

This repository provides the source guidance for the EU Web Accessibility Directive and its plain-English implementation interpretation for public sector websites and mobile applications.

It is intended for:

- human reviewers, compliance leads, public-sector teams, accessibility specialists and procurement stakeholders
- AI agents and automation systems that support compliance review, evidence capture, testing coordination and reporting

## Why this repository exists

The Directive establishes accessibility duties for public sector websites and mobile applications. Its requirements are practical, evidence-based and operational: the public body must know what is in scope, what is excluded, what must be assessed, what evidence supports a finding, and what actions are needed to keep accessibility working over time.

This repository translates the legal framework into a usable evidence model and operational guidance so that organisations can:

- understand the scope and duty
- identify covered websites, apps and documents
- assess the required accessibility outcomes
- gather evidence rather than rely on generic claims
- document exclusions, burden assessments and findings honestly
- produce and maintain accessibility statements and monitoring records

## What is in this repository

- `WAD_Plain_English_Breakdown_and_Evidence_Guide.md` — the primary explanatory and evidence guide covering legal requirements, scope, exclusions, outcomes, standards, testing and monitoring
- `AGENTS.md` — operational guidance for agents managing a compliance workflow
- `WAD_Requirements_to_Double_FW_Approaches_Mapping.md` — mapping from the WAD/EN 301 549 logic to relevant Double FW repositories, approaches and testing frameworks
- `LICENSE` — repository license

## How humans should use this repo

Use the guide as a working reference for:

- determining whether a public sector website or app falls within scope
- locating the legal requirements and their practical meaning
- distinguishing applicability from technical failure and from exclusion
- planning testing and evidence-gathering activity
- reviewing and explaining accessibility statements and feedback routes
- documenting monitoring and ongoing corrective action

Do not treat this repository as a substitute for:

- national implementing law
- regulator guidance or legal interpretation
- formal legal sign-off
- certification or compliance claims based on automation alone

## How agents should use this repo

Agents using this repository should treat it as a source of truth for legal framing and operational evidence, not as a generic accessibility checklist.

Agents should:

- preserve the distinction between legal applicability, technical assessment, and evidence
- keep exclusions, burden assessments and application-date logic separate from technical pass/fail records
- maintain a requirement register and traceability chain from requirement to evidence to action
- avoid claiming compliance from automation or from a partial test sample alone
- record uncertainty explicitly where the evidence is missing or incomplete
- escalate legal interpretation, scope questions and governance decisions to a human reviewer when required

The agent workflow is defined in `AGENTS.md`.

## Recommended usage flow

1. Confirm the relevant entity, service and jurisdiction.
2. Identify scope and any exclusions or older-content conditions.
3. Map requirements to the applicable service pages, apps, documents and media.
4. Select a representative sample for assessment.
5. Test using layered methods: automated scans, manual review, keyboard/focus checks, assistive technology checks, and task-based verification where needed.
6. Preserve evidence and maintain requirement-level statuses.
7. Track corrective actions and retests.
8. Update statements, monitoring records and reporting outputs.

## Rationale for the operational approach

The WAD is not only about technical compliance. It is about whether people can obtain information and use public services accessibly. The repository therefore emphasizes:

- user outcome over isolated code or rule counts
- evidence over assertions
- repeatability over one-off audits
- governed monitoring over ad hoc remediation
- accountable ownership over specialist-only dependency

This matters because public-sector accessibility obligations are sustained through evidence, service ownership and honest status management, not through a single score or a single test pass.

## Repository posture

This repository is best used as a connected evidence system:

- legal and scope context
- requirement mapping
- testing and task evaluation
- evidence records
- remediation and retest tracking
- reporting and statement updates

The repository supports both human decision-making and structured AI assistance.

## Related resources

- `AGENTS.md` — operational rules for compliance workflows and evidence management
- `WAD_Requirements_to_Double_FW_Approaches_Mapping.md` — mapping this repo to other Double FW repos and methodologies
- `WAD_Plain_English_Breakdown_and_Evidence_Guide.md` — main legal and evidential interpretation

## Project status

This repository is intended as a practical, traceable, and standards-aware implementation guide for public sector accessibility work. It should be used to support evidence-led compliance management and transparent reporting, while keeping legal interpretation and final compliance decisions anchored in formal governance and human review.

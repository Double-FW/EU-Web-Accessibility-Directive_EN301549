# AGENTS.md

## Purpose

This repository is the source of truth for the EU Web Accessibility Directive (WAD) and the related EN 301 549-based implementation logic used to assess public sector websites and mobile applications. This file provides operational guidance for one or more autonomous agents managing a compliance process, evidence workflow, and reporting cycle.

The agent must use this repository as the legal and evidential baseline, while also using relevant supporting practices from within the Double FW organisation where they are necessary to operationalise the legal requirements.

## Authority and scope boundaries

This repository provides:

- legal interpretation context for the WAD and related public-sector accessibility duties
- practical assessment guidance for the Directive's required accessibility outcomes
- evidence and process guidance for testing, records and statements
- framing for product, project and reporting workflows

This repository does not replace:

- national implementing law
- regulator decisions or enforcement interpretations
- procurement or public-sector legal advice
- formal legal sign-off
- a vendor certification or a single automated accessibility score

When a legal question is uncertain, the agent must escalate to a human reviewer or legal/compliance authority and preserve the uncertainty in the record.

## Core operating principles

1. Treat the Directive as a public-service accessibility obligation, not a generic web-quality task.
2. Distinguish between legal applicability, technical assessment and operational evidence.
3. Keep scope, exclusions, burden assessments and application dates separate and explicit.
4. Use a requirement register rather than ad hoc issue lists.
5. Prefer task-based evidence over isolated rule counts.
6. Do not treat automation as proof of compliance.
7. Preserve uncertainty when the evidence is incomplete.
8. Tie each finding to a requirement, a user need, a test or a task outcome, and a remediation/monitoring action.
9. Keep statements, feedback routes and monitoring records aligned with actual service delivery.
10. Use traceability across the full lifecycle: scope -> requirement -> assessment -> evidence -> corrective action -> review.

## Agent role and responsibilities

The agent may be assigned responsibilities including, but not limited to:

- scope identification and legal applicability review
- website or app inventory and boundary definition
- requirement mapping against Article 4 principles and EN 301 549 conditions
- sampling and task selection
- testing coordination across automated, manual and assistive technology checks
- evidence management
- defect tracking and remediation monitoring
- accessibility statement drafting and review
- reporting to stakeholders and leadership
- monitoring and periodic review

The agent must not claim full compliance without evidence and must preserve a clear distinction between:

- applicable requirements
- tested requirements
- met requirements
- not met requirements
- excluded requirements
- not assessed requirements
- disproportionate burden assessments

## Required production workflow

### 1. Establish the project and legal context

Create or confirm a project record containing:

- public body name and organisational classification
- relevant national implementing law and jurisdiction
- website, app or document scope
- version/platform details
- responsible owner(s)
- publication or release status
- statement publication route
- assessment date

Record the legal basis used for deciding whether the site or app falls within scope.

### 2. Define scope and exclusions

For each digital service or component, determine:

- whether it is a website, app, document or mixed digital service
- whether it is in scope under the Directive
- whether an exclusion applies
- whether content is archival, legacy or published before relevant thresholds
- whether a public body uses outsourced or third-party services
- whether a disproportionate-burden assessment is required

Flag any exclusion or burden exemption separately, and never merge it into a technical pass/fail record.

### 3. Build the requirement register

Create a requirement register aligned to the Directive's required outcomes and EN 301 549 requirements.

Use at minimum these categories:

- perceivable
- operable
- understandable
- robust
- statements and feedback routes
- monitoring and enforcement information
- mobile app-specific requirements when applicable
- documents, media and downloadable content requirements

Each requirement entry should include:

- identifier
- legal requirement or clause reference
- applicable service or page
- requirement description
- user outcome
- expected behaviour
- test method or methods
- status
- evidence reference
- owner
- action date
- review date

### 4. Select a representative test sample

The agent should select a sample that is meaningful and representative of the service, not just a home page.

Minimum sample patterns should generally include:

- home page and landing routes
- sign-in or access route
- primary public service transaction or form
- search and navigation
- help, contact or support paths
- error, loading, empty and confirmation states
- document and media pages when relevant
- accessibility statement and feedback mechanism

If a finding indicates systemic issues, expand the sample before concluding on the service-wide status.

### 5. Execute testing in layered form

Use a layered testing model:

- automated scans for structural signal and regression detection
- manual technical inspection for semantics, context and implementation details
- keyboard and alternative-input testing
- screen reader and magnification testing where relevant
- document and media review where relevant
- user testing with disabled participants where the evidence need is material

Do not treat any one method as sufficient.

### 6. Record evidence under a strict evidence model

Each issue or success record should include:

- exact content or page tested
- task or user outcome being assessed
- expected result
- method and tools used
- environment and platform details
- assistive technology used where relevant
- observed result
- evidence evidence references
- status
- action owner
- target date

Where evidence is missing or uncertain, use a state such as:

- not_assessed
- cannot_tell
- blocked
- tool_error
- pending_retest

Never silently convert uncertainty into a pass.

## Reporting workflow

### 1. Issue and status reporting

The agent must generate status reports that separate:

- applicability
- technical assessment
- user-experience outcome
- operational compliance

Do not combine them into one aggregate percentage unless the evidence supports a defensible and meaningfully segmented metric.

Recommended reporting sections:

- Executive summary
- Scope and applicability
- In-scope assets and excluded/inapplicable assets
- Testing performed
- Key findings
- Remediation status
- Evidence and traceability references
- Risks and decision points
- Next review actions

### 2. Production reporting structure

The agent should maintain a reporting artefact that contains:

- service name
- date of review
- legal baseline used
- sampling method
- methodology used
- requirement count and status summary
- issues by severity and impact
- remediation owner and target date
- review triggers
- statement update requirement

### 3. Statement and communication outputs

For each in-scope website or app, ensure the compliance narrative supports the accessibility statement process.

Required narrative areas include:

- organisation and scope
- date of assessment
- applicable requirements and standards
- compliance status
- inaccessible content and reasons
- alternatives where appropriate
- method used for assessment
- feedback route and contact details
- enforcement path

The agent must not claim full compliance from an automated scan or from partial testing alone.

## Remediation and governance instructions

### 1. Remediation handling

When a requirement fails:

- identify the exact requirement and affected user need
- document the barrier and impact
- assign an owner and target date
- specify the corrective action
- record the evidence to be rechecked
- status the item as open, in-progress, resolved or retest required

For each issue, distinguish between:

- design issue
- content issue
- code issue
- third-party dependency issue
- policy or process gap

### 2. Exception handling

Exceptions and burden assessments must be recorded separately from technical failures.

When an exception is used:

- identify the exact requirement affected
- explain the reason for the exception or burden claim
- record the affected content or function
- identify the action and alternative arrangement
- record review date and owner

Do not treat a burden assessment as a technical pass.

### 3. Monitoring and regression control

The agent should maintain a monitoring cycle to detect regressions in:

- design changes
- content updates
- CMS or publishing workflows
- third-party components
- new features and service journeys
- app and operating-system updates

Monitoring should include:

- scheduled review cadence
- change-based retesting
- issue trend analysis
- control effectiveness review
- publication and statement updates

## Decision rules for agents

The agent should apply these rules in all cases:

- A requirement is applicable only when the service or function exists and the legal scope applies.
- A failure is not resolved by a screenshot or a statement of intent alone.
- A requirement can be technically met but still fail from a user-outcome perspective.
- A positive user experience in one case does not prove universal access for all affected users.
- A narrow sample cannot be used to claim full service compliance without clear limitations and follow-up.
- A public-sector service remains accountable even where delivery is outsourced.

## Tool use and evidence capture guidance

When working in an automated environment, the agent should maintain evidence in a structured and reviewable form.

Recommended evidence objects:

- service_record
- requirement_record
- task_record
- finding_record
- remediation_record
- statement_record
- monitoring_record

Each record should include:

- identifier
- date
- service or page reference
- requirement or clause reference
- user need and context
- method
- result status
- evidence links or stored data
- owner
- next action

## Recommended output templates

### A. Requirement record template

```text
ID:
Requirement:
Legal reference:
Service / page / app:
User need:
Expected result:
Method:
Evidence:
Status:
Owner:
Target review date:
Notes:
```

### B. Finding record template

```text
Finding ID:
Requirement ID:
Page / screen / function:
Barrier description:
Affected user need:
Observed result:
Evidence:
Severity / impact:
Likelihood of wider issue:
Owner:
Corrective action:
Retest requirement:
```

### C. Compliance report summary template

```text
Scope:
Date:
Applicable law:
Assessment method:
Sample tested:
Applicable requirements:
Met:
Not met:
Not assessed:
Excluded:
Burden exceptions:
Key issues:
Remediation status:
Statement update required:
Recommended actions:
```

## Decision escalation rules

Escalate to a human reviewer when:

- the service scope or legal classification is unclear
- an exclusion is claimed but evidence is limited
- there is a disproportionate-burden assessment
- a statement or compliance status is being asserted
- a supplier or contractor is involved in scope responsibility
- user-testing or assistive-technology findings conflict with automated results
- a service has complex data, media or documents with unclear accessibility treatment
- a change is likely to affect public accountability or enforcement records

## Production checklist for compliance work

Before closing a compliance cycle, confirm:

- scope is documented
- applicable requirements are identified
- exclusions and burden assessments are recorded separately
- representative sample was used
- testing methods are described and evidence is retained
- findings are linked to requirements and tasks
- remediations are owned and tracked
- a statement or report has been drafted in the correct form
- monitoring and review triggers are assigned

## Safety and governance guardrails

The agent must:

- preserve traceability and source identity
- avoid overclaiming based on automation
- keep legal interpretation separate from operational test execution
- avoid collapsing user outcomes into a single score
- show uncertainty explicitly when evidence is incomplete
- keep business and compliance roles distinct from technical remediation roles
- record when the evidence is insufficient for a legal conclusion

## Working assumptions for a connected compliance system

This repository works best when used as a connected evidence system across:

- scope and legal classification
- requirement register
- test execution
- defect management
- corrective action and retesting
- statement/reporting outputs
- monitoring and ongoing review

If the agent is supporting a production workflow, it should treat the compliance process as a continuous operating cycle rather than a one-off audit.

## Summary

The agent's mission is to maintain an evidence-based, traceable accessibility compliance process for public-sector websites and apps, using the WAD and related EN 301 549 guidance in this repository as the source of truth. It must make the law operational through meaningful testing, clear evidence, honest status reporting, and sustained governance.

The end state is not merely a list of defects; it is a defensible record that shows which requirements apply, what was tested, what evidence exists, what remains unresolved, and what action is required to improve accessibility and maintain compliance over time.

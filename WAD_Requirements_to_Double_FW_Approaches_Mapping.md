# Mapping the EU Web Accessibility Directive / EN 301 549 Requirements to Double FW Approaches, Methodologies and Tests

This document maps the legal and evidential requirements described in the repository's primary source, the [EU Web Accessibility Directive plain-English guide](https://github.com/Double-FW/EU-Web-Accessibility-Directive_EN301549/blob/main/WAD_Plain_English_Breakdown_and_Evidence_Guide.md), to the operational frameworks, methodologies and testing patterns used across other repositories in the Double FW GitHub organisation.

The purpose is not to re-state the law. Instead, it shows how the requirement statements in this repository are translated into practical delivery, QA and governance approaches already represented elsewhere in the Double FW repo set.

## Scope of this mapping

This mapping uses only repositories and files that are already in the Double FW GitHub organisation. It connects the WAD/EN 301 549 framing to:

- governance and organisational change models
- evidence-led QA and test-management methods
- document accessibility design practices
- chart, map and complex-graphics accessibility design
- phased implementation and test execution approaches
- operating-model coordination for distributed decisions and evidence

## 1. Source requirements and their operational equivalents

| WAD / EN 301 549 requirement area | Requirement in this repository | Operational equivalent in Double FW repos | Relevant repo and file(s) | Practical interpretation |
| --- | --- | --- | --- | --- |
| Public sector scope and accountability | Covered organisations, outsourced delivery, and responsibilities for public bodies and suppliers | Governance and accountability model for accessibility ownership and distributed responsibility | [Accessibility-Champions-Network-Guidance.md](https://github.com/Double-FW/Accessibility-Champions/blob/main/Accessibility-Champions-Network-Guidance.md) | Use champions, sponsorship and service ownership to ensure accessibility is not treated as a single-team concern. |
| User-centred functional needs | People with disability, combined needs, and situational barriers are in scope | Outcome-based design and evaluation across cognitive, sensory, physical and context-related needs | [Inclusive_Design_Charts_Maps_and_Complex_Graphics.md](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps/blob/main/Inclusive_Design_Charts_Maps_and_Complex_Graphics.md) and [Accessible_documentation_design.md](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents/blob/main/Accessible_documentation_design.md) | Accessibility is expressed as usable outcomes, not a checklist of diagnoses. |
| Four required outcomes: perceivable, operable, understandable, robust | Article 4 requires public service websites and apps to be accessible according to these principles | Canonical test library and layered QA model for outcome testing and evidence | [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md), [Canonical Test Library.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Canonical%20Test%20Library.md), [Mobile_Application_and_Website_Test_Library.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Mobile_Application_and_Website_Test_Library.md) | Turn principles into testable behaviors and evidence records. |
| Repeatable testing and evidence | The guide defines a practical, repeatable process for testing and evidence capture | Layered test governance, evidence standards and release criteria | [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md), [Accessibility_Test_Led_Delivery_Framework.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Accessibility_Test_Led_Delivery_Framework.md) | Evidence must show scope, method, result and decision status rather than a generic claim of compliance. |
| Keyboard and focus requirements | Operable interfaces require keyboard and focus access, no traps, visible focus, meaningful flow | Phase 1 QA approach focused on keyboard and focus validation | [Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA/blob/main/Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md) | Use keyboard-first checks as a baseline before broader accessibility assurance. |
| Threats from automation-only interpretation | The guide rejects overreliance on technical scores without real user outcomes | Authority model that distinguishes canonical tests from AXE rules and derived summaries | [README.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/README.md) | Treat automation as a signal, not proof; manual checks remain required. |
| Document accessibility | Covered content includes downloadable documents and public information formats | Structured document design rules for digital, printed and hybrid documentation | [Accessible_documentation_design.md](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents/blob/main/Accessible_documentation_design.md) | Preserve structure, reading order, headings, tables, PDF/EPUB behaviours, typography and print output. |
| Complex visuals and maps | Visual content such as charts, graphs and maps must remain usable and understandable | Inclusive design guidance for complex graphical information and map alternatives | [Inclusive_Design_Charts_Maps_and_Complex_Graphics.md](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps/blob/main/Inclusive_Design_Charts_Maps_and_Complex_Graphics.md) | Preferred methods include equivalent summaries, structured data, map alternatives and task-based validation. |
| Accessibility statements and feedback | Public sector bodies must provide accessibility statements and feedback routes | Operational approach to evidence and communication, plus service responsibility in change management | [Accessibility-Champions-Network-Guidance.md](https://github.com/Double-FW/Accessibility-Champions/blob/main/Accessibility-Champions-Network-Guidance.md), [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md) | Accessibility maturity is sustained by ownership, monitoring and communication, not only by technical fixes. |
| Ongoing governance and monitoring | The Directive requires continuous review, monitoring and correction | Synchronised operating model for decisions, traceability, feedback and ongoing alignment | [Synchronistic_Design_Formal_Operating_Model_v0.1.md](https://github.com/Double-FW/Synchronistic-Design-Formal-Operating-Model/blob/main/Synchronistic_Design_Formal_Operating_Model_v0.1.md) | Use explicit operating routines to maintain evidence, update decisions and avoid drift over time. |

## 2. Detailed requirement mapping

### 2.1 Scope, duty and responsibility

The WAD guide begins with who is covered, what counts as public service delivery and why. The equivalent operational model in Double FW is the organisational-change and governance approach in Accessibility Champions.

Relevant repo: [Accessibility-Champions](https://github.com/Double-FW/Accessibility-Champions)

Key alignment:

- the repository treats accessibility as a shared organisational responsibility rather than a specialist-only issue
- role clarity is mapped to sponsorship, championing, and operational ownership
- the model supports business integration, not only technical remediation

This aligns directly with the WAD requirement that public bodies remain responsible even when a function is outsourced or delivered through suppliers.

### 2.2 Outcome-led accessibility requirements

The legal requirement is expressed as four principles: perceivable, operable, understandable and robust. The leading operational translation in Double FW is the QA Accessibility Testing set.

Relevant repos and files:

- [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md)
- [Canonical Test Library.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Canonical%20Test%20Library.md)
- [Mobile_Application_and_Website_Test_Library.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Mobile_Application_and_Website_Test_Library.md)
- [Accessibility_Test_Led_Delivery_Framework.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Accessibility_Test_Led_Delivery_Framework.md)

Key alignment:

- The QA repo separates conformance evidence from usability and quality evidence.
- It emphasises layered testing across component, journey, assistive-technology and user-outcome levels.
- It avoids equating a single automated score with proof of accessibility.

This is a close operational match to the WAD guide's repeated point that a technical score alone does not prove a public service works accessibly.

### 2.3 Testing as a managed function rather than an audit event

The WAD guide proposes a repeatable testing and evidence process. The Double FW QA repos translate this into a managed lifecycle.

Relevant repo and files:

- [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md)
- [Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA/blob/main/Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md)

Key alignment:

- testing starts before implementation is complete and continues through delivery and regression management
- evidence is required for findings, retests and exceptions
- automated scans are treated as only one layer, not the whole assurance model
- keyboard and focus checks remain a separate and material validation stream

This matches the WAD guide's insistence that assessment must connect the legal requirement, the implementation, and a person's ability to use the service.

### 2.4 Keyboard and focus as the baseline of operability

A fundamental part of WAD operability is the ability to use the service without a mouse, with meaningful focus order, visible focus and no traps. The phased QA repo operationalizes this as a practical baseline.

Relevant repo and file:

- [Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md](https://github.com/Double-FW/Phased-Approach-to-integrating-Accessibility-into-QA/blob/main/Accessibility_QA_Axe_Core_Keyboard_Test_Plan.md)

Key alignment:

- axe-core is used as an early automated signal
- keyboard-only testing verifies actual operability
- focus tests cover logical order, visible focus, exit paths and dynamic updates
- the phase-based model is intentionally foundational: it creates a repeatable starting point before broader accessibility assurance

This is an operationally strong match to the WAD focus on keyboard access and focus as core public service usability requirements.

### 2.5 Accessible documents, media and information architecture

The WAD guide explicitly includes downloadable documents, media and public information as covered content. Double FW has a dedicated document framework for this.

Relevant repo and file:

- [Accessible_documentation_design.md](https://github.com/Double-FW/Accessible_Digital_and_Printed_Documents/blob/main/Accessible_documentation_design.md)

Key alignment:

- document structure is treated as a primary requirement before styling
- the repository covers heading hierarchy, reading order, tables, forms, PDFs, EPUBs and print outputs
- verification is evidence-based, not visually subjective

This closely fits the Directive's concern with usable information and documents as part of an accessible public service.

### 2.6 Complex visual information and alternative presentations

The WAD guide refers to charts, maps, images and equivalent information requirements. Double FW has a strong repo for this area.

Relevant repo and file:

- [Inclusive_Design_Charts_Maps_and_Complex_Graphics.md](https://github.com/Double-FW/Accessible_Charts_Graphs_and_Maps/blob/main/Inclusive_Design_Charts_Maps_and_Complex_Graphics.md)

Key alignment:

- design starts with the user's question and essential task
- alternative presentation and equivalent meaning is preserved
- maps and charts are tested through task completion and not only by technical inspection
- visual content is paired with structured, accessible and synchronised alternatives

This operational model strongly complements the WAD requirement to ensure that information remains perceivable and understandable when rendered in different formats.

### 2.7 Governance, evidence and sustainable delivery

The WAD guide requires organisations to maintain evidence, public statements and ongoing monitoring. The Double FW operating model and governance guidance translate this into a practice of coordinated change and traceability.

Relevant repos and files:

- [Synchronistic_Design_Formal_Operating_Model_v0.1.md](https://github.com/Double-FW/Synchronistic-Design-Formal-Operating-Model/blob/main/Synchronistic_Design_Formal_Operating_Model_v0.1.md)
- [Accessibility-Champions-Network-Guidance.md](https://github.com/Double-FW/Accessibility-Champions/blob/main/Accessibility-Champions-Network-Guidance.md)
- [Testing_Approach.md](https://github.com/Double-FW/QA_Accessibility_Testing/blob/main/Testing_Approach.md)

Key alignment:

- the operating model emphasises intent, context, traceable reasoning and feedback loops
- accessibility maturity is treated as an organisational system, not a one-off audit
- quality evidence is connected to decisions, responsibility and ongoing cycles of improvement

This is a strong organisational analogue to the WAD requirement for continued review, update and proof of accessibility over time.

## 3. Practical mapping by requirement category

### 3.1 Legal requirement → operational approach

| Requirement class | Double FW translation |
| --- | --- |
| public body accountability | Accessibility champions network and governance model |
| user needs and disability inclusion | inclusive design guidance for documents and complex graphics |
| outcome definition | canonical tests and mobile/web test library |
| repeatable testing | QA test-led delivery framework |
| keyboard and operability | phased axe + keyboard/focus plan |
| document and media accessibility | accessible digital and printed documents guide |
| complex data display accessibility | charts, graphs and maps guide |
| evidence and release decisions | layered evidence model and testing approach |
| sustainable change | synchronistic design operating model |

### 3.2 WAD sections to repo methods

| WAD section in this repository | Closest Double FW method |
| --- | --- |
| 1. Purpose and intended outcomes | QA testing approach and delivery framework |
| 2. Which people it supports | accessible charts/maps and document design guidance |
| 3. Which organisations have duties | accessibility champions governance model |
| 4. Which websites, apps and content are covered | mobile application and website test library |
| 8. The four required accessibility outcomes | canonical test library and QA test lifecycle |
| 10. What to assess and how to measure it | mobile/web accessibility test library |
| 11. A repeatable testing and evidence process | testing approach and phased QA plan |
| 12. Additional checks for mobile apps | mobile application and website test library |
| 13. Accessibility statements | governance and organisational responsibility models |
| 17. Keeping accessibility working over time | synchronistic design operating model |

## 4. Integration recommendations

For a public-sector website or app aligned to this WAD repository, the practical Double FW combination is:

1. Start with the organisational ownership model in Accessibility Champions.
2. Define the scope and service boundary using the WAD guide and public sector responsibility logic.
3. Translate the four principles into testable user outcomes via the QA repository.
4. Use the phased keyboard/focus approach as the minimum baseline for product quality.
5. Validate document, content and service information structures using the accessible document guidance.
6. Apply chart, map and complex-graphics accessibility guidance where the experience depends on visual evidence.
7. Keep evidence and service decisions linked through a traceable operating model.

## 5. Summary conclusion

The Double FW repository ecosystem contains a coherent translation layer for the WAD/EN 301 549 requirements in this repository:

- the legal and policy logic is defined in the WAD guide itself
- testing governance and evidence are defined in the QA Accessibility Testing repo
- phased execution is defined in the QA phase 1 plan
- user-centered document and visual-information methods are defined in the document and charts/maps repos
- organisational ownership and ongoing operating-model alignment are defined in the champions and synchronistic-design repos

Taken together, these repositories provide a practical, evidence-based implementation model for the Directive's public-service accessibility obligations without replacing the legal interpretation in this repository.

## 6. Status

This mapping is a cross-repository operational translation, intended for internal use and programme planning. It is not a substitute for legal interpretation, regulator guidance, or formal conformance decisions.

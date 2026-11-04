# EN 301 549 / WAD requirements-to-tests matrix

Version 1.0 · Double FW Ltd · 4 November 2026

Companion: [EN301549_AI_Test_Prompts.md](EN301549_AI_Test_Prompts.md). Save both Markdown files in the same EN301549 directory so their relative links work.

## Source snapshots and authority

Prepared for Double FW Ltd on 4 November 2026. This is a test-design mapping; no product tests have been executed.

| Source | Snapshot | Use |
| --- | --- | --- |
| [WAD guide](https://github.com/Double-FW/EU-Web-Accessibility-Directive_EN301549/blob/589c96c6fac60bae073a5234dfd72b0ba568e972/WAD_Plain_English_Breakdown_and_Evidence_Guide.md) | 589c96c6fac60bae073a5234dfd72b0ba568e972 | User groups, WAD scope/duties, outcomes, assessment areas and evidence |
| [WAD cross-repository mapping](https://github.com/Double-FW/EU-Web-Accessibility-Directive_EN301549/blob/589c96c6fac60bae073a5234dfd72b0ba568e972/WAD_Requirements_to_Double_FW_Approaches_Mapping.md) | Same WAD snapshot | Links between the guide and QA methods |
| [WAD agent instructions](https://github.com/Double-FW/EU-Web-Accessibility-Directive_EN301549/blob/589c96c6fac60bae073a5234dfd72b0ba568e972/AGENTS.md) | Same WAD snapshot | Applicability, evidence and decision boundaries |
| [Canonical Test Library](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Canonical%20Test%20Library.md) | c0450cdcb89484248ca4a15355ea5d71a58af043 | Stable CTL-001–CTL-200 identities, requirements and supported behaviour |
| [Canonical relationship register](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Canonical_WCAG_AA_Relationship_Register.md) | Same QA snapshot | Direct, partial and technique relationships; policy relationships excluded from automatic technical equivalence |
| [AXE alignment](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/AXE_and%20_Test_Inventory_Alignment.md) and [rule descriptions](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/AXE_Test_AA_Rule_Descriptions.md) | Same QA snapshot | Named candidate axe rules and manual complements |
| [ACT-style tests](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Accessibility_ACT-Style_Test_System.md) | Same QA snapshot | Pattern and practice execution examples |
| [Mobile/web library](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Mobile_Application_and_Website_Test_Library.md) | Same QA snapshot | Cross-platform behavioural support; numbered items are not CTL identities |
| [QA management approach](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/Testing_Approach.md) and [QA agent playbook](https://github.com/Double-FW/QA_Accessibility_Testing/blob/c0450cdcb89484248ca4a15355ea5d71a58af043/AGENTS.md) | Same QA snapshot | QA-MGMT and QA-AGENT references used below |

The superseded *Canonical Test Library Alignment to Exact WCAG SC IDs.md* is deliberately not used. The cross-reference covering IBM, Alfa, QualWeb and AccessLint is not evidence of axe capability.

The guide records EN 301 549 V3.2.1 as its harmonised baseline. This mapping preserves that repository baseline; it does not independently establish which reference is currently cited in the Official Journal or what additional national duties apply. Confirm those before a legal conclusion. Newer WCAG 2.2 requirements and broader CTL practices remain separate.

This document maps the requirements and outcomes **outlined by the repository**. It includes 50 WCAG 2.1 A/AA web tests, of which live captions (WEB-124) is explicitly an additional baseline test: WAD excludes live media and Annex A omits the live-caption clauses. Document, native-software and additional EN requirements are represented at the guide's stated level of detail, with explicit supplemental tests. It is **not an exhaustive transcription of every Annex A subclause**. Before a formal assessment, GOV-02 requires a clause-level applicability register from the selected standard's Table A.1 or A.2. A category-level pass cannot close its unlisted subclauses. Additional EN requirements include unconditional entries as well as function-dependent ones; follow each table's actual conditions.

The [full standard linked by the guide](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) provides the exact conditions. Conditional tests below require the selected clause and thresholds as inputs; they do not invent universal technical limits.

## User groups and required outcomes

| Code | Repository user group / functional need | Test context |
| --- | --- | --- |
| NV | Blind users / use without vision | Screen readers, braille and non-visual routes |
| LV | Limited vision | Magnification, enlarged text, contrast and display preferences |
| CP | Difficulty distinguishing colours | Meaning through text, shape and other cues |
| DH | Deaf users / use without hearing | Captions, text and visual communication |
| LH | Limited hearing | Clear audio, captions and relevant hearing support |
| NS | Speech impairments / no speech | Non-speech identification, support and communication |
| MS | Limited movement, dexterity, manipulation or strength | Keyboard, switch, voice, touch alternatives and reduced precision |
| MR | Limited reach | Accessible input and controls without excessive reach or motion |
| CL | Learning disability or cognitive, language, reading or memory needs | Comprehensible content, predictable operation and recovery; includes relevant dyslexic/neurodivergent needs |
| MH | Mental health impairments interacting with barriers | Predictability, control, recoverability and reduced avoidable stress |
| PS | Avoiding photosensitive seizure triggers | Safe flash analysis without exposing users |
| ALL | All relevant groups and combined needs | Select relevant functional needs for each task; no single participant represents a group |

Codes identify likely affected needs, not an exclusive eligibility list. Include intersecting needs, older users and temporary/situational limitations in task selection. Do not require diagnosis disclosure. Speech users and users without speech may need different routes within the same motor-access task.

| Article 4 outcome | Tests providing evidence |
| --- | --- |
| Perceivable | WEB-1…; DOC-01–03/05; relevant media, communication and mobile tests |
| Operable | WEB-2…; DOC-04; APP-02–04; activation and media-control tests |
| Understandable | WEB-3…; labels, instructions, identification, recovery, documentation and support tests |
| Robust | WEB-4…; DOC-02/04; APP-01/02/05; platform interoperability and dynamic-state tests |

The four outcomes are many-to-many: a form's names, instructions, errors, focus and submission result must work together. GOV-05 evaluates real task outcomes and does not replace technical tests.

## Classification and use

| Classification | Meaning |
| --- | --- |
| AXE: partial + named rule IDs | Automatable rule-level observations on browser-rendered content. Only the listed subset is assigned; an empty finding set is not a requirement pass. |
| AXE: no coverage assigned | This mapping assigns no reliable axe coverage for the test. Other specialist tools may still automate measurements. |
| AI execution (E) | An agent with the stated browser, device, analyser or file tools can execute the specified observable subset. Complete results remain subject to the manual complement. |
| AI-assisted (A) | An agent can inventory, compare, extract evidence or flag candidates. Semantic adequacy, legal judgement and service effectiveness remain human decisions. |
| Manual only (N) | The stated outcome depends on direct human/participant evidence; no AI substitute is assigned. |
| Manual complement | Required human technical, AT, editorial, specialist or user review for the full mapped requirement. |

These methods are complementary, not mutually exclusive. “AI execution” does not mean an LLM can infer accessibility from source code or a screenshot. Without the required tools and fixtures, record blocked/not_tested. AI-assisted work must not produce a final semantic or legal pass.

At execution time record axe-core version, enabled rules, tags, options, exclusions and browser. Check each named rule is available and enabled using the installed engine's rule metadata. Unsupported or disabled rules are tool/coverage gaps, not passes. Use relevant WCAG 2.0/2.1 A/AA tags for the declared baseline, including older criteria absent from WCAG 2.2. Keep best-practice rules and WCAG 2.2 additions in separately labelled results. Scan all selected reachable states, frames and supported shadow content, and document limits.

All WEB-* records below are **web** tests. An embedded webview may use them for its web content; native UI and downloaded files need their own applicable clauses, tools and fixtures. Axe-core does not assess an entire native app, PDF/Word document, call system or support process.

CTL references preserve existing QA identities and supply supporting evidence. They are not declarations of full criterion equivalence. Gaps receive new test IDs in this document; these IDs do not already exist in the QA repository. QA-MGMT/QA-AGENT refer to the named source methods above, not existing atomic tests.

## Execution record and decision rules

For every test store: requirement/test ID, exact technical clause and version, applicability reason, asset/build/hash, task and interface state, relevant groups, expected result, actual steps/result, tool/browser/OS/device/AT versions, settings, evidence, limits, owner, defect/retest references and reviewer.

Use pass, fail, blocked, cannot_tell, not_tested, not_applicable or tool_error for **test observations**. A pass describes only the observed subcondition and scope. Keep requirement-level met / not met / not assessed / not applicable separately; full met requires all applicable conditions and manual complements. Record legal exclusion and burden separately from technical outcomes. Do not calculate a single compliance percentage from this matrix.

Use test accounts and reversible fixtures. Do not send feedback/support messages, submit complaints, make purchases, publish statements or perform other consequential actions without the relevant explicit authorisation. The prompts use sandbox or supplied records by default.

## Matrix

Each row has a unique test ID, procedure and expected outcome, existing QA references, and separate manual/axe/AI classifications. Expanded procedures appear in the test specifications after the tables.
### Web technical requirements

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [WEB-111](#web-111) — Non-text content | Guide §§8–10; EN 9.1.1.1; WCAG 2.1 1.1.1 | NV LV CP CL | Equivalent information or function is available in text; decorative content does not add irrelevant announcements | CTL-007, CTL-033, CTL-034, CTL-035, CTL-036, CTL-038, CTL-039, CTL-040, CTL-187, CTL-195 | Partial: image-alt, input-image-alt, area-alt, object-alt | A — [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111) | Content reviewer confirms meaning, chart information and decorative decisions; screen reader checks output |
| [WEB-121](#web-121) — Audio-only and video-only prerecorded | Guide §§8–10; EN 9.1.2.1; WCAG 2.1 1.2.1 | NV DH LH CL | Applicable audio-only information has equivalent text; silent video has equivalent text or audio | CTL-181 | No coverage assigned | A — [AI-WEB-121](EN301549_AI_Test_Prompts.md#ai-web-121) | Review full asset and alternative for equivalence and applicable exceptions |
| [WEB-122](#web-122) — Captions prerecorded | Guide §§8–10; EN 9.1.2.2; WCAG 2.1 1.2.2 | DH LH CL | Required captions convey speech and meaningful audio information in synchronisation | CTL-183 | Partial: video-caption | A — [AI-WEB-122](EN301549_AI_Test_Prompts.md#ai-web-122) | Human checks full-asset accuracy, speaker identification, sounds and synchronisation |
| [WEB-123](#web-123) — Audio description or media alternative prerecorded | Guide §§8–10; EN 9.1.2.3; WCAG 2.1 1.2.3 | NV LV CL | Applicable prerecorded video has description or a full time-based media alternative under this criterion | CTL-184 | No coverage assigned | A — [AI-WEB-123](EN301549_AI_Test_Prompts.md#ai-web-123) | Editorial equivalence and exception review; dialogue transcript alone is insufficient |
| [WEB-124](#web-124) — Captions live | Guide §5.6 and §10.7; EN 9.1.2.4 / WCAG 2.1 1.2.4; additional baseline only, absent from WAD Annex A | DH LH | In-scope live audiovisual content has required live captions; WAD live-media exclusion is decided separately | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | A — [AI-WEB-124](EN301549_AI_Test_Prompts.md#ai-web-124) | WAD excludes live time-based media and Annex A omits live-caption clauses. Reviewer confirms any separately adopted requirement and checks actual captions. |
| [WEB-125](#web-125) — Audio description prerecorded | Guide §§8–10; EN 9.1.2.5; WCAG 2.1 1.2.5 | NV LV | Required description conveys essential visual information; transcript alone does not satisfy this criterion | CTL-184 | No coverage assigned | A — [AI-WEB-125](EN301549_AI_Test_Prompts.md#ai-web-125) | Human editorial and playback review; consider whether existing audio conveys required visuals |
| [WEB-131](#web-131) — Information and relationships | Guide §§8–10; EN 9.1.3.1; WCAG 2.1 1.3.1 | NV LV CL | Structure and relationships are programmatically determinable or available in text | CTL-054, CTL-056, CTL-058, CTL-063, CTL-066, CTL-069, CTL-080, CTL-088, CTL-113, CTL-119, CTL-120, CTL-121, CTL-143, CTL-163, CTL-169, CTL-176, CTL-191, CTL-196 | Partial: definition-list, aria-required-children, aria-required-parent | E — [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Screen reader navigation and content review; a single H1 or table caption is not universally mandatory |
| [WEB-132](#web-132) — Meaningful sequence | Guide §§8–10; EN 9.1.3.2; WCAG 2.1 1.3.2 | NV LV CL | A correct reading sequence is available where order affects meaning | CTL-060, CTL-062, CTL-189 | No coverage assigned | E — [AI-WEB-132](EN301549_AI_Test_Prompts.md#ai-web-132) | Human narrative and task-order review with screen reader |
| [WEB-133](#web-133) — Sensory characteristics | Guide §§8–10; EN 9.1.3.3; WCAG 2.1 1.3.3 | NV LV DH CP CL | Instructions do not rely solely on sensory characteristics | CTL-040, CTL-152 | No coverage assigned | A — [AI-WEB-133](EN301549_AI_Test_Prompts.md#ai-web-133) | Human tests instructions with relevant access methods |
| [WEB-134](#web-134) — Orientation | Guide §§8–10; EN 9.1.3.4; WCAG 2.1 1.3.4 | LV MS MR | No single-orientation restriction unless essential | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-134](EN301549_AI_Test_Prompts.md#ai-web-134) | Physical-device verification and exception review |
| [WEB-135](#web-135) — Identify input purpose | Guide §§8–10; EN 9.1.3.5; WCAG 2.1 1.3.5 | NV CL MS | Covered personal-data input purposes are programmatically identifiable | CTL-118 | No coverage assigned | E — [AI-WEB-135](EN301549_AI_Test_Prompts.md#ai-web-135) | Confirm actual purpose and autofill or AT behaviour |
| [WEB-141](#web-141) — Use of colour | Guide §§8–10; EN 9.1.4.1; WCAG 2.1 1.4.1 | CP LV NV CL | Colour is not the sole visual means of conveying information or distinction | CTL-001, CTL-002, CTL-003, CTL-004, CTL-005, CTL-006, CTL-007 | No coverage assigned | E — [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141) | Human visual and semantic review; simulation does not reproduce individual vision |
| [WEB-142](#web-142) — Audio control | Guide §§8–10; EN 9.1.4.2; WCAG 2.1 1.4.2 | NV LH CL MH | Automatic audio longer than three seconds has an applicable pause, stop or independent volume mechanism | CTL-028, CTL-030, CTL-182 | Partial: no-autoplay-audio | E — [AI-WEB-142](EN301549_AI_Test_Prompts.md#ai-web-142) | Listen to output and verify usability alongside screen reader audio |
| [WEB-143](#web-143) — Contrast minimum | Guide §§8–10; EN 9.1.4.3; WCAG 2.1 1.4.3 | LV CP | Ordinary text reaches 4.5:1 and qualifying large text 3:1 subject to exceptions | CTL-008, CTL-009, CTL-012 | Partial: color-contrast | E — [AI-WEB-143](EN301549_AI_Test_Prompts.md#ai-web-143) | Measure image text, gradients and overlays manually; inactive controls may be exempt |
| [WEB-144](#web-144) — Resize text | Guide §§8–10; EN 9.1.4.4; WCAG 2.1 1.4.4 | LV CL | Text resizes to 200 percent without loss under applicable conditions | CTL-014, CTL-015, CTL-017, CTL-018, CTL-020 | No coverage assigned | E — [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144) | Confirm text-resize and full-task behaviour; viewport reduction alone is insufficient |
| [WEB-145](#web-145) — Images of text | Guide §§8–10; EN 9.1.4.5; WCAG 2.1 1.4.5 | LV CL | Text replaces images of text where required | CTL-037 | No coverage assigned | A — [AI-WEB-145](EN301549_AI_Test_Prompts.md#ai-web-145) | Reviewer determines essential and customisable exceptions |
| [WEB-1410](#web-1410) — Reflow | Guide §§8–10; EN 9.1.4.10; WCAG 2.1 1.4.10 | LV MS CL | No loss and no two-dimensional scrolling except content requiring that layout | CTL-015, CTL-016, CTL-017, CTL-018, CTL-020, CTL-069, CTL-175 | No coverage assigned | E — [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Manual magnification review and verification of two-dimensional-content exceptions |
| [WEB-1411](#web-1411) — Non-text contrast | Guide §§8–10; EN 9.1.4.11; WCAG 2.1 1.4.11 | LV CP | Required component, state and graphical information reaches 3:1 under applicable conditions | CTL-011 | No coverage assigned | E — [AI-WEB-1411](EN301549_AI_Test_Prompts.md#ai-web-1411) | Human identifies essential visual parts; text contrast scans do not cover this test |
| [WEB-1412](#web-1412) — Text spacing | Guide §§8–10; EN 9.1.4.12; WCAG 2.1 1.4.12 | LV CL | No content or functionality loss under applicable spacing overrides | CTL-019 | No coverage assigned | E — [AI-WEB-1412](EN301549_AI_Test_Prompts.md#ai-web-1412) | Visual and reading-tool inspection; apply language/script exceptions |
| [WEB-1413](#web-1413) — Content on hover or focus | Guide §§8–10; EN 9.1.4.13; WCAG 2.1 1.4.13 | LV MS CL | Applicable added content is dismissible, hoverable and persistent | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-1413](EN301549_AI_Test_Prompts.md#ai-web-1413) | Human checks hover transit, magnification and exceptions |
| [WEB-211](#web-211) — Keyboard | Guide §§8–10; EN 9.2.1.1; WCAG 2.1 2.1.1 | NV MS MR CL | Applicable functionality operates through a keyboard interface subject to exceptions | CTL-070, CTL-091, CTL-092, CTL-093, CTL-107, CTL-133, CTL-174, CTL-178, CTL-181 | No coverage assigned | E — [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211) | Manual keyboard and alternative-input journeys; direct script activation is not keyboard proof |
| [WEB-212](#web-212) — No keyboard trap | Guide §§8–10; EN 9.2.1.2; WCAG 2.1 2.1.2 | NV MS MR | Focus can leave components with keyboard alone, with instructions for non-standard exits where required | CTL-094, CTL-173, CTL-174, CTL-178 | No coverage assigned | E — [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212) | Manual keyboard and relevant AT verification |
| [WEB-214](#web-214) — Character key shortcuts | Guide §§8–10; EN 9.2.1.4; WCAG 2.1 2.1.4 | NV MS CL | Applicable character shortcuts can be disabled, remapped or restricted to component focus | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-214](EN301549_AI_Test_Prompts.md#ai-web-214) | Voice-input and screen reader interference review |
| [WEB-221](#web-221) — Timing adjustable | Guide §§8–10; EN 9.2.2.1; WCAG 2.1 2.2.1 | NV LV MS CL MH | Applicable limits meet criterion conditions for turning off, adjusting or extending, subject to exceptions | CTL-160, CTL-197, CTL-198 | Partial: meta-refresh | E — [AI-WEB-221](EN301549_AI_Test_Prompts.md#ai-web-221) | Human confirms exceptions and actual recovery; no universal task completion time |
| [WEB-222](#web-222) — Pause stop hide | Guide §§8–10; EN 9.2.2.2; WCAG 2.1 2.2.2 | LV NV CL MH | Applicable movement and updates provide required user controls | CTL-023, CTL-024, CTL-028, CTL-029, CTL-182 | Partial: blink | E — [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Human reviews user control and essential exceptions |
| [WEB-231](#web-231) — Three flashes or below threshold | Guide §§8–10; EN 9.2.3.1; WCAG 2.1 2.3.1 | PS | Content satisfies applicable frequency or flash-area/luminance conditions | CTL-026 | No coverage assigned | E — [AI-WEB-231](EN301549_AI_Test_Prompts.md#ai-web-231) | Specialist reviews analyser output; never expose participants to suspected hazardous flashing |
| [WEB-241](#web-241) — Bypass blocks | Guide §§8–10; EN 9.2.4.1; WCAG 2.1 2.4.1 | NV MS CL | A working mechanism bypasses repeated blocks | CTL-052, CTL-053 | Partial: bypass | E — [AI-WEB-241](EN301549_AI_Test_Prompts.md#ai-web-241) | Keyboard and screen reader checks; a skip link is one permissible technique |
| [WEB-242](#web-242) — Page titled | Guide §§8–10; EN 9.2.4.2; WCAG 2.1 2.4.2 | NV LV CL | Titles describe topic or purpose of assessed pages | CTL-044, CTL-045, CTL-047 | Partial: document-title | E — [AI-WEB-242](EN301549_AI_Test_Prompts.md#ai-web-242) | Human checks useful differentiation and SPA context |
| [WEB-243](#web-243) — Focus order | Guide §§8–10; EN 9.2.4.3; WCAG 2.1 2.4.3 | NV LV MS CL | Sequential focus preserves meaning and operability | CTL-053, CTL-061, CTL-062, CTL-070, CTL-097, CTL-098, CTL-164, CTL-173, CTL-189 | No coverage assigned | E — [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Human checks logical transitions and orientation; positive tabindex alone is not failure proof |
| [WEB-244](#web-244) — Link purpose in context | Guide §§8–10; EN 9.2.4.4; WCAG 2.1 2.4.4 | NV CL | Link purpose follows from text alone or permitted programmatically determined context | CTL-136, CTL-137, CTL-140, CTL-147 | Partial: link-name, area-alt | A — [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244) | Human context review; stronger out-of-context CTL rules are not automatically mandatory |
| [WEB-245](#web-245) — Multiple ways | Guide §§8–10; EN 9.2.4.5; WCAG 2.1 2.4.5 | NV LV CL | More than one way locates pages within a set except applicable exceptions | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-245](EN301549_AI_Test_Prompts.md#ai-web-245) | Reviewer establishes set boundaries and usable discovery |
| [WEB-246](#web-246) — Headings and labels | Guide §§8–10; EN 9.2.4.6; WCAG 2.1 2.4.6 | NV LV CL | Headings and labels describe topic or purpose | CTL-054, CTL-057, CTL-081 | No coverage assigned | A — [AI-WEB-246](EN301549_AI_Test_Prompts.md#ai-web-246) | Human content and AT navigation review |
| [WEB-247](#web-247) — Focus visible | Guide §§8–10; EN 9.2.4.7; WCAG 2.1 2.4.7 | LV MS MR | Keyboard focus is visible | CTL-005, CTL-095, CTL-096, CTL-103 | No coverage assigned | E — [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247) | Human visual checks; do not import newer enhanced focus geometry into this baseline |
| [WEB-251](#web-251) — Pointer gestures | Guide §§8–10; EN 9.2.5.1; WCAG 2.1 2.5.1 | MS MR | Applicable gestures have single-pointer alternatives without a path | CTL-108, CTL-109 | No coverage assigned | E — [AI-WEB-251](EN301549_AI_Test_Prompts.md#ai-web-251) | Physical-device and alternative-input review; keep additional WCAG 2.2 dragging requirements separate |
| [WEB-252](#web-252) — Pointer cancellation | Guide §§8–10; EN 9.2.5.2; WCAG 2.1 2.5.2 | MS MR CL | Functions meet applicable cancellation or reversal conditions unless essential | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-252](EN301549_AI_Test_Prompts.md#ai-web-252) | Human touch-behaviour and exception review |
| [WEB-253](#web-253) — Label in name | Guide §§8–10; EN 9.2.5.3; WCAG 2.1 2.5.3 | MS CL NV | Textual visible labels are contained in accessible names where required | CTL-073 | No coverage assigned | E — [AI-WEB-253](EN301549_AI_Test_Prompts.md#ai-web-253) | Human verifies visual text and voice invocation; missing-name scans are insufficient |
| [WEB-254](#web-254) — Motion actuation | Guide §§8–10; EN 9.2.5.4; WCAG 2.1 2.5.4 | MS MR | Applicable motion functions have UI alternatives and disable controls subject to exceptions | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-254](EN301549_AI_Test_Prompts.md#ai-web-254) | Physical-device and exception verification |
| [WEB-311](#web-311) — Language of page | Guide §§8–10; EN 9.3.1.1; WCAG 2.1 3.1.1 | NV CL | Default human language is programmatically determinable | CTL-041 | Partial: html-has-lang, html-lang-valid | A — [AI-WEB-311](EN301549_AI_Test_Prompts.md#ai-web-311) | Human language and pronunciation review |
| [WEB-312](#web-312) — Language of parts | Guide §§8–10; EN 9.3.1.2; WCAG 2.1 3.1.2 | NV CL | Language changes are programmatically determinable where required | CTL-042 | Partial: valid-lang | A — [AI-WEB-312](EN301549_AI_Test_Prompts.md#ai-web-312) | Human language and screen reader pronunciation review |
| [WEB-321](#web-321) — On focus | Guide §§8–10; EN 9.3.2.1; WCAG 2.1 3.2.1 | NV MS CL MH | Receiving focus does not itself initiate context change | CTL-099, CTL-156, CTL-200 | No coverage assigned | E — [AI-WEB-321](EN301549_AI_Test_Prompts.md#ai-web-321) | Human and AT review; legitimate in-context help is not automatically a failure |
| [WEB-322](#web-322) — On input | Guide §§8–10; EN 9.3.2.2; WCAG 2.1 3.2.2 | NV MS CL MH | Changing settings does not unexpectedly change context without required prior advice | CTL-099, CTL-112, CTL-156, CTL-200 | No coverage assigned | E — [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322) | Human warning and predictability review |
| [WEB-323](#web-323) — Consistent navigation | Guide §§8–10; EN 9.3.2.3; WCAG 2.1 3.2.3 | NV CL MH | Repeated navigation has consistent relative order unless user changes apply | CTL-047 | No coverage assigned | E — [AI-WEB-323](EN301549_AI_Test_Prompts.md#ai-web-323) | Human page-set and navigation review |
| [WEB-324](#web-324) — Consistent identification | Guide §§8–10; EN 9.3.2.4; WCAG 2.1 3.2.4 | NV CL MH | Same-function components are identified consistently | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-324](EN301549_AI_Test_Prompts.md#ai-web-324) | Human functional-equivalence and context review |
| [WEB-331](#web-331) — Error identification | Guide §§8–10; EN 9.3.3.1; WCAG 2.1 3.3.1 | NV LV CP CL MH | Automatically detected errors identify the item and describe the error in text | CTL-002, CTL-079, CTL-122, CTL-123, CTL-124, CTL-125 | No coverage assigned | E — [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331) | Screen reader and content review |
| [WEB-332](#web-332) — Labels or instructions | Guide §§8–10; EN 9.3.3.2; WCAG 2.1 3.3.2 | NV LV CL | Required input has labels or instructions | CTL-003, CTL-072, CTL-078, CTL-080, CTL-113, CTL-114, CTL-116, CTL-119, CTL-120, CTL-121, CTL-134, CTL-194 | Partial: label | E — [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Human verifies visible/spoken clarity and sufficient guidance |
| [WEB-333](#web-333) — Error suggestion | Guide §§8–10; EN 9.3.3.3; WCAG 2.1 3.3.3 | NV CL MH | Known corrections are suggested unless a relevant exception applies | CTL-126, CTL-134 | No coverage assigned | A — [AI-WEB-333](EN301549_AI_Test_Prompts.md#ai-web-333) | Human wording, security and purpose-exception review |
| [WEB-334](#web-334) — Error prevention legal financial data | Guide §§8–10; EN 9.3.3.4; WCAG 2.1 3.3.4 | NV LV MS CL MH | Applicable submissions are reversible, checked or confirmed as permitted | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-334](EN301549_AI_Test_Prompts.md#ai-web-334) | Human confirms scope and safeguards |
| [WEB-411](#web-411) — Parsing retained in WCAG 2.1 baseline | Guide §§8–10; EN 9.4.1.1; WCAG 2.1 4.1.1 | NV | WCAG 2.1 parsing conditions are assessed independently of the WCAG 2.2 register | GAP: no direct active CTL mapping; supplemental test | No coverage assigned | E — [AI-WEB-411](EN301549_AI_Test_Prompts.md#ai-web-411) | Human reviews parser output; this removed WCAG 2.2 criterion has no current CTL standards mapping |
| [WEB-412](#web-412) — Name role value | Guide §§8–10; EN 9.4.1.2; WCAG 2.1 4.1.2 | NV MS CL | Components expose appropriate names, roles, states and values and make changes available | CTL-035, CTL-071, CTL-081, CTL-082, CTL-147, CTL-157, CTL-161, CTL-163, CTL-167, CTL-169, CTL-172, CTL-176, CTL-177, CTL-190, CTL-193, CTL-196 | Partial: aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, input-button-name, label, frame-title | E — [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Actual screen reader and alternative-input verification; ARIA syntax alone is insufficient |
| [WEB-413](#web-413) — Status messages | Guide §§8–10; EN 9.4.1.3; WCAG 2.1 4.1.3 | NV LV CL | Applicable status messages are programmatically determinable without focus transfer | CTL-123, CTL-146, CTL-150, CTL-151, CTL-152, CTL-158, CTL-160, CTL-192 | No coverage assigned | E — [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Screen reader timing and verbosity review; live-region markup alone is not spoken-output proof |

### Documents

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [DOC-01](#doc-01) — Document alternatives and language | Guide §10.8; applicable Clause 10 | NV LV CL | Covered documents preserve equivalent text and language information | CTL-033, CTL-034, CTL-035, CTL-036, CTL-041, CTL-042 | No coverage assigned | A — [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Document specialist verifies actual alternatives and language with relevant AT |
| [DOC-02](#doc-02) — Document structure and reading order | Guide §10.8; applicable Clause 10 | NV LV CL | Document structure, relationships and sequence preserve meaning | CTL-054, CTL-060, CTL-063, CTL-066, CTL-067 | No coverage assigned | A — [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02) | Format-aware manual and screen reader review; extracted text alone is insufficient |
| [DOC-03](#doc-03) — Document presentation and enlargement | Guide §10.8; applicable Clause 10 | LV CP CL | Covered documents remain perceivable under their applicable format-specific requirements | CTL-008, CTL-009, CTL-014, CTL-017, CTL-019 | No coverage assigned | E — [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03) | Do not impose browser CSS measurements on native readers without checking the relevant Clause 10 condition |
| [DOC-04](#doc-04) — Document links forms and errors | Guide §10.8; applicable Clause 10 | NV MS CL | Document interactions, labels, errors and recovery are usable under applicable conditions | CTL-071, CTL-072, CTL-079, CTL-091, CTL-092, CTL-122 | No coverage assigned | E — [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04) | Document form and AT testing in actual readers; no real external submission |
| [DOC-05](#doc-05) — Document media and conversions | Guide §10.8; applicable Clause 10 | NV DH LH CL | Applicable embedded alternatives and accessibility information survive the document workflow | CTL-183, CTL-184 | No coverage assigned | A — [AI-DOC-05](EN301549_AI_Test_Prompts.md#ai-doc-05) | Human media and format-conversion review; original accessible source does not establish output accessibility |

### Native and hybrid mobile apps

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [APP-01](#app-01) — Native platform accessibility exposure | Guide §12; applicable Clause 11 and Table A.2 | NV MS CL | Native controls expose required information and operations through platform services | CTL-071, CTL-157, CTL-161 | No coverage assigned | E — [AI-APP-01](EN301549_AI_Test_Prompts.md#ai-app-01) | Actual TalkBack/VoiceOver and relevant input testing; a browser axe scan does not cover native widgets |
| [APP-02](#app-02) — Native reading focus and screen changes | Guide §12; applicable Clause 11 and Table A.2 | NV LV MS CL | Order, announcements and focus preserve orientation and complete-task operation | CTL-060, CTL-061, CTL-100, CTL-101, CTL-148, CTL-151 | No coverage assigned | E — [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Each supported OS and AT combination requires appropriate direct verification |
| [APP-03](#app-03) — Native text settings orientation and input | Guide §12; applicable Clause 11 and Table A.2 | LV CP MS MR CL | Relevant native preferences, orientation and input alternatives remain effective | CTL-014, CTL-017, CTL-018, CTL-107, CTL-108 | No coverage assigned | E — [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03) | Physical-device text, switch, keyboard, voice and gesture review as relevant; no universal web CSS threshold |
| [APP-04](#app-04) — Native authentication permissions and recovery | Guide §12; applicable Clause 11 and Table A.2 | NV MS CL MH | People can identify controls, choose permissions, recover from errors and understand completion | CTL-072, CTL-078, CTL-122, CTL-126, CTL-133 | No coverage assigned | E — [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Human reviews system dialogs, third-party sign-in and relevant AT; WCAG 2.2 accessible authentication is an additional baseline if adopted |
| [APP-05](#app-05) — Hybrid apps and platform-specific coverage | Guide §12; Tables A.1/A.2 conditions | NV LV DH LH MS CL | Every surface and supported platform has its own applicable test evidence | QA-AGENT, QA-MGMT | No coverage assigned | A — [AI-APP-05](EN301549_AI_Test_Prompts.md#ai-app-05) | Reviewer approves coverage; Android success is not evidence for iOS |

### Additional EN requirements and function conditions

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [EN-01](#en-01) — Accessibility feature activation | Guide §10.11; activation requirements; EN 5.2 | NV LV DH LH MS CL | Features can be activated without requiring the capability they are intended to replace | CTL-091, CTL-092, CTL-107 | No coverage assigned | E — [AI-EN-01](EN301549_AI_Test_Prompts.md#ai-en-01) | Human confirms discoverability and activation with relevant AT; additional EN-specific test beyond CTL support |
| [EN-02](#en-02) — Biometric identification alternatives | Guide §10.11; biometric requirements; EN 5.3 | NV LV MS MR | Applicable biometric identification meets the selected clause's permitted-alternative conditions | CTL-107 | No coverage assigned | E — [AI-EN-02](EN301549_AI_Test_Prompts.md#ai-en-02) | Reviewer checks the exact clause and identity-security constraints; do not infer that any fallback is sufficient |
| [EN-03](#en-03) — Accessibility preservation during conversion | Guide §10.11; conversion requirements; EN 5.4 | NV LV DH CL | Required accessibility information is preserved or a documented equivalent provided under the applicable clause | CTL-034, CTL-060, CTL-066, CTL-183 | No coverage assigned | E — [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03) | Specialist verifies output meaning and actual reader/player operation; supplemental EN conversion test |
| [EN-04](#en-04) — Voice bandwidth and communication quality | Guide §10.12; voice communication conditions; EN 6.1 | LH DH | Measured voice function satisfies the selected clause's conditions | QA-AGENT | No coverage assigned | E — [AI-EN-04](EN301549_AI_Test_Prompts.md#ai-en-04) | Audio/communications specialist validates measurement method and applicable thresholds; no browser-only inference |
| [EN-05](#en-05) — Real-time text provision and presentation | Guide §10.12; real-time text conditions; EN 6.2.1.1–6.2.2.4 | DH LH NS CL | Applicable RTT provision and display conditions are met for both participants | QA-AGENT | No coverage assigned | E — [AI-EN-05](EN301549_AI_Test_Prompts.md#ai-en-05) | Specialist validates exact subclauses, endpoint support and user experience |
| [EN-06](#en-06) — Real-time text interoperability and latency | Guide §10.12; interoperability and responsiveness; EN 6.2.3(a–d), 6.2.4 | DH LH NS | Applicable interoperability and responsiveness conditions are evidenced | QA-AGENT | No coverage assigned | E — [AI-EN-06](EN301549_AI_Test_Prompts.md#ai-en-06) | Specialist checks endpoint matrices, clock synchronisation and clause thresholds |
| [EN-07](#en-07) — Caller identification and voice-service alternatives | Guide §10.12; caller information; EN 6.3, 6.4 | DH LH NS NV | Caller information and alternatives satisfy the selected conditional requirements | QA-AGENT | No coverage assigned | E — [AI-EN-07](EN301549_AI_Test_Prompts.md#ai-en-07) | Human AT and communication review; an informational site need not add a calling service solely for this test |
| [EN-08](#en-08) — Video quality and audiovisual synchronisation | Guide §10.12; video communication conditions; EN 6.5.2–6.5.4 | DH LH NS CL | Applicable video communication quality and synchronisation conditions are met | QA-AGENT | No coverage assigned | E — [AI-EN-08](EN301549_AI_Test_Prompts.md#ai-en-08) | Specialist measurement and sign-language/lipreading review where relevant |
| [EN-09](#en-09) — Audio activity speaker identity and video alternatives | Guide §10.12; communication indicators; EN 6.5.5–6.5.6; any additional 6.6 commitment separately | DH LH NS NV | Applicable communication indicators and alternatives are available and usable | QA-AGENT | No coverage assigned | E — [AI-EN-09](EN301549_AI_Test_Prompts.md#ai-en-09) | Human checks indicator meaning and actual communication experience against selected clauses |
| [EN-10](#en-10) — Caption playback synchronisation preservation and presentation | Guide §10.7 and §10.10; media access features; EN 7.1.1–7.1.4 | DH LH CL | Applicable caption processing, presentation and preservation conditions are met | CTL-181, CTL-183 | No coverage assigned | E — [AI-EN-10](EN301549_AI_Test_Prompts.md#ai-en-10) | Human checks readability and full playback; separately establish whether spoken-subtitle conditions apply |
| [EN-11](#en-11) — Audio-description playback synchronisation and preservation | Guide §10.7 and §10.10; media access features; EN 7.2.1–7.2.3 | NV LV | Applicable description playback, alignment and preservation conditions are met | CTL-181, CTL-184 | No coverage assigned | E — [AI-EN-11](EN301549_AI_Test_Prompts.md#ai-en-11) | Human listens for mixing, timing and lost content; does not establish editorial sufficiency by metadata alone |
| [EN-12](#en-12) — Caption and description activation controls | Guide §10.7 and §10.10; media controls; EN 7.3 | NV LV DH LH MS | Required access-feature controls can be located and operated accessibly under applicable conditions | CTL-091, CTL-092, CTL-181 | No coverage assigned | E — [AI-EN-12](EN301549_AI_Test_Prompts.md#ai-en-12) | Human verifies actual AT output and comparative access effort |
| [EN-13](#en-13) — Platform services AT interoperability and user control | Guide §10.13; software accessibility services; EN 11.5–11.6, subject to Table A.2 selections | NV LV MS CL | Applicable software interoperability and control conditions have evidence | CTL-071, CTL-107, CTL-157 | No coverage assigned | E — [AI-EN-13](EN301549_AI_Test_Prompts.md#ai-en-13) | Native software specialist must expand exact Clause 11 subclauses; CTL mappings are partial only |
| [EN-14](#en-14) — Respect applicable user preferences | Guide §10.13; user preferences; EN 11.7 | NV LV CP CL MH | Relevant platform/user preferences are honoured under applicable conditions | CTL-014, CTL-019, CTL-022 | No coverage assigned | E — [AI-EN-14](EN301549_AI_Test_Prompts.md#ai-en-14) | Human verifies necessary exceptions and combined settings; reduced-motion support alone is not universal WAD proof |
| [EN-15](#en-15) — Accessible content production repair and templates | Guide §10.13; authoring tools; EN 11.8.1–11.8.5 | NV LV DH CL | Offered authoring tools meet applicable support-for-accessible-content conditions | QA-AGENT | No coverage assigned | E — [AI-EN-15](EN301549_AI_Test_Prompts.md#ai-en-15) | Authoring/document specialist expands and judges exact Clause 11 conditions; no existing exact CTL test |
| [EN-16](#en-16) — Accessible feature and compatibility documentation | Guide §10.13; documentation; EN 12.1.1–12.1.2 | NV LV DH LH CL | Required documentation describes relevant accessibility/compatibility features and is itself accessible | QA-MGMT | No coverage assigned | A — [AI-EN-16](EN301549_AI_Test_Prompts.md#ai-en-16) | Human checks completeness, accuracy and practical usability |
| [EN-17](#en-17) — Accessible support information and communication | Guide §10.13; support; EN 12.2.2–12.2.4 | NV DH LH NS CL | Applicable support information and communication conditions are satisfied | QA-MGMT | No coverage assigned | A — [AI-EN-17](EN301549_AI_Test_Prompts.md#ai-en-17) | Human reviews actual communication and alternatives; do not contact staff without explicit sending authorisation |
| [EN-18](#en-18) — Spoken-subtitle processing where applicable | Guide §§10.7 and 10.10; selected caption-processing conditions; EN 7.1.5 | NV LV CL | Applicable spoken-subtitle processing has direct playback evidence | CTL-181 | No coverage assigned | E — [AI-EN-18](EN301549_AI_Test_Prompts.md#ai-en-18) | Media/EN specialist determines exact applicability and listens to the actual output |

### Scope and exclusions

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [SCOPE-01](#scope-01) — Public body national law and service scope | Guide §§3–4; Articles 1–3 | ALL | Scope and responsibility have a reasoned, documented basis | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-01](EN301549_AI_Test_Prompts.md#ai-scope-01) | Public body/legal reviewer decides scope; outsourcing does not remove accountability |
| [SCOPE-02](#scope-02) — Public service broadcasting exclusion | Guide §5.1; Article 1(3) | ALL | Only qualifying assets are assigned this exclusion | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-02](EN301549_AI_Test_Prompts.md#ai-scope-02) | Legal reviewer confirms remit and scope |
| [SCOPE-03](#scope-03) — NGO exclusion conditions | Guide §5.2; Article 1(3) | ALL | Charitable/NGO status alone is not used as an exclusion | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-03](EN301549_AI_Test_Prompts.md#ai-scope-03) | Legal reviewer applies entity and service definitions |
| [SCOPE-04](#scope-04) — Schools and essential administrative functions | Guide §5.3; Article 1(5) | ALL | Only nationally permitted exclusions are used; essential administrative functions remain assessed | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-04](EN301549_AI_Test_Prompts.md#ai-scope-04) | Legal reviewer approves national option and essential-function decisions |
| [SCOPE-05](#scope-05) — Older office documents | Guide §5.4; Article 1(4) | ALL | Only documents meeting both applicable date and active-process conditions are excluded | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-05](EN301549_AI_Test_Prompts.md#ai-scope-05) | Reviewer confirms current administrative use and provenance |
| [SCOPE-06](#scope-06) — Older prerecorded and live media | Guide §§5.5–5.6; Article 1(4) | NV DH LH | Each asset has a supported media-scope decision; players/surrounding pages remain separately assessed | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-06](EN301549_AI_Test_Prompts.md#ai-scope-06) | Legal/content reviewer decides scope and national treatment of retained recordings |
| [SCOPE-07](#scope-07) — Navigation maps essential information | Guide §5.7; Article 1(4) | NV LV MS CL | Essential navigation information is available accessibly when the map exclusion is used | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-07](EN301549_AI_Test_Prompts.md#ai-scope-07) | Human checks completeness and actual wayfinding task; exclusion is not a technical map pass |
| [SCOPE-08](#scope-08) — Third-party funding development and control | Guide §5.8; Article 1(4) | ALL | Only content satisfying all applicable exclusion conditions is assigned this exclusion | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-08](EN301549_AI_Test_Prompts.md#ai-scope-08) | Public body/legal reviewer determines actual control and responsibility |
| [SCOPE-09](#scope-09) — Heritage reproductions and metadata | Guide §5.9; Article 1(4) | NV LV CL | Exclusion is limited to justified reproduction conditions; associated metadata remains considered | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-09](EN301549_AI_Test_Prompts.md#ai-scope-09) | Heritage and legal specialist validates reasons and feasible accessibility |
| [SCOPE-10](#scope-10) — Older intranet and extranet content | Guide §§4.4 and 5.10; Article 1(4) | ALL | Only qualifying content retains this exclusion until substantial revision | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-10](EN301549_AI_Test_Prompts.md#ai-scope-10) | Human/legal review defines substantial revision; no invented universal numeric threshold |
| [SCOPE-11](#scope-11) — Archive conditions | Guide §5.11; Article 1(4) | ALL | Archive exclusions require both inactive administrative use and qualifying update history | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-11](EN301549_AI_Test_Prompts.md#ai-scope-11) | Reviewer confirms service boundaries and evidence |
| [SCOPE-12](#scope-12) — Disproportionate burden record | Guide §6; Article 5 | ALL | A reasoned requirement-specific assessment is distinct from technical status | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-SCOPE-12](EN301549_AI_Test_Prompts.md#ai-scope-12) | Human accountable/legal authority decides burden; AI cannot approve it |

### Operational duties and outcome assurance

| Test / requirement | Source / baseline | Groups | Expected outcome | Existing QA support | AXE automation | AI / prompt | Manual complement |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [GOV-01](#gov-01) — Declared technical and legal baseline | Guide §9; Article 6 | ALL | Every assessment declares its baseline and additions separately | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-01](EN301549_AI_Test_Prompts.md#ai-gov-01) | Reviewer verifies current Official Journal/national reference before any conformity claim |
| [GOV-02](#gov-02) — Clause-level applicability register | Guide §§10.10 and 11.2 | ALL | All relevant Annex A requirements have documented applicability and assessment records | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-02](EN301549_AI_Test_Prompts.md#ai-gov-02) | EN specialist expands conditional clause families before audit sign-off |
| [GOV-03](#gov-03) — Representative sample and complete processes | Guide §11.3 | ALL | Samples cover meaningful variation and complete selected journeys with stated limits | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-03](EN301549_AI_Test_Prompts.md#ai-gov-03) | Reviewer approves sample and expansion on systemic findings |
| [GOV-04](#gov-04) — Layered test methods and AT coverage | Guide §11.4 | ALL | Evidence uses appropriate complementary methods rather than a scan-only claim | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-04](EN301549_AI_Test_Prompts.md#ai-gov-04) | Accessibility lead reviews sufficiency and resolves conflicting results |
| [GOV-05](#gov-05) — Real user outcomes and equivalent task completion | Guide §§1 and 11.5 | ALL | People can complete meaningful tasks and understand decisions; differences and barriers are recorded | QA-MGMT, QA-AGENT | No coverage assigned | N — — | Manual user research only; agent simulation cannot establish participant experience |
| [GOV-06](#gov-06) — Traceable evidence honest status and privacy | Guide §§11.6–11.10 | ALL | Results are traceable and uncertainty and personal data are handled accurately | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-06](EN301549_AI_Test_Prompts.md#ai-gov-06) | Reviewer checks evidence adequacy, retention and factual accuracy |
| [GOV-07](#gov-07) — Statement location format and identification | Guide §§13.1–13.2; Article 7 and Decision 2018/1523 | ALL | Statement is available in the required location and identifies its actual scope | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-07](EN301549_AI_Test_Prompts.md#ai-gov-07) | Human confirms legal details and actual accessibility |
| [GOV-08](#gov-08) — Statement content and evidence accuracy | Guide §§13.2–13.5 | ALL | Statement accurately describes known assessed conditions using the required model | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-08](EN301549_AI_Test_Prompts.md#ai-gov-08) | Accountable human approves legal/compliance assertions and publication |
| [GOV-09](#gov-09) — Regular statement review | Guide §13.6 | ALL | Statement is maintained accurately under applicable review duties | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-09](EN301549_AI_Test_Prompts.md#ai-gov-09) | Human decides necessary changes and approvals |
| [GOV-10](#gov-10) — Feedback access and requests for excluded/burden information | Guide §14; Article 7(1) | ALL | Anyone can report failures and request covered categories of information through an accessible mechanism | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-10](EN301549_AI_Test_Prompts.md#ai-gov-10) | Human checks actual AT use; external sending requires explicit authorisation |
| [GOV-11](#gov-11) — Feedback routing response and alternatives | Guide §14; Article 7(1) | ALL | Requests reach accountable teams and receive adequate timely responses and usable alternatives | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-11](EN301549_AI_Test_Prompts.md#ai-gov-11) | Human judges adequacy and any live service test; no real messages without sending authorisation |
| [GOV-12](#gov-12) — Enforcement and unsatisfactory response | Guide §18; Article 9 | ALL | Users can find the relevant effective enforcement route | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-12](EN301549_AI_Test_Prompts.md#ai-gov-12) | Human validates national authority and procedure; no complaint is submitted by this test |
| [GOV-13](#gov-13) — National simplified and in-depth monitoring methods | Guide §§15.1–15.2; Article 8 and Decision 2018/1524 | ALL | Monitoring methods satisfy their respective scope; a clean simplified scan is not full compliance | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-13](EN301549_AI_Test_Prompts.md#ai-gov-13) | Monitoring authority validates method; these are national duties |
| [GOV-14](#gov-14) — National sample composition and page selection | Guide §§15.3–15.4; Decision 2018/1524 | ALL | National samples follow applicable decision rules and recorded selection methods | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-14](EN301549_AI_Test_Prompts.md#ai-gov-14) | Monitoring authority confirms exact calculations; no internal public-body page quota is inferred |
| [GOV-15](#gov-15) — National reporting and useful corrective findings | Guide §15.5; Article 8 | ALL | National reports meet applicable cycle and accessibility duties; bodies can act on findings | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-15](EN301549_AI_Test_Prompts.md#ai-gov-15) | Monitoring authority approves reports and publication |
| [GOV-16](#gov-16) — Supplier evidence and accountable ownership | Guide §16 | ALL | Public body ownership and supplier evidence cover actual deployed service | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-16](EN301549_AI_Test_Prompts.md#ai-gov-16) | Accountable procurement/service owners decide duties; declaration alone is insufficient |
| [GOV-17](#gov-17) — Training awareness and accessible delivery controls | Guide §17; Article 7(4)–(5) | ALL | Relevant training/awareness obligations and adopted delivery controls have evidence | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-17](EN301549_AI_Test_Prompts.md#ai-gov-17) | Human evaluates duty holder and control effectiveness; attendance is not proof of competence |
| [GOV-18](#gov-18) — Regression correction and change review | Guide §17; Article 4 and Article 7(1) | ALL | Changes are assessed, failures tracked and evidence/statements kept current | QA-MGMT, QA-AGENT | No coverage assigned | A — [AI-GOV-18](EN301549_AI_Test_Prompts.md#ai-gov-18) | Human release/service decision; prioritisation does not convert failure into pass |

## Test specifications

These procedures make every matrix row executable. For conditional EN tests, identify the actual Annex A subclauses and their applicability/thresholds before executing; retain a result for each subclause rather than one blanket category result.

### WEB-111

**Non-text content** · Guide §§8–10; EN 9.1.1.1; WCAG 2.1 1.1.1 · Groups: NV LV CP CL

**Procedure**

1. Inventory meaningful, decorative, functional and complex images, icons, charts and image maps.
2. Extract alternatives including CSS/background content.
3. Compare alternatives with image purpose and surrounding task, flagging uncertain meaning.

**Expected:** Equivalent information or function is available in text; decorative content does not add irrelevant announcements.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: image-alt, input-image-alt, area-alt, object-alt. AI: AI-assisted analysis/evidence only; [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111). Manual: Content reviewer confirms meaning, chart information and decorative decisions; screen reader checks output.

**QA relationship:** CTL-007 (partial support); CTL-033 (direct requirement); CTL-034 (direct requirement); CTL-035 (partial support); CTL-036 (direct requirement); CTL-038 (direct requirement); CTL-039 (direct requirement); CTL-040 (partial support); CTL-187 (direct requirement); CTL-195 (direct requirement).

### WEB-121

**Audio-only and video-only prerecorded** · Guide §§8–10; EN 9.1.2.1; WCAG 2.1 1.2.1 · Groups: NV DH LH CL

**Procedure**

1. Inventory prerecorded audio-only and silent video assets.
2. Locate text alternatives or equivalent audio as appropriate.
3. Compare timed samples with the alternative and list omissions.

**Expected:** Applicable audio-only information has equivalent text; silent video has equivalent text or audio.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-121](EN301549_AI_Test_Prompts.md#ai-web-121). Manual: Review full asset and alternative for equivalence and applicable exceptions.

**QA relationship:** CTL-181 (partial support).

### WEB-122

**Captions prerecorded** · Guide §§8–10; EN 9.1.2.2; WCAG 2.1 1.2.2 · Groups: DH LH CL

**Procedure**

1. Find prerecorded audiovisual assets and caption tracks.
2. Extract cue timings and check gaps, overlaps and playback.
3. Compare speech, speaker changes and meaningful sounds with captions, preserving recognition uncertainty.

**Expected:** Required captions convey speech and meaningful audio information in synchronisation.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: video-caption. AI: AI-assisted analysis/evidence only; [AI-WEB-122](EN301549_AI_Test_Prompts.md#ai-web-122). Manual: Human checks full-asset accuracy, speaker identification, sounds and synchronisation.

**QA relationship:** CTL-183 (direct requirement).

### WEB-123

**Audio description or media alternative prerecorded** · Guide §§8–10; EN 9.1.2.3; WCAG 2.1 1.2.3 · Groups: NV LV CL

**Procedure**

1. Identify essential visual information absent from audio.
2. Locate description or a complete media alternative.
3. Compare action, events and displayed text with that alternative.

**Expected:** Applicable prerecorded video has description or a full time-based media alternative under this criterion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-123](EN301549_AI_Test_Prompts.md#ai-web-123). Manual: Editorial equivalence and exception review; dialogue transcript alone is insufficient.

**QA relationship:** CTL-184 (partial support).

### WEB-124

**Captions live** · Guide §5.6 and §10.7; EN 9.1.2.4 / WCAG 2.1 1.2.4; additional baseline only, absent from WAD Annex A · Groups: DH LH

**Procedure**

1. Confirm an adopted national or organisational live-caption requirement; do not treat this test as a WAD minimum duty.
2. Identify an authorised test stream after scope review.
3. Verify caption selection and delivery in timestamped intervals.
4. Record outages and measurable delay.

**Expected:** In-scope live audiovisual content has required live captions; WAD live-media exclusion is decided separately.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-124](EN301549_AI_Test_Prompts.md#ai-web-124). Manual: WAD excludes live time-based media and Annex A omits live-caption clauses. Reviewer confirms any separately adopted requirement and checks actual captions..

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-125

**Audio description prerecorded** · Guide §§8–10; EN 9.1.2.5; WCAG 2.1 1.2.5 · Groups: NV LV

**Procedure**

1. Identify essential visuals absent from programme audio.
2. Select the description track and capture timestamped playback.
3. List missing visual events and description collisions.

**Expected:** Required description conveys essential visual information; transcript alone does not satisfy this criterion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-125](EN301549_AI_Test_Prompts.md#ai-web-125). Manual: Human editorial and playback review; consider whether existing audio conveys required visuals.

**QA relationship:** CTL-184 (partial support).

### WEB-131

**Information and relationships** · Guide §§8–10; EN 9.1.3.1; WCAG 2.1 1.3.1 · Groups: NV LV CL

**Procedure**

1. Compare visible headings, lists, tables, labels and groups with DOM and accessibility-tree relations.
2. Inspect representative table headers and grouped inputs.
3. Record implied relationships missing from semantic output.

**Expected:** Structure and relationships are programmatically determinable or available in text.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: definition-list, aria-required-children, aria-required-parent. AI: AI execution of stated observable subset; [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131). Manual: Screen reader navigation and content review; a single H1 or table caption is not universally mandatory.

**QA relationship:** CTL-054 (partial support); CTL-056 (direct requirement); CTL-058 (direct requirement); CTL-063 (direct requirement); CTL-066 (direct requirement); CTL-069 (partial support); CTL-080 (partial support); CTL-088 (direct requirement); CTL-113 (partial support); CTL-119 (partial support); CTL-120 (partial support); CTL-121 (partial support); CTL-143 (direct requirement); CTL-163 (partial support); CTL-169 (partial support); CTL-176 (partial support); CTL-191 (direct requirement); CTL-196 (partial support).

### WEB-132

**Meaningful sequence** · Guide §§8–10; EN 9.1.3.2; WCAG 2.1 1.3.2 · Groups: NV LV CL

**Procedure**

1. Capture DOM, accessibility-tree and visible reading order.
2. Linearise cards, columns and dialogs.
3. Identify sequences that change meaning.

**Expected:** A correct reading sequence is available where order affects meaning.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-132](EN301549_AI_Test_Prompts.md#ai-web-132). Manual: Human narrative and task-order review with screen reader.

**QA relationship:** CTL-060 (direct requirement); CTL-062 (partial support); CTL-189 (partial support).

### WEB-133

**Sensory characteristics** · Guide §§8–10; EN 9.1.3.3; WCAG 2.1 1.3.3 · Groups: NV LV DH CP CL

**Procedure**

1. Extract instructions referring to shape, position, size, orientation or sound.
2. Locate non-sensory control identifiers.
3. Flag instructions that cannot be resolved through text or semantics.

**Expected:** Instructions do not rely solely on sensory characteristics.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-133](EN301549_AI_Test_Prompts.md#ai-web-133). Manual: Human tests instructions with relevant access methods.

**QA relationship:** CTL-040 (partial support); CTL-152 (partial support).

### WEB-134

**Orientation** · Guide §§8–10; EN 9.1.3.4; WCAG 2.1 1.3.4 · Groups: LV MS MR

**Procedure**

1. Run portrait and landscape viewports or device orientations.
2. Complete the same tasks in both.
3. Record locking and claimed essential-orientation reasons.

**Expected:** No single-orientation restriction unless essential.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-134](EN301549_AI_Test_Prompts.md#ai-web-134). Manual: Physical-device verification and exception review.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-135

**Identify input purpose** · Guide §§8–10; EN 9.1.3.5; WCAG 2.1 1.3.5 · Groups: NV CL MS

**Procedure**

1. Inventory fields collecting information about the user.
2. Compare applicable purposes with machine-readable input-purpose tokens.
3. Check token validity and purpose agreement.

**Expected:** Covered personal-data input purposes are programmatically identifiable.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-135](EN301549_AI_Test_Prompts.md#ai-web-135). Manual: Confirm actual purpose and autofill or AT behaviour.

**QA relationship:** CTL-118 (direct requirement).

### WEB-141

**Use of colour** · Guide §§8–10; EN 9.1.4.1; WCAG 2.1 1.4.1 · Groups: CP LV NV CL

**Procedure**

1. Inventory coloured status, errors, required states, selections, links and data series.
2. Inspect text, shapes, patterns and semantic equivalents.
3. Compare greyscale and original information.

**Expected:** Colour is not the sole visual means of conveying information or distinction.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141). Manual: Human visual and semantic review; simulation does not reproduce individual vision.

**QA relationship:** CTL-001 (direct requirement); CTL-002 (partial support); CTL-003 (partial support); CTL-004 (direct requirement); CTL-005 (partial support); CTL-006 (direct requirement); CTL-007 (partial support).

### WEB-142

**Audio control** · Guide §§8–10; EN 9.1.4.2; WCAG 2.1 1.4.2 · Groups: NV LH CL MH

**Procedure**

1. Observe initial load and triggered media.
2. Measure automatic audio duration.
3. Operate pause, stop or independent volume with keyboard.

**Expected:** Automatic audio longer than three seconds has an applicable pause, stop or independent volume mechanism.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: no-autoplay-audio. AI: AI execution of stated observable subset; [AI-WEB-142](EN301549_AI_Test_Prompts.md#ai-web-142). Manual: Listen to output and verify usability alongside screen reader audio.

**QA relationship:** CTL-028 (partial support); CTL-030 (direct requirement); CTL-182 (partial support).

### WEB-143

**Contrast minimum** · Guide §§8–10; EN 9.1.4.3; WCAG 2.1 1.4.3 · Groups: LV CP

**Procedure**

1. Measure text foreground/background pairs across default, hover, focus and error states.
2. Record font size, weight, colours and ratios.
3. Separate large text, exceptions and unmeasurable backgrounds.

**Expected:** Ordinary text reaches 4.5:1 and qualifying large text 3:1 subject to exceptions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: color-contrast. AI: AI execution of stated observable subset; [AI-WEB-143](EN301549_AI_Test_Prompts.md#ai-web-143). Manual: Measure image text, gradients and overlays manually; inactive controls may be exempt.

**QA relationship:** CTL-008 (direct requirement); CTL-009 (direct requirement); CTL-012 (direct requirement).

### WEB-144

**Resize text** · Guide §§8–10; EN 9.1.4.4; WCAG 2.1 1.4.4 · Groups: LV CL

**Procedure**

1. Apply actual text resizing to 200 percent.
2. Exercise navigation, forms and dialogs.
3. Compare clipping, overlap and functional loss.

**Expected:** Text resizes to 200 percent without loss under applicable conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144). Manual: Confirm text-resize and full-task behaviour; viewport reduction alone is insufficient.

**QA relationship:** CTL-014 (direct requirement); CTL-015 (partial support); CTL-017 (partial support); CTL-018 (partial support); CTL-020 (partial support).

### WEB-145

**Images of text** · Guide §§8–10; EN 9.1.4.5; WCAG 2.1 1.4.5 · Groups: LV CL

**Procedure**

1. Inventory images containing text.
2. Compare with selectable text and customisation options.
3. Identify logotypes and claimed essential presentations.

**Expected:** Text replaces images of text where required.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-145](EN301549_AI_Test_Prompts.md#ai-web-145). Manual: Reviewer determines essential and customisable exceptions.

**QA relationship:** CTL-037 (direct requirement).

### WEB-1410

**Reflow** · Guide §§8–10; EN 9.1.4.10; WCAG 2.1 1.4.10 · Groups: LV MS CL

**Procedure**

1. Set 320 CSS pixel width for vertical reading and 256 CSS pixel height for horizontal writing.
2. Traverse content, forms, dialogs and tables.
3. Record two-dimensional scrolling and losses separately from exceptions.

**Expected:** No loss and no two-dimensional scrolling except content requiring that layout.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410). Manual: Manual magnification review and verification of two-dimensional-content exceptions.

**QA relationship:** CTL-015 (partial support); CTL-016 (direct requirement); CTL-017 (partial support); CTL-018 (partial support); CTL-020 (partial support); CTL-069 (partial support); CTL-175 (direct requirement).

### WEB-1411

**Non-text contrast** · Guide §§8–10; EN 9.1.4.11; WCAG 2.1 1.4.11 · Groups: LV CP

**Procedure**

1. Inventory controls, state indicators and meaningful graphics.
2. Measure essential visual information against adjacent colours.
3. Record ratios and native, inactive or essential exceptions.

**Expected:** Required component, state and graphical information reaches 3:1 under applicable conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-1411](EN301549_AI_Test_Prompts.md#ai-web-1411). Manual: Human identifies essential visual parts; text contrast scans do not cover this test.

**QA relationship:** CTL-011 (direct requirement).

### WEB-1412

**Text spacing** · Guide §§8–10; EN 9.1.4.12; WCAG 2.1 1.4.12 · Groups: LV CL

**Procedure**

1. Apply line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 times font size without changing other styles.
2. Exercise content and controls.
3. Record clipping, overflow and loss.

**Expected:** No content or functionality loss under applicable spacing overrides.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-1412](EN301549_AI_Test_Prompts.md#ai-web-1412). Manual: Visual and reading-tool inspection; apply language/script exceptions.

**QA relationship:** CTL-019 (direct requirement).

### WEB-1413

**Content on hover or focus** · Guide §§8–10; EN 9.1.4.13; WCAG 2.1 1.4.13 · Groups: LV MS CL

**Procedure**

1. Reveal added content through hover and focus.
2. Try dismissal without moving hover/focus.
3. Move onto added content and check persistence.

**Expected:** Applicable added content is dismissible, hoverable and persistent.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-1413](EN301549_AI_Test_Prompts.md#ai-web-1413). Manual: Human checks hover transit, magnification and exceptions.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-211

**Keyboard** · Guide §§8–10; EN 9.2.1.1; WCAG 2.1 2.1.1 · Groups: NV MS MR CL

**Procedure**

1. Inventory every task control.
2. Use ordinary keyboard events through navigation, widgets, forms and dialogs.
3. Verify equivalent task results without pointer or timed keystrokes.

**Expected:** Applicable functionality operates through a keyboard interface subject to exceptions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211). Manual: Manual keyboard and alternative-input journeys; direct script activation is not keyboard proof.

**QA relationship:** CTL-070 (partial support); CTL-091 (direct requirement); CTL-092 (direct requirement); CTL-093 (direct requirement); CTL-107 (direct requirement); CTL-133 (direct requirement); CTL-174 (partial support); CTL-178 (partial support); CTL-181 (partial support).

### WEB-212

**No keyboard trap** · Guide §§8–10; EN 9.2.1.2; WCAG 2.1 2.1.2 · Groups: NV MS MR

**Procedure**

1. Enter every region using Tab, reverse Tab and appropriate widget keys.
2. Try standard or documented keyboard exits.
3. Repeat with dialogs open and closed.

**Expected:** Focus can leave components with keyboard alone, with instructions for non-standard exits where required.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212). Manual: Manual keyboard and relevant AT verification.

**QA relationship:** CTL-094 (direct requirement); CTL-173 (partial support); CTL-174 (partial support); CTL-178 (partial support).

### WEB-214

**Character key shortcuts** · Guide §§8–10; EN 9.2.1.4; WCAG 2.1 2.1.4 · Groups: NV MS CL

**Procedure**

1. Inventory single-character shortcut handlers.
2. Trigger them outside and inside focused components on harmless fixtures.
3. Test disable, remap or focus-only restriction.

**Expected:** Applicable character shortcuts can be disabled, remapped or restricted to component focus.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-214](EN301549_AI_Test_Prompts.md#ai-web-214). Manual: Voice-input and screen reader interference review.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-221

**Timing adjustable** · Guide §§8–10; EN 9.2.2.1; WCAG 2.1 2.2.1 · Groups: NV LV MS CL MH

**Procedure**

1. Inventory server/client time limits.
2. Exercise switch-off, adjustment and extension with approved test clocks.
3. Record warning intervals, opportunities and data preservation.

**Expected:** Applicable limits meet criterion conditions for turning off, adjusting or extending, subject to exceptions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: meta-refresh. AI: AI execution of stated observable subset; [AI-WEB-221](EN301549_AI_Test_Prompts.md#ai-web-221). Manual: Human confirms exceptions and actual recovery; no universal task completion time.

**QA relationship:** CTL-160 (partial support); CTL-197 (direct requirement); CTL-198 (direct requirement).

### WEB-222

**Pause stop hide** · Guide §§8–10; EN 9.2.2.2; WCAG 2.1 2.2.2 · Groups: LV NV CL MH

**Procedure**

1. Inventory moving, blinking, scrolling and auto-updating content.
2. Measure automatic start, duration and parallel content.
3. Use pause, stop, hide or frequency controls.

**Expected:** Applicable movement and updates provide required user controls.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: blink. AI: AI execution of stated observable subset; [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222). Manual: Human reviews user control and essential exceptions.

**QA relationship:** CTL-023 (direct requirement); CTL-024 (direct requirement); CTL-028 (partial support); CTL-029 (direct requirement); CTL-182 (partial support).

### WEB-231

**Three flashes or below threshold** · Guide §§8–10; EN 9.2.3.1; WCAG 2.1 2.3.1 · Groups: PS

**Procedure**

1. Collect animations and video without displaying suspected unsafe flashing.
2. Run an approved flash analyser on complete assets.
3. Record version, settings, results and unanalysed dynamic output.

**Expected:** Content satisfies applicable frequency or flash-area/luminance conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-231](EN301549_AI_Test_Prompts.md#ai-web-231). Manual: Specialist reviews analyser output; never expose participants to suspected hazardous flashing.

**QA relationship:** CTL-026 (direct requirement).

### WEB-241

**Bypass blocks** · Guide §§8–10; EN 9.2.4.1; WCAG 2.1 2.4.1 · Groups: NV MS CL

**Procedure**

1. Identify repeated blocks.
2. Activate the implemented bypass mechanism by keyboard.
3. Record focus destination and next navigation position.

**Expected:** A working mechanism bypasses repeated blocks.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: bypass. AI: AI execution of stated observable subset; [AI-WEB-241](EN301549_AI_Test_Prompts.md#ai-web-241). Manual: Keyboard and screen reader checks; a skip link is one permissible technique.

**QA relationship:** CTL-052 (direct requirement); CTL-053 (partial support).

### WEB-242

**Page titled** · Guide §§8–10; EN 9.2.4.2; WCAG 2.1 2.4.2 · Groups: NV LV CL

**Procedure**

1. Read browser titles on initial load and each tested route.
2. Compare with page topic and task.
3. Record empty, stale or ambiguous titles.

**Expected:** Titles describe topic or purpose of assessed pages.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: document-title. AI: AI execution of stated observable subset; [AI-WEB-242](EN301549_AI_Test_Prompts.md#ai-web-242). Manual: Human checks useful differentiation and SPA context.

**QA relationship:** CTL-044 (direct requirement); CTL-045 (direct requirement); CTL-047 (partial support).

### WEB-243

**Focus order** · Guide §§8–10; EN 9.2.4.3; WCAG 2.1 2.4.3 · Groups: NV LV MS CL

**Procedure**

1. Record focus through forms, navigation and dialogs.
2. Open, close, validate and navigate back.
3. Compare transitions with meaningful task sequence.

**Expected:** Sequential focus preserves meaning and operability.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243). Manual: Human checks logical transitions and orientation; positive tabindex alone is not failure proof.

**QA relationship:** CTL-053 (partial support); CTL-061 (direct requirement); CTL-062 (partial support); CTL-070 (partial support); CTL-097 (direct requirement); CTL-098 (direct requirement); CTL-164 (direct requirement); CTL-173 (partial support); CTL-189 (partial support).

### WEB-244

**Link purpose in context** · Guide §§8–10; EN 9.2.4.4; WCAG 2.1 2.4.4 · Groups: NV CL

**Procedure**

1. Extract link names and programmatically determined context.
2. Compare with destinations.
3. Flag misleading or ambiguous links.

**Expected:** Link purpose follows from text alone or permitted programmatically determined context.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: link-name, area-alt. AI: AI-assisted analysis/evidence only; [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244). Manual: Human context review; stronger out-of-context CTL rules are not automatically mandatory.

**QA relationship:** CTL-136 (direct requirement); CTL-137 (direct requirement); CTL-140 (direct requirement); CTL-147 (partial support).

### WEB-245

**Multiple ways** · Guide §§8–10; EN 9.2.4.5; WCAG 2.1 2.4.5 · Groups: NV LV CL

**Procedure**

1. Inventory the scoped page set.
2. Exercise search, sitemap, navigation or equivalent methods.
3. Identify process/result exceptions.

**Expected:** More than one way locates pages within a set except applicable exceptions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-245](EN301549_AI_Test_Prompts.md#ai-web-245). Manual: Reviewer establishes set boundaries and usable discovery.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-246

**Headings and labels** · Guide §§8–10; EN 9.2.4.6; WCAG 2.1 2.4.6 · Groups: NV LV CL

**Procedure**

1. List headings and labels with corresponding content or actions.
2. Compare topic and purpose.
3. Flag misdescription or ambiguity.

**Expected:** Headings and labels describe topic or purpose.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-246](EN301549_AI_Test_Prompts.md#ai-web-246). Manual: Human content and AT navigation review.

**QA relationship:** CTL-054 (partial support); CTL-057 (direct requirement); CTL-081 (partial support).

### WEB-247

**Focus visible** · Guide §§8–10; EN 9.2.4.7; WCAG 2.1 2.4.7 · Groups: LV MS MR

**Procedure**

1. Navigate every control by keyboard.
2. Capture focus in supported themes and sizes.
3. Flag missing, clipped or obscured indicators.

**Expected:** Keyboard focus is visible.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247). Manual: Human visual checks; do not import newer enhanced focus geometry into this baseline.

**QA relationship:** CTL-005 (partial support); CTL-095 (direct requirement); CTL-096 (direct requirement); CTL-103 (direct requirement).

### WEB-251

**Pointer gestures** · Guide §§8–10; EN 9.2.5.1; WCAG 2.1 2.5.1 · Groups: MS MR

**Procedure**

1. Inventory multipoint/path-based gestures.
2. Perform each function through single-pointer non-path alternatives.
3. Record essential-gesture claims.

**Expected:** Applicable gestures have single-pointer alternatives without a path.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-251](EN301549_AI_Test_Prompts.md#ai-web-251). Manual: Physical-device and alternative-input review; keep additional WCAG 2.2 dragging requirements separate.

**QA relationship:** CTL-108 (direct requirement); CTL-109 (partial support).

### WEB-252

**Pointer cancellation** · Guide §§8–10; EN 9.2.5.2; WCAG 2.1 2.5.2 · Groups: MS MR CL

**Procedure**

1. Test down, move-away, cancel and release on sandbox actions.
2. Verify abort, undo or up-event completion.
3. Record exceptions.

**Expected:** Functions meet applicable cancellation or reversal conditions unless essential.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-252](EN301549_AI_Test_Prompts.md#ai-web-252). Manual: Human touch-behaviour and exception review.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-253

**Label in name** · Guide §§8–10; EN 9.2.5.3; WCAG 2.1 2.5.3 · Groups: MS CL NV

**Procedure**

1. Extract visible text and computed accessible names.
2. Check whether visible labels are contained in names.
3. Separate icon-only and symbolic labels.

**Expected:** Textual visible labels are contained in accessible names where required.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-253](EN301549_AI_Test_Prompts.md#ai-web-253). Manual: Human verifies visual text and voice invocation; missing-name scans are insufficient.

**QA relationship:** CTL-073 (direct requirement).

### WEB-254

**Motion actuation** · Guide §§8–10; EN 9.2.5.4; WCAG 2.1 2.5.4 · Groups: MS MR

**Procedure**

1. Identify shake/tilt functions.
2. Exercise UI alternatives and disable motion response.
3. Verify disabled motion does not change state.

**Expected:** Applicable motion functions have UI alternatives and disable controls subject to exceptions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-254](EN301549_AI_Test_Prompts.md#ai-web-254). Manual: Physical-device and exception verification.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-311

**Language of page** · Guide §§8–10; EN 9.3.1.1; WCAG 2.1 3.1.1 · Groups: NV CL

**Procedure**

1. Read language metadata.
2. Compare with primary human language.
3. Record invalid or conflicting values.

**Expected:** Default human language is programmatically determinable.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: html-has-lang, html-lang-valid. AI: AI-assisted analysis/evidence only; [AI-WEB-311](EN301549_AI_Test_Prompts.md#ai-web-311). Manual: Human language and pronunciation review.

**QA relationship:** CTL-041 (direct requirement).

### WEB-312

**Language of parts** · Guide §§8–10; EN 9.3.1.2; WCAG 2.1 3.1.2 · Groups: NV CL

**Procedure**

1. Find language changes.
2. Inspect language markings.
3. Separate proper names, technical terms and other exceptions.

**Expected:** Language changes are programmatically determinable where required.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: valid-lang. AI: AI-assisted analysis/evidence only; [AI-WEB-312](EN301549_AI_Test_Prompts.md#ai-web-312). Manual: Human language and screen reader pronunciation review.

**QA relationship:** CTL-042 (direct requirement).

### WEB-321

**On focus** · Guide §§8–10; EN 9.3.2.1; WCAG 2.1 3.2.1 · Groups: NV MS CL MH

**Procedure**

1. Traverse focusable controls with ordinary keyboard keys.
2. Record navigation, submission, new windows and context shifts.
3. Compare with intended task behaviour.

**Expected:** Receiving focus does not itself initiate context change.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-321](EN301549_AI_Test_Prompts.md#ai-web-321). Manual: Human and AT review; legitimate in-context help is not automatically a failure.

**QA relationship:** CTL-099 (partial support); CTL-156 (partial support); CTL-200 (partial support).

### WEB-322

**On input** · Guide §§8–10; EN 9.3.2.2; WCAG 2.1 3.2.2 · Groups: NV MS CL MH

**Procedure**

1. Change selects, text, radio choices and switches.
2. Observe submissions, routes and focus.
3. Check prior advice for relevant context changes.

**Expected:** Changing settings does not unexpectedly change context without required prior advice.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322). Manual: Human warning and predictability review.

**QA relationship:** CTL-099 (partial support); CTL-112 (direct requirement); CTL-156 (partial support); CTL-200 (partial support).

### WEB-323

**Consistent navigation** · Guide §§8–10; EN 9.3.2.3; WCAG 2.1 3.2.3 · Groups: NV CL MH

**Procedure**

1. Compare repeated navigation within the same set.
2. Record relative order and user customisation.
3. Flag unexpected differences.

**Expected:** Repeated navigation has consistent relative order unless user changes apply.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-323](EN301549_AI_Test_Prompts.md#ai-web-323). Manual: Human page-set and navigation review.

**QA relationship:** CTL-047 (partial support).

### WEB-324

**Consistent identification** · Guide §§8–10; EN 9.3.2.4; WCAG 2.1 3.2.4 · Groups: NV CL MH

**Procedure**

1. Inventory controls sharing a function across pages.
2. Compare labels, names and icons.
3. Flag inconsistent identification.

**Expected:** Same-function components are identified consistently.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-324](EN301549_AI_Test_Prompts.md#ai-web-324). Manual: Human functional-equivalence and context review.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-331

**Error identification** · Guide §§8–10; EN 9.3.3.1; WCAG 2.1 3.3.1 · Groups: NV LV CP CL MH

**Procedure**

1. Submit empty/invalid fixtures.
2. Capture error text, affected item, associations and announcements.
3. Correct and retry.

**Expected:** Automatically detected errors identify the item and describe the error in text.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331). Manual: Screen reader and content review.

**QA relationship:** CTL-002 (partial support); CTL-079 (direct requirement); CTL-122 (direct requirement); CTL-123 (partial support); CTL-124 (direct requirement); CTL-125 (direct requirement).

### WEB-332

**Labels or instructions** · Guide §§8–10; EN 9.3.3.2; WCAG 2.1 3.3.2 · Groups: NV LV CL

**Procedure**

1. Inventory user inputs.
2. Compare labels/instructions with required data and formats.
3. Inspect groups, required states and associations.

**Expected:** Required input has labels or instructions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: label. AI: AI execution of stated observable subset; [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332). Manual: Human verifies visible/spoken clarity and sufficient guidance.

**QA relationship:** CTL-003 (partial support); CTL-072 (direct requirement); CTL-078 (direct requirement); CTL-080 (partial support); CTL-113 (partial support); CTL-114 (direct requirement); CTL-116 (direct requirement); CTL-119 (partial support); CTL-120 (partial support); CTL-121 (partial support); CTL-134 (partial support); CTL-194 (direct requirement).

### WEB-333

**Error suggestion** · Guide §§8–10; EN 9.3.3.3; WCAG 2.1 3.3.3 · Groups: NV CL MH

**Procedure**

1. Trigger known invalid values and formats.
2. Capture correction suggestions.
3. Check whether suggestions solve the problem and record exceptions.

**Expected:** Known corrections are suggested unless a relevant exception applies.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-WEB-333](EN301549_AI_Test_Prompts.md#ai-web-333). Manual: Human wording, security and purpose-exception review.

**QA relationship:** CTL-126 (direct requirement); CTL-134 (partial support).

### WEB-334

**Error prevention legal financial data** · Guide §§8–10; EN 9.3.3.4; WCAG 2.1 3.3.4 · Groups: NV LV MS CL MH

**Procedure**

1. Identify consequential transactions in sandbox.
2. Exercise review, correction, reversal or confirmation safeguards.
3. Capture outcomes without real submissions.

**Expected:** Applicable submissions are reversible, checked or confirmed as permitted.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-334](EN301549_AI_Test_Prompts.md#ai-web-334). Manual: Human confirms scope and safeguards.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-411

**Parsing retained in WCAG 2.1 baseline** · Guide §§8–10; EN 9.4.1.1; WCAG 2.1 4.1.1 · Groups: NV

**Procedure**

1. Run approved HTML conformance checks on delivered markup and relevant generated fragments.
2. Inspect incomplete tags, improper nesting, duplicate attributes and IDs under WCAG 2.1 definitions.
3. Keep parsing findings distinct from name/role/value findings.

**Expected:** WCAG 2.1 parsing conditions are assessed independently of the WCAG 2.2 register.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-411](EN301549_AI_Test_Prompts.md#ai-web-411). Manual: Human reviews parser output; this removed WCAG 2.2 criterion has no current CTL standards mapping.

**QA relationship:** No active CTL standards relationship found. Use this supplemental test and record the coverage gap..

### WEB-412

**Name role value** · Guide §§8–10; EN 9.4.1.2; WCAG 2.1 4.1.2 · Groups: NV MS CL

**Procedure**

1. Inspect names, roles, values, states and relations before/after interaction.
2. Exercise native/custom controls using expected keyboard patterns.
3. Compare exposed properties with operation.

**Expected:** Components expose appropriate names, roles, states and values and make changes available.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: Partial: aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, input-button-name, label, frame-title. AI: AI execution of stated observable subset; [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412). Manual: Actual screen reader and alternative-input verification; ARIA syntax alone is insufficient.

**QA relationship:** CTL-035 (partial support); CTL-071 (direct requirement); CTL-081 (partial support); CTL-082 (direct requirement); CTL-147 (partial support); CTL-157 (direct requirement); CTL-161 (direct requirement); CTL-163 (partial support); CTL-167 (direct requirement); CTL-169 (partial support); CTL-172 (direct requirement); CTL-176 (partial support); CTL-177 (direct requirement); CTL-190 (direct requirement); CTL-193 (direct requirement); CTL-196 (partial support).

### WEB-413

**Status messages** · Guide §§8–10; EN 9.4.1.3; WCAG 2.1 4.1.3 · Groups: NV LV CL

**Procedure**

1. Trigger loading, validation, counts and completion.
2. Capture tree events/live-region mutations without moving focus.
3. With an actual AT harness capture announcements; otherwise mark that portion untested.

**Expected:** Applicable status messages are programmatically determinable without focus transfer.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413). Manual: Screen reader timing and verbosity review; live-region markup alone is not spoken-output proof.

**QA relationship:** CTL-123 (partial support); CTL-146 (direct requirement); CTL-150 (direct requirement); CTL-151 (direct requirement); CTL-152 (partial support); CTL-158 (direct requirement); CTL-160 (partial support); CTL-192 (direct requirement).

### DOC-01

**Document alternatives and language** · Guide §10.8; applicable Clause 10 · Groups: NV LV CL

**Procedure**

1. Inventory covered downloadable PDF, office and equivalent files with hashes/versions.
2. Extract document language and image alternatives using a format-aware checker.
3. Compare image/function descriptions with visible content.

**Expected:** Covered documents preserve equivalent text and language information.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01). Manual: Document specialist verifies actual alternatives and language with relevant AT.

**QA relationship:** CTL-033, CTL-034, CTL-035, CTL-036, CTL-041, CTL-042. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### DOC-02

**Document structure and reading order** · Guide §10.8; applicable Clause 10 · Groups: NV LV CL

**Procedure**

1. Inspect headings, tags, lists and table relations in the actual file.
2. Extract the tagged reading sequence including columns/footnotes.
3. Compare with intended order and inspect untagged content.

**Expected:** Document structure, relationships and sequence preserve meaning.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02). Manual: Format-aware manual and screen reader review; extracted text alone is insufficient.

**QA relationship:** CTL-054, CTL-060, CTL-063, CTL-066, CTL-067. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### DOC-03

**Document presentation and enlargement** · Guide §10.8; applicable Clause 10 · Groups: LV CP CL

**Procedure**

1. Measure covered document text contrast.
2. Apply supported enlargement and display adjustments in named readers.
3. Inspect clipping, missing content and interaction loss against the applicable document conditions.

**Expected:** Covered documents remain perceivable under their applicable format-specific requirements.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03). Manual: Do not impose browser CSS measurements on native readers without checking the relevant Clause 10 condition.

**QA relationship:** CTL-008, CTL-009, CTL-014, CTL-017, CTL-019. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### DOC-04

**Document links forms and errors** · Guide §10.8; applicable Clause 10 · Groups: NV MS CL

**Procedure**

1. Open interactive documents in each supported reader.
2. Traverse links and fields using keyboard and inspect names/roles.
3. Enter invalid data, correct it and complete an approved test submission.

**Expected:** Document interactions, labels, errors and recovery are usable under applicable conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04). Manual: Document form and AT testing in actual readers; no real external submission.

**QA relationship:** CTL-071, CTL-072, CTL-079, CTL-091, CTL-092, CTL-122. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### DOC-05

**Document media and conversions** · Guide §10.8; applicable Clause 10 · Groups: NV DH LH CL

**Procedure**

1. Inventory embedded media and generated/exported formats.
2. Compare originals and outputs for alternatives, structure and usable controls.
3. Record lost information and unsupported reader behaviour.

**Expected:** Applicable embedded alternatives and accessibility information survive the document workflow.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-DOC-05](EN301549_AI_Test_Prompts.md#ai-doc-05). Manual: Human media and format-conversion review; original accessible source does not establish output accessibility.

**QA relationship:** CTL-183, CTL-184. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### APP-01

**Native platform accessibility exposure** · Guide §12; applicable Clause 11 and Table A.2 · Groups: NV MS CL

**Procedure**

1. Use an authorised device/emulator inspector to capture native accessibility trees.
2. Inspect names, roles, values, states, relations and text interfaces before/after interaction.
3. Exercise custom controls through platform accessibility actions and ordinary input.

**Expected:** Native controls expose required information and operations through platform services.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-APP-01](EN301549_AI_Test_Prompts.md#ai-app-01). Manual: Actual TalkBack/VoiceOver and relevant input testing; a browser axe scan does not cover native widgets.

**QA relationship:** CTL-071, CTL-157, CTL-161. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### APP-02

**Native reading focus and screen changes** · Guide §12; applicable Clause 11 and Table A.2 · Groups: NV LV MS CL

**Procedure**

1. Trace navigation through screens, dialogs, overlays and notifications.
2. Capture focus before/after transitions and errors.
3. With an AT harness capture actual speech; otherwise leave spoken output untested.

**Expected:** Order, announcements and focus preserve orientation and complete-task operation.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02). Manual: Each supported OS and AT combination requires appropriate direct verification.

**QA relationship:** CTL-060, CTL-061, CTL-100, CTL-101, CTL-148, CTL-151. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### APP-03

**Native text settings orientation and input** · Guide §12; applicable Clause 11 and Table A.2 · Groups: LV CP MS MR CL

**Procedure**

1. Apply platform text size and accessibility settings on supported devices.
2. Repeat portrait/landscape and applicable alternative-input journeys.
3. Capture loss and preference mismatch against the selected native clauses.

**Expected:** Relevant native preferences, orientation and input alternatives remain effective.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03). Manual: Physical-device text, switch, keyboard, voice and gesture review as relevant; no universal web CSS threshold.

**QA relationship:** CTL-014, CTL-017, CTL-018, CTL-107, CTL-108. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### APP-04

**Native authentication permissions and recovery** · Guide §12; applicable Clause 11 and Table A.2 · Groups: NV MS CL MH

**Procedure**

1. Exercise sign-in, identification, permission allow/deny and recovery with test accounts.
2. Inspect platform permission prompts and error paths.
3. Complete transactions with keyboard or supported accessibility actions.

**Expected:** People can identify controls, choose permissions, recover from errors and understand completion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04). Manual: Human reviews system dialogs, third-party sign-in and relevant AT; WCAG 2.2 accessible authentication is an additional baseline if adopted.

**QA relationship:** CTL-072, CTL-078, CTL-122, CTL-126, CTL-133. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### APP-05

**Hybrid apps and platform-specific coverage** · Guide §12; Tables A.1/A.2 conditions · Groups: NV LV DH LH MS CL

**Procedure**

1. Inventory native screens, webviews, embedded documents and media.
2. Assign web/document/native test suites per surface.
3. Compare iOS/Android builds and supported versions for missing coverage.

**Expected:** Every surface and supported platform has its own applicable test evidence.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-APP-05](EN301549_AI_Test_Prompts.md#ai-app-05). Manual: Reviewer approves coverage; Android success is not evidence for iOS.

**QA relationship:** QA-AGENT, QA-MGMT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-01

**Accessibility feature activation** · Guide §10.11; activation requirements; EN 5.2 · Groups: NV LV DH LH MS CL

**Procedure**

1. Inventory documented accessibility features.
2. Start with each feature off.
3. Reach and activate it using the access method for which it is intended, logging dependencies.

**Expected:** Features can be activated without requiring the capability they are intended to replace.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-01](EN301549_AI_Test_Prompts.md#ai-en-01). Manual: Human confirms discoverability and activation with relevant AT; additional EN-specific test beyond CTL support.

**QA relationship:** CTL-091, CTL-092, CTL-107. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-02

**Biometric identification alternatives** · Guide §10.11; biometric requirements; EN 5.3 · Groups: NV LV MS MR

**Procedure**

1. Inventory biometric mechanisms and which biological characteristics they require.
2. Exercise permitted alternatives with test identities.
3. Compare identity-verification completion and access barriers.

**Expected:** Applicable biometric identification meets the selected clause's permitted-alternative conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-02](EN301549_AI_Test_Prompts.md#ai-en-02). Manual: Reviewer checks the exact clause and identity-security constraints; do not infer that any fallback is sufficient.

**QA relationship:** CTL-107. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-03

**Accessibility preservation during conversion** · Guide §10.11; conversion requirements; EN 5.4 · Groups: NV LV DH CL

**Procedure**

1. Take representative accessible input fixtures.
2. Run conversion/export/transcoding paths.
3. Compare structure, text alternatives, language, captions and other applicable metadata before/after.

**Expected:** Required accessibility information is preserved or a documented equivalent provided under the applicable clause.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03). Manual: Specialist verifies output meaning and actual reader/player operation; supplemental EN conversion test.

**QA relationship:** CTL-034, CTL-060, CTL-066, CTL-183. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-04

**Voice bandwidth and communication quality** · Guide §10.12; voice communication conditions; EN 6.1 · Groups: LH DH

**Procedure**

1. Identify actual two-way voice functions and selected applicable clauses.
2. Run a calibrated communications harness over supported configurations.
3. Record bandwidth/quality measurements, fixture signals and network conditions.

**Expected:** Measured voice function satisfies the selected clause's conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-04](EN301549_AI_Test_Prompts.md#ai-en-04). Manual: Audio/communications specialist validates measurement method and applicable thresholds; no browser-only inference.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-05

**Real-time text provision and presentation** · Guide §10.12; real-time text conditions; EN 6.2.1.1–6.2.2.4 · Groups: DH LH NS CL

**Procedure**

1. For offered voice/RTT functions connect authorised test endpoints.
2. Type bidirectionally and log incremental delivery, display, separation and any concurrent speech.
3. Compare each selected RTT provision/display condition with measurements.

**Expected:** Applicable RTT provision and display conditions are met for both participants.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-05](EN301549_AI_Test_Prompts.md#ai-en-05). Manual: Specialist validates exact subclauses, endpoint support and user experience.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-06

**Real-time text interoperability and latency** · Guide §10.12; interoperability and responsiveness; EN 6.2.3(a–d), 6.2.4 · Groups: DH LH NS

**Procedure**

1. Select the applicable interoperability and timing conditions.
2. Exchange timestamped text between supported protocol/device combinations.
3. Measure delay, losses and character integrity rather than inferring from marketing claims.

**Expected:** Applicable interoperability and responsiveness conditions are evidenced.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-06](EN301549_AI_Test_Prompts.md#ai-en-06). Manual: Specialist checks endpoint matrices, clock synchronisation and clause thresholds.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-07

**Caller identification and voice-service alternatives** · Guide §10.12; caller information; EN 6.3, 6.4 · Groups: DH LH NS NV

**Procedure**

1. Exercise caller identity on offered call functions.
2. Inspect accessible presentation and permitted voice-service alternatives.
3. Complete an approved test call using relevant non-speech routes.

**Expected:** Caller information and alternatives satisfy the selected conditional requirements.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-07](EN301549_AI_Test_Prompts.md#ai-en-07). Manual: Human AT and communication review; an informational site need not add a calling service solely for this test.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-08

**Video quality and audiovisual synchronisation** · Guide §10.12; video communication conditions; EN 6.5.2–6.5.4 · Groups: DH LH NS CL

**Procedure**

1. Use timestamped video/audio fixtures and supported endpoints.
2. Measure relevant resolution, frame rate and audiovisual offset.
3. Record network settings and conditions for each selected clause.

**Expected:** Applicable video communication quality and synchronisation conditions are met.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-08](EN301549_AI_Test_Prompts.md#ai-en-08). Manual: Specialist measurement and sign-language/lipreading review where relevant.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-09

**Audio activity speaker identity and video alternatives** · Guide §10.12; communication indicators; EN 6.5.5–6.5.6; any additional 6.6 commitment separately · Groups: DH LH NS NV

**Procedure**

1. In an approved multiparty fixture activate audio and change speakers.
2. Inspect applicable activity/identity indicators and their accessible exposure.
3. Test any required alternative to video-based services.

**Expected:** Applicable communication indicators and alternatives are available and usable.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-09](EN301549_AI_Test_Prompts.md#ai-en-09). Manual: Human checks indicator meaning and actual communication experience against selected clauses.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-10

**Caption playback synchronisation preservation and presentation** · Guide §10.7 and §10.10; media access features; EN 7.1.1–7.1.4 · Groups: DH LH CL

**Procedure**

1. Use captioned fixtures through player, transport and conversion paths.
2. Measure cue timing, switching and preservation of supported caption information.
3. Exercise caption presentation features required by selected clauses.

**Expected:** Applicable caption processing, presentation and preservation conditions are met.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-10](EN301549_AI_Test_Prompts.md#ai-en-10). Manual: Human checks readability and full playback; separately establish whether spoken-subtitle conditions apply.

**QA relationship:** CTL-181, CTL-183. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-11

**Audio-description playback synchronisation and preservation** · Guide §10.7 and §10.10; media access features; EN 7.2.1–7.2.3 · Groups: NV LV

**Procedure**

1. Play known described fixtures through supported paths.
2. Select the description and measure event alignment.
3. Compare description availability before/after transport or processing.

**Expected:** Applicable description playback, alignment and preservation conditions are met.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-11](EN301549_AI_Test_Prompts.md#ai-en-11). Manual: Human listens for mixing, timing and lost content; does not establish editorial sufficiency by metadata alone.

**QA relationship:** CTL-181, CTL-184. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-12

**Caption and description activation controls** · Guide §10.7 and §10.10; media controls; EN 7.3 · Groups: NV LV DH LH MS

**Procedure**

1. Locate controls for caption and description activation.
2. Operate using keyboard/AT and compare access with primary playback controls.
3. Record all steps and control exposure against selected conditions.

**Expected:** Required access-feature controls can be located and operated accessibly under applicable conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-12](EN301549_AI_Test_Prompts.md#ai-en-12). Manual: Human verifies actual AT output and comparative access effort.

**QA relationship:** CTL-091, CTL-092, CTL-181. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-13

**Platform services AT interoperability and user control** · Guide §10.13; software accessibility services; EN 11.5–11.6, subject to Table A.2 selections · Groups: NV LV MS CL

**Procedure**

1. Inventory platform accessibility APIs, custom UI and relevant accessibility settings.
2. Inspect exposed actions/text/state and preference controls.
3. Run configured AT interoperability scenarios and record unsupported services.

**Expected:** Applicable software interoperability and control conditions have evidence.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-13](EN301549_AI_Test_Prompts.md#ai-en-13). Manual: Native software specialist must expand exact Clause 11 subclauses; CTL mappings are partial only.

**QA relationship:** CTL-071, CTL-107, CTL-157. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-14

**Respect applicable user preferences** · Guide §10.13; user preferences; EN 11.7 · Groups: NV LV CP CL MH

**Procedure**

1. Apply supported contrast, colour, font and other relevant preferences one at a time and combined.
2. Compare content and task results.
3. Record which settings and exact conditional clauses were tested.

**Expected:** Relevant platform/user preferences are honoured under applicable conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-14](EN301549_AI_Test_Prompts.md#ai-en-14). Manual: Human verifies necessary exceptions and combined settings; reduced-motion support alone is not universal WAD proof.

**QA relationship:** CTL-014, CTL-019, CTL-022. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-15

**Accessible content production repair and templates** · Guide §10.13; authoring tools; EN 11.8.1–11.8.5 · Groups: NV LV DH CL

**Procedure**

1. Inventory offered authoring functions, transformations, checking/repair and templates.
2. Create representative content and deliberately include repairable barriers.
3. Export outputs and verify applicable authoring support and accessible templates.

**Expected:** Offered authoring tools meet applicable support-for-accessible-content conditions.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-15](EN301549_AI_Test_Prompts.md#ai-en-15). Manual: Authoring/document specialist expands and judges exact Clause 11 conditions; no existing exact CTL test.

**QA relationship:** QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-16

**Accessible feature and compatibility documentation** · Guide §10.13; documentation; EN 12.1.1–12.1.2 · Groups: NV LV DH LH CL

**Procedure**

1. Inventory documentation for accessibility features, compatibility and use.
2. Check completeness against implemented features.
3. Apply web/document tests to its actual format.

**Expected:** Required documentation describes relevant accessibility/compatibility features and is itself accessible.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-EN-16](EN301549_AI_Test_Prompts.md#ai-en-16). Manual: Human checks completeness, accuracy and practical usability.

**QA relationship:** QA-MGMT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-17

**Accessible support information and communication** · Guide §10.13; support; EN 12.2.2–12.2.4 · Groups: NV DH LH NS CL

**Procedure**

1. Inspect support descriptions and access channels.
2. Review authorised sandbox support records against published accessibility information.
3. Check whether supplied alternatives and answers are usable.

**Expected:** Applicable support information and communication conditions are satisfied.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-EN-17](EN301549_AI_Test_Prompts.md#ai-en-17). Manual: Human reviews actual communication and alternatives; do not contact staff without explicit sending authorisation.

**QA relationship:** QA-MGMT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### EN-18

**Spoken-subtitle processing where applicable** · Guide §§10.7 and 10.10; selected caption-processing conditions; EN 7.1.5 · Groups: NV LV CL

**Procedure**

1. Identify whether selected Annex A clauses require spoken-subtitle capability for this function.
2. With an authorised known fixture activate the supported spoken-subtitle path.
3. Record availability, playback, content and relevant settings against the selected condition.

**Expected:** Applicable spoken-subtitle processing has direct playback evidence.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI execution of stated observable subset; [AI-EN-18](EN301549_AI_Test_Prompts.md#ai-en-18). Manual: Media/EN specialist determines exact applicability and listens to the actual output.

**QA relationship:** CTL-181. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-01

**Public body national law and service scope** · Guide §§3–4; Articles 1–3 · Groups: ALL

**Procedure**

1. Inspect entity evidence, jurisdiction and supplied national-law register.
2. List domains, portals, apps, platforms, documents, media and supplier integrations.
3. Flag unsupported scope decisions.

**Expected:** Scope and responsibility have a reasoned, documented basis.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-01](EN301549_AI_Test_Prompts.md#ai-scope-01). Manual: Public body/legal reviewer decides scope; outsourcing does not remove accountability.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-02

**Public service broadcasting exclusion** · Guide §5.1; Article 1(3) · Groups: ALL

**Procedure**

1. Inspect claimed broadcasting remit and exact assets.
2. Compare claim with the guide's broadcasting categories.
3. List missing evidence and other-duty referrals.

**Expected:** Only qualifying assets are assigned this exclusion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-02](EN301549_AI_Test_Prompts.md#ai-scope-02). Manual: Legal reviewer confirms remit and scope.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-03

**NGO exclusion conditions** · Guide §5.2; Article 1(3) · Groups: ALL

**Procedure**

1. Review evidence of essential public services and services addressing disabled people.
2. Compare both conditions with the exclusion claim.
3. Record organisational scope separately.

**Expected:** Charitable/NGO status alone is not used as an exclusion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-03](EN301549_AI_Test_Prompts.md#ai-scope-03). Manual: Legal reviewer applies entity and service definitions.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-04

**Schools and essential administrative functions** · Guide §5.3; Article 1(5) · Groups: ALL

**Procedure**

1. Inspect national use of the school option.
2. Inventory essential online administrative functions.
3. Check exclusions do not hide those functions or extend automatically to universities.

**Expected:** Only nationally permitted exclusions are used; essential administrative functions remain assessed.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-04](EN301549_AI_Test_Prompts.md#ai-scope-04). Manual: Legal reviewer approves national option and essential-function decisions.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-05

**Older office documents** · Guide §5.4; Article 1(4) · Groups: ALL

**Procedure**

1. Inspect publication evidence for files claimed older than 23 September 2018.
2. Check whether each is needed by an active administrative process.
3. Flag creation-date-only evidence.

**Expected:** Only documents meeting both applicable date and active-process conditions are excluded.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-05](EN301549_AI_Test_Prompts.md#ai-scope-05). Manual: Reviewer confirms current administrative use and provenance.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-06

**Older prerecorded and live media** · Guide §§5.5–5.6; Article 1(4) · Groups: NV DH LH

**Procedure**

1. Separate publication dates, live streams and retained recordings.
2. Compare prerecorded claims with 23 September 2020.
3. Flag live recordings awaiting assessment and misuse of a universal 14-day exemption.

**Expected:** Each asset has a supported media-scope decision; players/surrounding pages remain separately assessed.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-06](EN301549_AI_Test_Prompts.md#ai-scope-06). Manual: Legal/content reviewer decides scope and national treatment of retained recordings.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-07

**Navigation maps essential information** · Guide §5.7; Article 1(4) · Groups: NV LV MS CL

**Procedure**

1. Identify maps used for navigation.
2. Locate accessible destination, address and necessary directions.
3. Run the navigation-information task without the map visual.

**Expected:** Essential navigation information is available accessibly when the map exclusion is used.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-07](EN301549_AI_Test_Prompts.md#ai-scope-07). Manual: Human checks completeness and actual wayfinding task; exclusion is not a technical map pass.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-08

**Third-party funding development and control** · Guide §5.8; Article 1(4) · Groups: ALL

**Procedure**

1. Inspect contracts and actual funding/development/control for claimed third-party exclusions.
2. Compare each limb separately.
3. Flag purchased or embedded components excluded by label alone.

**Expected:** Only content satisfying all applicable exclusion conditions is assigned this exclusion.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-08](EN301549_AI_Test_Prompts.md#ai-scope-08). Manual: Public body/legal reviewer determines actual control and responsibility.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-09

**Heritage reproductions and metadata** · Guide §5.9; Article 1(4) · Groups: NV LV CL

**Procedure**

1. Review item-specific preservation/authenticity or extraction evidence.
2. Separate reproduction from surrounding metadata.
3. Identify assessable associated information.

**Expected:** Exclusion is limited to justified reproduction conditions; associated metadata remains considered.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-09](EN301549_AI_Test_Prompts.md#ai-scope-09). Manual: Heritage and legal specialist validates reasons and feasible accessibility.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-10

**Older intranet and extranet content** · Guide §§4.4 and 5.10; Article 1(4) · Groups: ALL

**Procedure**

1. Check pre-23 September 2019 publication evidence.
2. Inspect substantial-revision records and national guidance.
3. Flag unsupported revision thresholds.

**Expected:** Only qualifying content retains this exclusion until substantial revision.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-10](EN301549_AI_Test_Prompts.md#ai-scope-10). Manual: Human/legal review defines substantial revision; no invented universal numeric threshold.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-11

**Archive conditions** · Guide §5.11; Article 1(4) · Groups: ALL

**Procedure**

1. Inspect update/edit history after 23 September 2019.
2. Check active administrative-process dependencies.
3. Distinguish technical maintenance from editorial updates.

**Expected:** Archive exclusions require both inactive administrative use and qualifying update history.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-11](EN301549_AI_Test_Prompts.md#ai-scope-11). Manual: Reviewer confirms service boundaries and evidence.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### SCOPE-12

**Disproportionate burden record** · Guide §6; Article 5 · Groups: ALL

**Procedure**

1. Inspect exact unmet requirements, resource/cost/benefit evidence and options.
2. Check alternatives, statement references, owner and review triggers.
3. Flag priority/time/knowledge-only reasons or imported EAA exceptions.

**Expected:** A reasoned requirement-specific assessment is distinct from technical status.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-SCOPE-12](EN301549_AI_Test_Prompts.md#ai-scope-12). Manual: Human accountable/legal authority decides burden; AI cannot approve it.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-01

**Declared technical and legal baseline** · Guide §9; Article 6 · Groups: ALL

**Procedure**

1. Inspect recorded harmonised version, Annex A table and country-specific additions.
2. Compare WCAG 2.1 legal mapping with WCAG 2.2 delivery commitments.
3. Flag version drift and claims that publication alone changes legal citation.

**Expected:** Every assessment declares its baseline and additions separately.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-01](EN301549_AI_Test_Prompts.md#ai-gov-01). Manual: Reviewer verifies current Official Journal/national reference before any conformity claim.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-02

**Clause-level applicability register** · Guide §§10.10 and 11.2 · Groups: ALL

**Procedure**

1. Inventory actual functions.
2. Check each applicable Annex A clause/subclause has conditions, method and status.
3. List missing clauses instead of treating broad category coverage as completion.

**Expected:** All relevant Annex A requirements have documented applicability and assessment records.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-02](EN301549_AI_Test_Prompts.md#ai-gov-02). Manual: EN specialist expands conditional clause families before audit sign-off.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-03

**Representative sample and complete processes** · Guide §11.3 · Groups: ALL

**Procedure**

1. Compare asset inventory with home, login, search, help, legal, statement, media, documents and state coverage.
2. Trace each selected process from entry through confirmation/error/recovery.
3. Flag unsupported service-wide extrapolation.

**Expected:** Samples cover meaningful variation and complete selected journeys with stated limits.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-03](EN301549_AI_Test_Prompts.md#ai-gov-03). Manual: Reviewer approves sample and expansion on systemic findings.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-04

**Layered test methods and AT coverage** · Guide §11.4 · Groups: ALL

**Procedure**

1. Inspect test records by requirement and environment.
2. Separate automated scans, keyboard, visual/content, AT and user evaluation.
3. List missing methods and unexecuted states.

**Expected:** Evidence uses appropriate complementary methods rather than a scan-only claim.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-04](EN301549_AI_Test_Prompts.md#ai-gov-04). Manual: Accessibility lead reviews sufficiency and resolves conflicting results.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-05

**Real user outcomes and equivalent task completion** · Guide §§1 and 11.5 · Groups: ALL

**Procedure**

1. Record externally observed completion, comprehension, help, errors, recovery, time/effort, confidence and satisfaction with relevant disabled participants.

**Expected:** People can complete meaningful tasks and understand decisions; differences and barriers are recorded.

**Evidence:** Direct participant observations and consented research records; retain completion, understanding, errors, help, effort and satisfaction by relevant functional need.

**Methods:** AXE: No coverage assigned. AI: Manual only; —. Manual: Manual user research only; agent simulation cannot establish participant experience.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-06

**Traceable evidence honest status and privacy** · Guide §§11.6–11.10 · Groups: ALL

**Procedure**

1. Validate each record for requirement, task, build, environment, method, actual/expected result and evidence.
2. Separate applicability, technical, user-experience and operational conclusions.
3. Flag invented passes, absent retests, missing limits and unnecessary health data.

**Expected:** Results are traceable and uncertainty and personal data are handled accurately.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-06](EN301549_AI_Test_Prompts.md#ai-gov-06). Manual: Reviewer checks evidence adequacy, retention and factual accuracy.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-07

**Statement location format and identification** · Guide §§13.1–13.2; Article 7 and Decision 2018/1523 · Groups: ALL

**Procedure**

1. Locate website statement or app website/download route.
2. Check public body, law, asset/version scope and accessible format.
3. Apply relevant web/document tests to the statement itself.

**Expected:** Statement is available in the required location and identifies its actual scope.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-07](EN301549_AI_Test_Prompts.md#ai-gov-07). Manual: Human confirms legal details and actual accessibility.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-08

**Statement content and evidence accuracy** · Guide §§13.2–13.5 · Groups: ALL

**Procedure**

1. Compare statement status and inaccessible content with the requirement register.
2. Check reasons, alternatives, preparation date, assessment method, contact and enforcement.
3. Flag unsupported full-compliance claims and numerical status thresholds.

**Expected:** Statement accurately describes known assessed conditions using the required model.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-08](EN301549_AI_Test_Prompts.md#ai-gov-08). Manual: Accountable human approves legal/compliance assertions and publication.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-09

**Regular statement review** · Guide §13.6 · Groups: ALL

**Procedure**

1. Compare statement review date with substantial changes and known findings.
2. Inspect assigned review owner and applicable national schedule.
3. Separate EU model annual recommendation from national mandatory rules.

**Expected:** Statement is maintained accurately under applicable review duties.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-09](EN301549_AI_Test_Prompts.md#ai-gov-09). Manual: Human decides necessary changes and approvals.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-10

**Feedback access and requests for excluded/burden information** · Guide §14; Article 7(1) · Groups: ALL

**Procedure**

1. Inspect feedback links and form/contact instructions.
2. In sandbox complete requests for an accessibility failure and for excluded/burden information.
3. Exercise keyboard, error and confirmation paths.

**Expected:** Anyone can report failures and request covered categories of information through an accessible mechanism.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-10](EN301549_AI_Test_Prompts.md#ai-gov-10). Manual: Human checks actual AT use; external sending requires explicit authorisation.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-11

**Feedback routing response and alternatives** · Guide §14; Article 7(1) · Groups: ALL

**Procedure**

1. Review authorised sandbox requests or supplied redacted logs.
2. Compare receipt, responsible team, response, alternative usability and escalation with published/national expectations.
3. Flag unmonitored addresses and invented EU response deadlines.

**Expected:** Requests reach accountable teams and receive adequate timely responses and usable alternatives.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-11](EN301549_AI_Test_Prompts.md#ai-gov-11). Manual: Human judges adequacy and any live service test; no real messages without sending authorisation.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-12

**Enforcement and unsatisfactory response** · Guide §18; Article 9 · Groups: ALL

**Procedure**

1. Inspect statement escalation link and named body against supplied jurisdiction records.
2. Verify the route is reachable and instructions usable.
3. Check record availability for review of duties and burden decisions.

**Expected:** Users can find the relevant effective enforcement route.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-12](EN301549_AI_Test_Prompts.md#ai-gov-12). Manual: Human validates national authority and procedure; no complaint is submitted by this test.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-13

**National simplified and in-depth monitoring methods** · Guide §§15.1–15.2; Article 8 and Decision 2018/1524 · Groups: ALL

**Procedure**

1. Where acting as monitoring body inspect methodology for all four principles and functional needs.
2. Separate simplified failure detection from in-depth applicable-requirement/process assessment.
3. Check transparent reproducible records.

**Expected:** Monitoring methods satisfy their respective scope; a clean simplified scan is not full compliance.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-13](EN301549_AI_Test_Prompts.md#ai-gov-13). Manual: Monitoring authority validates method; these are national duties.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-14

**National sample composition and page selection** · Guide §§15.3–15.4; Decision 2018/1524 · Groups: ALL

**Procedure**

1. For national monitoring review population-based sample calculations and service/region coverage.
2. Check stakeholder consultation, OS/version distinctions, repeat/new samples and structured/random page selection.
3. Verify required random pages reach at least 10 percent of the specified structured sample and all process steps are included.

**Expected:** National samples follow applicable decision rules and recorded selection methods.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-14](EN301549_AI_Test_Prompts.md#ai-gov-14). Manual: Monitoring authority confirms exact calculations; no internal public-body page quota is inferred.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-15

**National reporting and useful corrective findings** · Guide §15.5; Article 8 · Groups: ALL

**Procedure**

1. Review monitoring outputs for reproducible findings and correction information.
2. Check applicable three-year reporting schedule and accessible publication.
3. Keep national reporting separate from ongoing service correction.

**Expected:** National reports meet applicable cycle and accessibility duties; bodies can act on findings.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-15](EN301549_AI_Test_Prompts.md#ai-gov-15). Manual: Monitoring authority approves reports and publication.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-16

**Supplier evidence and accountable ownership** · Guide §16 · Groups: ALL

**Procedure**

1. Compare vendor report build/configuration with deployed integrations.
2. Inspect requirement mappings, known issues, correction owners and deadlines.
3. Trace one integration defect through corrective responsibility and retest.

**Expected:** Public body ownership and supplier evidence cover actual deployed service.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-16](EN301549_AI_Test_Prompts.md#ai-gov-16). Manual: Accountable procurement/service owners decide duties; declaration alone is insufficient.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-17

**Training awareness and accessible delivery controls** · Guide §17; Article 7(4)–(5) · Groups: ALL

**Procedure**

1. Inspect relevant training/awareness records and feedback-route communications.
2. Trace accessibility controls through design, content, CMS, engineering and procurement.
3. Separate national promotion duties from recommended internal controls.

**Expected:** Relevant training/awareness obligations and adopted delivery controls have evidence.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-17](EN301549_AI_Test_Prompts.md#ai-gov-17). Manual: Human evaluates duty holder and control effectiveness; attendance is not proof of competence.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

### GOV-18

**Regression correction and change review** · Guide §17; Article 4 and Article 7(1) · Groups: ALL

**Procedure**

1. Compare code/content/platform changes with retests and known defects.
2. Re-run affected tests on approved builds.
3. Check owners, user-impact priorities, review triggers and statement consistency.

**Expected:** Changes are assessed, failures tracked and evidence/statements kept current.

**Evidence:** Record the exact fixture/asset, tested state, step log, before/after observations, relevant measurements or extracted properties, and unresolved conditions. Preserve original tool output where used.

**Methods:** AXE: No coverage assigned. AI: AI-assisted analysis/evidence only; [AI-GOV-18](EN301549_AI_Test_Prompts.md#ai-gov-18). Manual: Human release/service decision; prioritisation does not convert failure into pass.

**QA relationship:** QA-MGMT, QA-AGENT. Supporting behavioural/process relationship only; this does not establish an exact EN subclause equivalent.

## Existing QA test index and reverse mapping

For every referenced CTL test this index preserves its name and shows the exact new tests/prompts supplying the assessed subset. Classifications apply to the linked procedures, not automatically to every word of the broader canonical requirement. Follow every linked prompt needed for the selected requirement, and complete its manual review.

| QA ID | Exact canonical title | Mapped procedures | AXE candidate subset | AI classes | Prompts | Manual |
| --- | --- | --- | --- | --- | --- | --- |
| CTL-001 | Information Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141) | No coverage assigned | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141) | Required for full outcome |
| CTL-002 | Error States Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141), [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331) | No coverage assigned | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141), [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331) | Required for full outcome |
| CTL-003 | Required States Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | label | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-004 | Selection State Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141) | No coverage assigned | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141) | Required for full outcome |
| CTL-005 | Focus State Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141), [WEB-247](EN301549_Requirements_Test_Matrix.md#web-247) | No coverage assigned | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141), [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247) | Required for full outcome |
| CTL-006 | Link Identification Not Conveyed by Colour Alone | [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141) | No coverage assigned | E | [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141) | Required for full outcome |
| CTL-007 | Data Series Not Differentiated Only by Colour | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [WEB-141](EN301549_Requirements_Test_Matrix.md#web-141) | area-alt, image-alt, input-image-alt, object-alt | A, E | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-WEB-141](EN301549_AI_Test_Prompts.md#ai-web-141) | Required for full outcome |
| CTL-008 | Text Contrast Minimum | [WEB-143](EN301549_Requirements_Test_Matrix.md#web-143), [DOC-03](EN301549_Requirements_Test_Matrix.md#doc-03) | color-contrast | E | [AI-WEB-143](EN301549_AI_Test_Prompts.md#ai-web-143), [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03) | Required for full outcome |
| CTL-009 | Large Text Contrast Minimum | [WEB-143](EN301549_Requirements_Test_Matrix.md#web-143), [DOC-03](EN301549_Requirements_Test_Matrix.md#doc-03) | color-contrast | E | [AI-WEB-143](EN301549_AI_Test_Prompts.md#ai-web-143), [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03) | Required for full outcome |
| CTL-011 | Control Boundary Contrast | [WEB-1411](EN301549_Requirements_Test_Matrix.md#web-1411) | No coverage assigned | E | [AI-WEB-1411](EN301549_AI_Test_Prompts.md#ai-web-1411) | Required for full outcome |
| CTL-012 | Placeholder Contrast Adequacy | [WEB-143](EN301549_Requirements_Test_Matrix.md#web-143) | color-contrast | E | [AI-WEB-143](EN301549_AI_Test_Prompts.md#ai-web-143) | Required for full outcome |
| CTL-014 | Text Resizes to 200 Percent | [WEB-144](EN301549_Requirements_Test_Matrix.md#web-144), [DOC-03](EN301549_Requirements_Test_Matrix.md#doc-03), [APP-03](EN301549_Requirements_Test_Matrix.md#app-03), [EN-14](EN301549_Requirements_Test_Matrix.md#en-14) | No coverage assigned | E | [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144), [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03), [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03), [AI-EN-14](EN301549_AI_Test_Prompts.md#ai-en-14) | Required for full outcome |
| CTL-015 | Text Resizes Beyond 200 Percent Where Supported | [WEB-144](EN301549_Requirements_Test_Matrix.md#web-144), [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410) | No coverage assigned | E | [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144), [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Required for full outcome |
| CTL-016 | Layout Reflows Without Horizontal Dependency | [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410) | No coverage assigned | E | [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Required for full outcome |
| CTL-017 | No Text Clipping on Resize | [WEB-144](EN301549_Requirements_Test_Matrix.md#web-144), [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410), [DOC-03](EN301549_Requirements_Test_Matrix.md#doc-03), [APP-03](EN301549_Requirements_Test_Matrix.md#app-03) | No coverage assigned | E | [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144), [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410), [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03), [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03) | Required for full outcome |
| CTL-018 | No Functional Loss on Resize | [WEB-144](EN301549_Requirements_Test_Matrix.md#web-144), [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410), [APP-03](EN301549_Requirements_Test_Matrix.md#app-03) | No coverage assigned | E | [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144), [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410), [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03) | Required for full outcome |
| CTL-019 | Text Spacing Override Support | [WEB-1412](EN301549_Requirements_Test_Matrix.md#web-1412), [DOC-03](EN301549_Requirements_Test_Matrix.md#doc-03), [EN-14](EN301549_Requirements_Test_Matrix.md#en-14) | No coverage assigned | E | [AI-WEB-1412](EN301549_AI_Test_Prompts.md#ai-web-1412), [AI-DOC-03](EN301549_AI_Test_Prompts.md#ai-doc-03), [AI-EN-14](EN301549_AI_Test_Prompts.md#ai-en-14) | Required for full outcome |
| CTL-020 | Zoom Capability Preserved | [WEB-144](EN301549_Requirements_Test_Matrix.md#web-144), [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410) | No coverage assigned | E | [AI-WEB-144](EN301549_AI_Test_Prompts.md#ai-web-144), [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Required for full outcome |
| CTL-022 | Motion Respects Reduced Motion Preference | [EN-14](EN301549_Requirements_Test_Matrix.md#en-14) | No coverage assigned | E | [AI-EN-14](EN301549_AI_Test_Prompts.md#ai-en-14) | Required for full outcome |
| CTL-023 | Auto-Moving Content Can Be Paused | [WEB-222](EN301549_Requirements_Test_Matrix.md#web-222) | blink | E | [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Required for full outcome |
| CTL-024 | Auto-Moving Content Can Be Stopped or Hidden | [WEB-222](EN301549_Requirements_Test_Matrix.md#web-222) | blink | E | [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Required for full outcome |
| CTL-026 | Flashing Content Frequency Safety | [WEB-231](EN301549_Requirements_Test_Matrix.md#web-231) | No coverage assigned | E | [AI-WEB-231](EN301549_AI_Test_Prompts.md#ai-web-231) | Required for full outcome |
| CTL-028 | Autoplay Audio Control | [WEB-142](EN301549_Requirements_Test_Matrix.md#web-142), [WEB-222](EN301549_Requirements_Test_Matrix.md#web-222) | blink, no-autoplay-audio | E | [AI-WEB-142](EN301549_AI_Test_Prompts.md#ai-web-142), [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Required for full outcome |
| CTL-029 | Autoplay Video Control | [WEB-222](EN301549_Requirements_Test_Matrix.md#web-222) | blink | E | [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Required for full outcome |
| CTL-030 | Media Does Not Mask Assistive Technology Audio | [WEB-142](EN301549_Requirements_Test_Matrix.md#web-142) | no-autoplay-audio | E | [AI-WEB-142](EN301549_AI_Test_Prompts.md#ai-web-142) | Required for full outcome |
| CTL-033 | Decorative Images Ignored by Assistive Technology | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Required for full outcome |
| CTL-034 | Informative Images Have Equivalent Text | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01), [EN-03](EN301549_Requirements_Test_Matrix.md#en-03) | area-alt, image-alt, input-image-alt, object-alt | A, E | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01), [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03) | Required for full outcome |
| CTL-035 | Functional Images Describe Action | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01) | area-alt, aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, image-alt, input-button-name, input-image-alt, label, object-alt | A, E | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Required for full outcome |
| CTL-036 | Complex Visuals Have Summary | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Required for full outcome |
| CTL-037 | Images of Text Avoided | [WEB-145](EN301549_Requirements_Test_Matrix.md#web-145) | No coverage assigned | A | [AI-WEB-145](EN301549_AI_Test_Prompts.md#ai-web-145) | Required for full outcome |
| CTL-038 | Background Images with Meaning Have Equivalent Content | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111) | Required for full outcome |
| CTL-039 | Visible Rating or Graphic Indicators Have Text Equivalent | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111) | Required for full outcome |
| CTL-040 | Supplementary Visual Cues Do Not Replace Meaningful Text | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111), [WEB-133](EN301549_Requirements_Test_Matrix.md#web-133) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111), [AI-WEB-133](EN301549_AI_Test_Prompts.md#ai-web-133) | Required for full outcome |
| CTL-041 | Primary Page Language Declared | [WEB-311](EN301549_Requirements_Test_Matrix.md#web-311), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01) | html-has-lang, html-lang-valid | A | [AI-WEB-311](EN301549_AI_Test_Prompts.md#ai-web-311), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Required for full outcome |
| CTL-042 | Inline Language Changes Marked | [WEB-312](EN301549_Requirements_Test_Matrix.md#web-312), [DOC-01](EN301549_Requirements_Test_Matrix.md#doc-01) | valid-lang | A | [AI-WEB-312](EN301549_AI_Test_Prompts.md#ai-web-312), [AI-DOC-01](EN301549_AI_Test_Prompts.md#ai-doc-01) | Required for full outcome |
| CTL-044 | Page Title Present | [WEB-242](EN301549_Requirements_Test_Matrix.md#web-242) | document-title | E | [AI-WEB-242](EN301549_AI_Test_Prompts.md#ai-web-242) | Required for full outcome |
| CTL-045 | Page Title Describes Primary Content | [WEB-242](EN301549_Requirements_Test_Matrix.md#web-242) | document-title | E | [AI-WEB-242](EN301549_AI_Test_Prompts.md#ai-web-242) | Required for full outcome |
| CTL-047 | SPA Title Updates on Route Change | [WEB-242](EN301549_Requirements_Test_Matrix.md#web-242), [WEB-323](EN301549_Requirements_Test_Matrix.md#web-323) | document-title | E | [AI-WEB-242](EN301549_AI_Test_Prompts.md#ai-web-242), [AI-WEB-323](EN301549_AI_Test_Prompts.md#ai-web-323) | Required for full outcome |
| CTL-052 | Skip Link or Equivalent Bypass Present | [WEB-241](EN301549_Requirements_Test_Matrix.md#web-241) | bypass | E | [AI-WEB-241](EN301549_AI_Test_Prompts.md#ai-web-241) | Required for full outcome |
| CTL-053 | Skip Link Focuses Main Content Reliably | [WEB-241](EN301549_Requirements_Test_Matrix.md#web-241), [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | bypass | E | [AI-WEB-241](EN301549_AI_Test_Prompts.md#ai-web-241), [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-054 | Heading Structure Present | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-246](EN301549_Requirements_Test_Matrix.md#web-246), [DOC-02](EN301549_Requirements_Test_Matrix.md#doc-02) | aria-required-children, aria-required-parent, definition-list | A, E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-246](EN301549_AI_Test_Prompts.md#ai-web-246), [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02) | Required for full outcome |
| CTL-056 | Heading Levels Follow Logical Hierarchy | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Required for full outcome |
| CTL-057 | Heading Text Is Descriptive | [WEB-246](EN301549_Requirements_Test_Matrix.md#web-246) | No coverage assigned | A | [AI-WEB-246](EN301549_AI_Test_Prompts.md#ai-web-246) | Required for full outcome |
| CTL-058 | Visual Headings Match Semantic Headings | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Required for full outcome |
| CTL-060 | Source Order Matches Intended Reading Order | [WEB-132](EN301549_Requirements_Test_Matrix.md#web-132), [DOC-02](EN301549_Requirements_Test_Matrix.md#doc-02), [APP-02](EN301549_Requirements_Test_Matrix.md#app-02), [EN-03](EN301549_Requirements_Test_Matrix.md#en-03) | No coverage assigned | A, E | [AI-WEB-132](EN301549_AI_Test_Prompts.md#ai-web-132), [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02), [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02), [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03) | Required for full outcome |
| CTL-061 | Tab Order Aligns With Logical Structure | [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243), [APP-02](EN301549_Requirements_Test_Matrix.md#app-02) | No coverage assigned | E | [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243), [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Required for full outcome |
| CTL-062 | CSS Reordering Does Not Break Meaning | [WEB-132](EN301549_Requirements_Test_Matrix.md#web-132), [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-132](EN301549_AI_Test_Prompts.md#ai-web-132), [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-063 | Related Thematic Items Use List Semantics | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [DOC-02](EN301549_Requirements_Test_Matrix.md#doc-02) | aria-required-children, aria-required-parent, definition-list | A, E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02) | Required for full outcome |
| CTL-066 | Data Tables Include Header Cells | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [DOC-02](EN301549_Requirements_Test_Matrix.md#doc-02), [EN-03](EN301549_Requirements_Test_Matrix.md#en-03) | aria-required-children, aria-required-parent, definition-list | A, E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02), [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03) | Required for full outcome |
| CTL-067 | Data Table Header Scope Defined | [DOC-02](EN301549_Requirements_Test_Matrix.md#doc-02) | No coverage assigned | A | [AI-DOC-02](EN301549_AI_Test_Prompts.md#ai-doc-02) | Required for full outcome |
| CTL-069 | Table Remains Structurally Intact on Small Screens | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Required for full outcome |
| CTL-070 | Scrollable Table Container Is Accessible | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-071 | Interactive Elements Have Accessible Names | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04), [APP-01](EN301549_Requirements_Test_Matrix.md#app-01), [EN-13](EN301549_Requirements_Test_Matrix.md#en-13) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04), [AI-APP-01](EN301549_AI_Test_Prompts.md#ai-app-01), [AI-EN-13](EN301549_AI_Test_Prompts.md#ai-en-13) | Required for full outcome |
| CTL-072 | Visible Labels Exist for Form Inputs | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04), [APP-04](EN301549_Requirements_Test_Matrix.md#app-04) | label | E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04), [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Required for full outcome |
| CTL-073 | Accessible Name Matches Visible Label | [WEB-253](EN301549_Requirements_Test_Matrix.md#web-253) | No coverage assigned | E | [AI-WEB-253](EN301549_AI_Test_Prompts.md#ai-web-253) | Required for full outcome |
| CTL-078 | Instructions Associated With Relevant Field | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332), [APP-04](EN301549_Requirements_Test_Matrix.md#app-04) | label | E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332), [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Required for full outcome |
| CTL-079 | Error Messages Associated With Relevant Field | [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04) | No coverage assigned | E | [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04) | Required for full outcome |
| CTL-080 | Group Labels for Related Controls | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | aria-required-children, aria-required-parent, definition-list, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-081 | Control Text Describes Purpose | [WEB-246](EN301549_Requirements_Test_Matrix.md#web-246), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | A, E | [AI-WEB-246](EN301549_AI_Test_Prompts.md#ai-web-246), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-082 | Icon-Only Controls Have Equivalent Text | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-088 | Metadata Values Clarified Non-Visually | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Required for full outcome |
| CTL-091 | All Interactive Elements Reachable by Keyboard | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04), [EN-01](EN301549_Requirements_Test_Matrix.md#en-01), [EN-12](EN301549_Requirements_Test_Matrix.md#en-12) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04), [AI-EN-01](EN301549_AI_Test_Prompts.md#ai-en-01), [AI-EN-12](EN301549_AI_Test_Prompts.md#ai-en-12) | Required for full outcome |
| CTL-092 | All Interactive Elements Operable by Keyboard | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04), [EN-01](EN301549_Requirements_Test_Matrix.md#en-01), [EN-12](EN301549_Requirements_Test_Matrix.md#en-12) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04), [AI-EN-01](EN301549_AI_Test_Prompts.md#ai-en-01), [AI-EN-12](EN301549_AI_Test_Prompts.md#ai-en-12) | Required for full outcome |
| CTL-093 | Standard Keyboard Activation Preserved | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211) | Required for full outcome |
| CTL-094 | No Keyboard Trap | [WEB-212](EN301549_Requirements_Test_Matrix.md#web-212) | No coverage assigned | E | [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212) | Required for full outcome |
| CTL-095 | Focus Indicator Always Visible | [WEB-247](EN301549_Requirements_Test_Matrix.md#web-247) | No coverage assigned | E | [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247) | Required for full outcome |
| CTL-096 | Focus Indicator Not Suppressed Without Equivalent | [WEB-247](EN301549_Requirements_Test_Matrix.md#web-247) | No coverage assigned | E | [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247) | Required for full outcome |
| CTL-097 | Focus Order Logical Through Forms | [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-098 | Focus Order Logical Through Navigation | [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-099 | Focus Does Not Move Unexpectedly During Input | [WEB-321](EN301549_Requirements_Test_Matrix.md#web-321), [WEB-322](EN301549_Requirements_Test_Matrix.md#web-322) | No coverage assigned | E | [AI-WEB-321](EN301549_AI_Test_Prompts.md#ai-web-321), [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322) | Required for full outcome |
| CTL-100 | Focus Moves to New Context on Open | [APP-02](EN301549_Requirements_Test_Matrix.md#app-02) | No coverage assigned | E | [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Required for full outcome |
| CTL-101 | Focus Returns on Close | [APP-02](EN301549_Requirements_Test_Matrix.md#app-02) | No coverage assigned | E | [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Required for full outcome |
| CTL-103 | Hidden Focusable Elements Revealed on Focus | [WEB-247](EN301549_Requirements_Test_Matrix.md#web-247) | No coverage assigned | E | [AI-WEB-247](EN301549_AI_Test_Prompts.md#ai-web-247) | Required for full outcome |
| CTL-107 | Alternative Input Method Support | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [APP-03](EN301549_Requirements_Test_Matrix.md#app-03), [EN-01](EN301549_Requirements_Test_Matrix.md#en-01), [EN-02](EN301549_Requirements_Test_Matrix.md#en-02), [EN-13](EN301549_Requirements_Test_Matrix.md#en-13) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03), [AI-EN-01](EN301549_AI_Test_Prompts.md#ai-en-01), [AI-EN-02](EN301549_AI_Test_Prompts.md#ai-en-02), [AI-EN-13](EN301549_AI_Test_Prompts.md#ai-en-13) | Required for full outcome |
| CTL-108 | Gesture Functions Have Non-Gesture Alternatives | [WEB-251](EN301549_Requirements_Test_Matrix.md#web-251), [APP-03](EN301549_Requirements_Test_Matrix.md#app-03) | No coverage assigned | E | [AI-WEB-251](EN301549_AI_Test_Prompts.md#ai-web-251), [AI-APP-03](EN301549_AI_Test_Prompts.md#ai-app-03) | Required for full outcome |
| CTL-109 | Pointer Precision Not Required for Basic Tasks | [WEB-251](EN301549_Requirements_Test_Matrix.md#web-251) | No coverage assigned | E | [AI-WEB-251](EN301549_AI_Test_Prompts.md#ai-web-251) | Required for full outcome |
| CTL-112 | Submission Occurs Only on Explicit Action | [WEB-322](EN301549_Requirements_Test_Matrix.md#web-322) | No coverage assigned | E | [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322) | Required for full outcome |
| CTL-113 | Required Fields Indicated Programmatically | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | aria-required-children, aria-required-parent, definition-list, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-114 | Required Fields Indicated Visually | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | label | E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-116 | Input Format Expectations Communicated | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | label | E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-118 | Autocomplete Used for Personal Data Where Appropriate | [WEB-135](EN301549_Requirements_Test_Matrix.md#web-135) | No coverage assigned | E | [AI-WEB-135](EN301549_AI_Test_Prompts.md#ai-web-135) | Required for full outcome |
| CTL-119 | Related Inputs Grouped Semantically | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | aria-required-children, aria-required-parent, definition-list, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-120 | Radio Groups Operate as One Logical Question | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | aria-required-children, aria-required-parent, definition-list, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-121 | Checkbox Sets Grouped Where They Share a Question | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | aria-required-children, aria-required-parent, definition-list, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-122 | Error Messages Shown When Submission Fails | [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331), [DOC-04](EN301549_Requirements_Test_Matrix.md#doc-04), [APP-04](EN301549_Requirements_Test_Matrix.md#app-04) | No coverage assigned | E | [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331), [AI-DOC-04](EN301549_AI_Test_Prompts.md#ai-doc-04), [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Required for full outcome |
| CTL-123 | Error Messages Are Announced to Assistive Technology | [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331), [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | E | [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331), [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-124 | Error Message Identifies the Relevant Field | [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331) | No coverage assigned | E | [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331) | Required for full outcome |
| CTL-125 | Error Message Explains the Problem | [WEB-331](EN301549_Requirements_Test_Matrix.md#web-331) | No coverage assigned | E | [AI-WEB-331](EN301549_AI_Test_Prompts.md#ai-web-331) | Required for full outcome |
| CTL-126 | Error Message Tells User How to Fix It | [WEB-333](EN301549_Requirements_Test_Matrix.md#web-333), [APP-04](EN301549_Requirements_Test_Matrix.md#app-04) | No coverage assigned | A, E | [AI-WEB-333](EN301549_AI_Test_Prompts.md#ai-web-333), [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Required for full outcome |
| CTL-133 | Form Completion Possible by Keyboard Only | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [APP-04](EN301549_Requirements_Test_Matrix.md#app-04) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-APP-04](EN301549_AI_Test_Prompts.md#ai-app-04) | Required for full outcome |
| CTL-134 | Password and Complex Input Assistance Available | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332), [WEB-333](EN301549_Requirements_Test_Matrix.md#web-333) | label | A, E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332), [AI-WEB-333](EN301549_AI_Test_Prompts.md#ai-web-333) | Required for full outcome |
| CTL-136 | Link Purpose Understandable in Isolation | [WEB-244](EN301549_Requirements_Test_Matrix.md#web-244) | area-alt, link-name | A | [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244) | Required for full outcome |
| CTL-137 | Repeated Link Text Distinguishable Where Destinations Differ | [WEB-244](EN301549_Requirements_Test_Matrix.md#web-244) | area-alt, link-name | A | [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244) | Required for full outcome |
| CTL-140 | Download or Alternate Format Links Identified | [WEB-244](EN301549_Requirements_Test_Matrix.md#web-244) | area-alt, link-name | A | [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244) | Required for full outcome |
| CTL-143 | Navigation Menus Use Correct Structural Semantics | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Required for full outcome |
| CTL-146 | Search Suggestions Announced Accessibly | [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | E | [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-147 | Share and Auxiliary Tool Clarity | [WEB-244](EN301549_Requirements_Test_Matrix.md#web-244), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | area-alt, aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label, link-name | A, E | [AI-WEB-244](EN301549_AI_Test_Prompts.md#ai-web-244), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-148 | SPA Route Changes Update Focus Position | [APP-02](EN301549_Requirements_Test_Matrix.md#app-02) | No coverage assigned | E | [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Required for full outcome |
| CTL-150 | Route Change Loading State Communicated | [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | E | [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-151 | Status Messages Announced Without Forced Focus Change | [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413), [APP-02](EN301549_Requirements_Test_Matrix.md#app-02) | No coverage assigned | E | [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413), [AI-APP-02](EN301549_AI_Test_Prompts.md#ai-app-02) | Required for full outcome |
| CTL-152 | Critical Alerts Perceivable in Multiple Modalities | [WEB-133](EN301549_Requirements_Test_Matrix.md#web-133), [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | A, E | [AI-WEB-133](EN301549_AI_Test_Prompts.md#ai-web-133), [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-156 | Focus Not Stolen by Non-Critical Updates | [WEB-321](EN301549_Requirements_Test_Matrix.md#web-321), [WEB-322](EN301549_Requirements_Test_Matrix.md#web-322) | No coverage assigned | E | [AI-WEB-321](EN301549_AI_Test_Prompts.md#ai-web-321), [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322) | Required for full outcome |
| CTL-157 | State Changes Reflected Programmatically | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412), [APP-01](EN301549_Requirements_Test_Matrix.md#app-01), [EN-13](EN301549_Requirements_Test_Matrix.md#en-13) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412), [AI-APP-01](EN301549_AI_Test_Prompts.md#ai-app-01), [AI-EN-13](EN301549_AI_Test_Prompts.md#ai-en-13) | Required for full outcome |
| CTL-158 | State Change Announced When It Matters | [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | E | [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-160 | Update Timing Allows Perception | [WEB-221](EN301549_Requirements_Test_Matrix.md#web-221), [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | meta-refresh | E | [AI-WEB-221](EN301549_AI_Test_Prompts.md#ai-web-221), [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-161 | Disclosure Controls Expose Expanded State | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412), [APP-01](EN301549_Requirements_Test_Matrix.md#app-01) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412), [AI-APP-01](EN301549_AI_Test_Prompts.md#ai-app-01) | Required for full outcome |
| CTL-163 | Collapsed Disclosure Content Removed Accessibly | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, definition-list, frame-title, input-button-name, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-164 | Revealed Content Follows Control Logically | [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-167 | Tabs Use Correct Roles When Enhanced | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-169 | Only Active Tab Panel Exposed | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, definition-list, frame-title, input-button-name, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-172 | Modal Dialog Announces Identity and Modality | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-173 | Modal Dialog Blocks Background Interaction | [WEB-212](EN301549_Requirements_Test_Matrix.md#web-212), [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212), [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-174 | Modal Dialog Has Accessible Close Method | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [WEB-212](EN301549_Requirements_Test_Matrix.md#web-212) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212) | Required for full outcome |
| CTL-175 | Modal Dialog Content Fits or Scrolls | [WEB-1410](EN301549_Requirements_Test_Matrix.md#web-1410) | No coverage assigned | E | [AI-WEB-1410](EN301549_AI_Test_Prompts.md#ai-web-1410) | Required for full outcome |
| CTL-176 | Action Dialog Uses Buttons vs Links Appropriately | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, definition-list, frame-title, input-button-name, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-177 | Mega Menu Trigger Uses Button Semantics | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-178 | Mega Menu Closes on Escape, Blur, or Outside Click | [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [WEB-212](EN301549_Requirements_Test_Matrix.md#web-212) | No coverage assigned | E | [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-WEB-212](EN301549_AI_Test_Prompts.md#ai-web-212) | Required for full outcome |
| CTL-181 | Native Media Controls or Accessible Equivalent Present | [WEB-121](EN301549_Requirements_Test_Matrix.md#web-121), [WEB-211](EN301549_Requirements_Test_Matrix.md#web-211), [EN-10](EN301549_Requirements_Test_Matrix.md#en-10), [EN-11](EN301549_Requirements_Test_Matrix.md#en-11), [EN-12](EN301549_Requirements_Test_Matrix.md#en-12), [EN-18](EN301549_Requirements_Test_Matrix.md#en-18) | No coverage assigned | A, E | [AI-WEB-121](EN301549_AI_Test_Prompts.md#ai-web-121), [AI-WEB-211](EN301549_AI_Test_Prompts.md#ai-web-211), [AI-EN-10](EN301549_AI_Test_Prompts.md#ai-en-10), [AI-EN-11](EN301549_AI_Test_Prompts.md#ai-en-11), [AI-EN-12](EN301549_AI_Test_Prompts.md#ai-en-12), [AI-EN-18](EN301549_AI_Test_Prompts.md#ai-en-18) | Required for full outcome |
| CTL-182 | Media Does Not Autoplay Unexpectedly | [WEB-142](EN301549_Requirements_Test_Matrix.md#web-142), [WEB-222](EN301549_Requirements_Test_Matrix.md#web-222) | blink, no-autoplay-audio | E | [AI-WEB-142](EN301549_AI_Test_Prompts.md#ai-web-142), [AI-WEB-222](EN301549_AI_Test_Prompts.md#ai-web-222) | Required for full outcome |
| CTL-183 | Captions Available for Spoken Video | [WEB-122](EN301549_Requirements_Test_Matrix.md#web-122), [DOC-05](EN301549_Requirements_Test_Matrix.md#doc-05), [EN-03](EN301549_Requirements_Test_Matrix.md#en-03), [EN-10](EN301549_Requirements_Test_Matrix.md#en-10) | video-caption | A, E | [AI-WEB-122](EN301549_AI_Test_Prompts.md#ai-web-122), [AI-DOC-05](EN301549_AI_Test_Prompts.md#ai-doc-05), [AI-EN-03](EN301549_AI_Test_Prompts.md#ai-en-03), [AI-EN-10](EN301549_AI_Test_Prompts.md#ai-en-10) | Required for full outcome |
| CTL-184 | Audio Description or Equivalent for Essential Visual Information | [WEB-123](EN301549_Requirements_Test_Matrix.md#web-123), [WEB-125](EN301549_Requirements_Test_Matrix.md#web-125), [DOC-05](EN301549_Requirements_Test_Matrix.md#doc-05), [EN-11](EN301549_Requirements_Test_Matrix.md#en-11) | No coverage assigned | A, E | [AI-WEB-123](EN301549_AI_Test_Prompts.md#ai-web-123), [AI-WEB-125](EN301549_AI_Test_Prompts.md#ai-web-125), [AI-DOC-05](EN301549_AI_Test_Prompts.md#ai-doc-05), [AI-EN-11](EN301549_AI_Test_Prompts.md#ai-en-11) | Required for full outcome |
| CTL-187 | Promo Media Indicators Explained Non-Visually | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111) | Required for full outcome |
| CTL-189 | Card Headline Comes First in Source Order | [WEB-132](EN301549_Requirements_Test_Matrix.md#web-132), [WEB-243](EN301549_Requirements_Test_Matrix.md#web-243) | No coverage assigned | E | [AI-WEB-132](EN301549_AI_Test_Prompts.md#ai-web-132), [AI-WEB-243](EN301549_AI_Test_Prompts.md#ai-web-243) | Required for full outcome |
| CTL-190 | Card Expandable Regions Follow Toggle State | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-191 | Comment Stream Uses Nested Structure for Replies | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131) | aria-required-children, aria-required-parent, definition-list | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131) | Required for full outcome |
| CTL-192 | Comment Submission Feedback Accessible | [WEB-413](EN301549_Requirements_Test_Matrix.md#web-413) | No coverage assigned | E | [AI-WEB-413](EN301549_AI_Test_Prompts.md#ai-web-413) | Required for full outcome |
| CTL-193 | Comment Controls Clearly Labelled | [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, frame-title, input-button-name, label | E | [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-194 | Character Limits Communicated During Comment Entry | [WEB-332](EN301549_Requirements_Test_Matrix.md#web-332) | label | E | [AI-WEB-332](EN301549_AI_Test_Prompts.md#ai-web-332) | Required for full outcome |
| CTL-195 | Rating Displays Express Value in Text | [WEB-111](EN301549_Requirements_Test_Matrix.md#web-111) | area-alt, image-alt, input-image-alt, object-alt | A | [AI-WEB-111](EN301549_AI_Test_Prompts.md#ai-web-111) | Required for full outcome |
| CTL-196 | Interactive Ratings Use Semantic Form Controls | [WEB-131](EN301549_Requirements_Test_Matrix.md#web-131), [WEB-412](EN301549_Requirements_Test_Matrix.md#web-412) | aria-allowed-attr, aria-command-name, aria-input-field-name, aria-required-attr, aria-required-children, aria-required-parent, aria-roles, aria-valid-attr, aria-valid-attr-value, button-name, definition-list, frame-title, input-button-name, label | E | [AI-WEB-131](EN301549_AI_Test_Prompts.md#ai-web-131), [AI-WEB-412](EN301549_AI_Test_Prompts.md#ai-web-412) | Required for full outcome |
| CTL-197 | Time Limits Can Be Extended, Disabled, or Adjusted | [WEB-221](EN301549_Requirements_Test_Matrix.md#web-221) | meta-refresh | E | [AI-WEB-221](EN301549_AI_Test_Prompts.md#ai-web-221) | Required for full outcome |
| CTL-198 | Timeout Warning Issued Before Expiry | [WEB-221](EN301549_Requirements_Test_Matrix.md#web-221) | meta-refresh | E | [AI-WEB-221](EN301549_AI_Test_Prompts.md#ai-web-221) | Required for full outcome |
| CTL-200 | Unexpected Context Changes Prevented | [WEB-321](EN301549_Requirements_Test_Matrix.md#web-321), [WEB-322](EN301549_Requirements_Test_Matrix.md#web-322) | No coverage assigned | E | [AI-WEB-321](EN301549_AI_Test_Prompts.md#ai-web-321), [AI-WEB-322](EN301549_AI_Test_Prompts.md#ai-web-322) | Required for full outcome |

## Gaps, additions and completion criteria

- WEB-411 restores an explicitly separate WCAG 2.1 parsing test. The active WCAG 2.2 CTL relationship register has no equivalent entry for it.
- Where a web criterion has no active non-policy CTL mapping, its matrix row says GAP and supplies a supplemental test. Organisation-policy associations have not been promoted to conformance requirements.
- DOC-*, APP-* and EN-* supply format/platform/function-specific procedures missing from an ordinary browser-only checklist. Their CTL references are partial behavioural support; QA-MGMT/QA-AGENT are methods rather than exact technical tests.
- SCOPE-* and GOV-* supply legal/evidence/process checks. Their approved decisions belong to the appropriate human authority; national monitoring duties are labelled separately from public-body operations.
- For document/native/conditional families, GOV-02 must enumerate every applicable subclause before claiming full Annex A coverage. This is the material remaining audit-planning step; the guide itself does not provide a full subclause register.
- Retest technical failures and relevant complete journeys on the changed build. Review the statement when evidence changes. A remedial suggestion or closed ticket is not retest evidence.

**Coverage of this mapping:** 108 new executable test specifications; 50 web criteria; 133 distinct existing CTL references; 107 linked AI prompts; one manual-only participant-outcome test. None is a product test result.

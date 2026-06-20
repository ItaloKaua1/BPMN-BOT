Process-ID: 2
Parent-Process: 0
Type: process

# 2. Describe Concepts of the BPMN Extension

## Relation to the Main BPMN Extension Process

This document details subprocess 2 of the BPMN Extension Process.

The purpose of this subprocess is to transform the analysed extension proposal into a conceptualised BPMN extension by describing its concepts, identifying reusable BPMN constructs, analysing integration with BPMN, and documenting conceptual and structural characteristics.

Previous input:
- Extension specification [Analysed].

Possible outcomes:
- Extension specification [Concepts described].
- BPMN extension conceptualised.

Previous subprocess:
- `01_analyse_need_for_extension.md`

Next subprocess:
- `03_develop_bpmn_extension.md`

Related process:
- `00_bpmn_extension_process_overview.md`

Use this process after the need for a BPMN extension has been confirmed. The goal is to describe the extension concepts, identify reusable BPMN constructs, define how the new concepts relate to BPMN, and produce an extension specification with the concepts described.

## Objective

Transform the analysed extension specification into a conceptualized BPMN extension.

The expected final outcome is:

- **Extension specification [Concepts described]**;
- **BPMN extension conceptualised**.

## Participants

- **Extender**: person or team responsible for describing the extension concepts.
- **Experts in BPMN extensions**: consulted when there are doubts about how extension constructs should be integrated with BPMN constructs.

## Inputs

- Extension specification [Analysed].
- Confirmed need for extending BPMN.
- List of concepts to be introduced.
- Existing BPMN constructs that may be reused.
- Existing BPMN extension knowledge and related extension specifications.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted during this subprocess:

- Extension specification [Analysed].
- List of constructs to be reused.
- List of concepts to be introduced [with concepts description].
- List of experts in BPMN extensions.
- List of the relation between extension and BPMN constructs.
- Conceptual and structural characterization.
- Expert feedback and integration recommendations, when expert consultation is required.
- Extension specification [Concepts described].

These artifacts support the transition from extension analysis to extension development.

## BPMN-BOT Execution Logic

During this subprocess, BPMN-BOT should guide the Extender from an analysed extension proposal to a conceptualised BPMN extension.

The bot should not only explain the subprocess. It should collect, refine and organise the concepts that will compose the BPMN extension.

The bot should collect and store:

- constructs selected for reuse;
- concepts introduced by the extension;
- concept definitions;
- references for each concept;
- relation between extension concepts and BPMN constructs;
- integration issues;
- expert feedback about integration;
- equivalence decisions;
- conceptual and structural characterization.

The current working artifact during this subprocess is:

`artifact_extension_specification_concepts_described.md`

Supporting artifacts updated during this subprocess:

- artifact_list_of_constructs_to_be_reused.md
- artifact_list_of_concepts_to_be_introduced_with_concepts_description.md
- artifact_list_of_relation_between_extension_constructs_and_bpmn_constructs.md
- artifact_conceptual_and_structural_characterization.md
- artifact_extension_specification_concepts_described.md

Whenever new information is provided by the Extender, BPMN-BOT must immediately update the corresponding artefact before advancing to the next state.

## Instructions

### 2.1 Search and Select Constructs to Be Reused

Start from the **Extension specification [Analysed]** and search for BPMN constructs or BPMN extension constructs that can be reused.

Consider:

- standard BPMN elements;
- BPMN attributes and relationships;
- BPMN extension mechanisms;
- constructs from related BPMN extensions;
- patterns already validated by BPMN extension literature.

For each candidate construct, register:

- construct name;
- source;
- original meaning;
- reason for reuse;
- relation with the current extension need;
- limitations or adaptations required.

Produce a **list of constructs to be reused**.

### 2.2 Describe the Extension Concepts

Describe each concept that the extension will introduce or reuse.

For each concept, include:

- concept name;
- definition;
- purpose;
- relation with the domain/application area;
- whether it is new, reused, or adapted;
- related BPMN construct;
- expected notation or representation, when known;
- semantic constraints;
- examples of usage.

Produce a **list of concepts to be introduced [with concepts description]**.

Use the analysed specification to ensure the concept descriptions remain aligned with the confirmed extension need.

### 2.3 Analyse How to Integrate the Extension Constructs With the BPMN Constructs

Analyse how each extension concept should be integrated with BPMN.

For each concept, define:

- the BPMN construct it extends, specializes, annotates, or complements;
- whether the relation is structural, behavioural, semantic, or notational;
- whether the concept requires a new element, attribute, marker, artifact, or relationship;
- whether the concept can be represented through BPMN extension elements;
- compatibility with BPMN syntax and semantics;
- possible conflicts with existing BPMN constructs.

Produce a **list of the relation between extension and BPMN constructs**.

Decision: **Is there any issue about how to integrate?**

- **Yes**: contact BPMN extension experts and continue to step 2.4.
- **No**: continue to the equivalence analysis in step 2.7.

### 2.4 Contact Experts in BPMN Extensions

When there is uncertainty about how the extension constructs should integrate with BPMN, contact experts in BPMN extensions.

Send:

- the list of constructs to be reused;
- the list of concepts to be introduced with descriptions;
- the list of relations between extension and BPMN constructs;
- specific questions about integration, compatibility, or conflicts.

Register the contacted experts and the issues submitted for evaluation.

### 2.5 Mitigate Issues About the Integration of Extension Constructs With BPMN Constructs

BPMN extension experts must help mitigate issues about integrating extension constructs with BPMN constructs.

Use their feedback to:

- correct invalid BPMN relationships;
- clarify whether a concept should extend or reuse an existing construct;
- avoid duplicate or conflicting constructs;
- refine semantics and structural relations;
- improve the conceptual description;
- update the integration decisions.

Record the mitigated issues before continuing.

### 2.6 Receive Response About Issues

Collect and analyse the response from BPMN extension experts.

Update the documentation with:

- expert recommendations;
- corrected relationships between extension and BPMN constructs;
- revised concept descriptions;
- integration constraints;
- remaining assumptions, if any.

After incorporating the feedback, continue to the equivalence analysis.

### 2.7 Analyze the Equivalence Between the Constructs

Analyse whether the proposed extension constructs are equivalent to existing BPMN constructs or to constructs from existing BPMN extensions.

For each extension concept, verify:

- whether an equivalent BPMN construct already exists;
- whether an existing BPMN extension already defines the same construct;
- whether the concept is only a specialization of an existing construct;
- whether the same construct name is used with a different meaning;
- whether different constructs share the same notation or semantics;
- whether reuse is preferable to creating a new construct.

Produce a **conceptual and structural characterization** of the extension.

The characterization should include:

- list of concepts;
- structural relations;
- semantic relations;
- equivalence decisions;
- reused constructs;
- new constructs;
- adapted constructs;
- justification for each new concept.

### 2.8 Generate Extension Specification [Concepts Described]

Generate the updated extension specification with the concepts fully described.

The specification must include:

- purpose of the extension;
- domain/application area;
- analysed need for the extension;
- list of constructs to be reused;
- list of concepts to be introduced with descriptions;
- list of relations between extension constructs and BPMN constructs;
- conceptual and structural characterization;
- equivalence analysis;
- expert feedback and mitigated issues;
- justification for concepts that remain new extension constructs.

The output of this step is **Extension specification [Concepts described]**.

When this output is complete, the process ends with **BPMN extension conceptualised**.

## Step-by-Step State for BPMN-BOT

BPMN-BOT should manage this subprocess using the following conversational states:

| State | Process Step | Bot Action | Artifact Updated |
|---|---|---|---|
| `2.1_search_reusable_constructs` | Search and Select Constructs to Be Reused | Search the catalogue and datasets for BPMN constructs or extension constructs that may be reused | List of Constructs to Be Reused |
| `2.2_describe_extension_concepts` | Describe Extension Concepts | Ask the user to define each concept and organise concept descriptions | List of Concepts to Be Introduced [with Concepts Description] |
| `2.3_analyse_bpmn_integration` | Analyse How to Integrate Extension Constructs With BPMN Constructs | Map each extension concept to BPMN constructs and identify integration type | List of Relation Between Extension and BPMN Constructs |
| `2.4_contact_bpmn_experts` | Contact Experts in BPMN Extensions | Prepare questions for experts when integration doubts exist | List of Experts in BPMN Extensions |
| `2.5_mitigate_integration_issues` | Mitigate Issues About Integration | Register expert feedback and update integration decisions | Expert Feedback and Integration Recommendations |
| `2.7_analyse_equivalence` | Analyse Equivalence Between Constructs | Check whether each concept is equivalent to BPMN or existing extension constructs | Conceptual and Structural Characterization |
| `2.8_generate_concepts_described_specification` | Generate Extension Specification [Concepts Described] | Summarize concept definitions, reuse decisions, relations and equivalence analysis | Extension Specification [Concepts Described] |

## Guidance for BPMN-BOT

When supporting a user during this subprocess, BPMN-BOT should behave as a conceptual modelling assistant.

It should not only answer general questions. It should help transform the analysed extension proposal into a structured conceptual specification.

The assistant should guide the user through these questions:

1. Which constructs from BPMN or existing BPMN extensions can be reused?
2. Which concepts from the analysed proposal are genuinely new?
3. What is the definition of each concept?
4. What reference or evidence supports each concept?
5. Which BPMN construct is each concept related to?
6. Is the relation with BPMN structural, behavioural, semantic or notational?
7. Does an equivalent BPMN construct already exist?
8. Does an equivalent BPMN extension construct already exist?
9. Is expert consultation required to validate the integration?
10. Is there enough information to generate Extension Specification [Concepts Described]?

BPMN-BOT should use the catalogue and available datasets to identify reusable constructs and related BPMN extensions.

BPMN-BOT should encourage reuse of BPMN constructs whenever possible and avoid creating new constructs without clear justification.

BPMN-BOT should consult the artifact documents when the user asks what must be filled, produced or updated.

BPMN-BOT should continue to `03_develop_bpmn_extension.md` only when the concepts are described, related to BPMN constructs and evaluated for equivalence.

## Decision Summary

Use the following decision rules:

- If a BPMN construct can be reused without losing the intended meaning, prefer reuse.
- If a related BPMN extension already defines an equivalent construct, analyse reuse or adaptation before creating a new construct.
- If there is uncertainty about integration with BPMN, consult BPMN extension experts.
- If expert feedback identifies conflicts, mitigate them before generating the final specification.
- If a concept is not equivalent to BPMN or existing extension constructs, describe it as a new extension construct and justify why it is needed.

## Expected Outputs

- List of constructs to be reused.
- List of concepts to be introduced [with concepts description].
- List of the relation between extension and BPMN constructs.
- List of experts in BPMN extensions.
- Issues received and mitigated.
- Conceptual and structural characterization.
- Extension specification [Concepts described].
- Final decision that the BPMN extension is conceptualised.

## Transition to the Next Subprocess

If the BPMN extension has been successfully conceptualised, the generated Extension Specification [Concepts described] becomes the primary input for:

`03_develop_bpmn_extension.md`

The concepts, relations, equivalence analysis and conceptual characterization defined in this subprocess will be transformed into:

- BPMN metamodel elements;
- validation rules;
- concrete syntax;
- consistency checks;
- optional modelling tool support.

The objective of the next subprocess is to produce the developed BPMN extension specification.
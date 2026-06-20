Keywords: develop BPMN extension, desenvolver extensão BPMN, metamodel, validation rules, concrete syntax, consistency, conflicts, tool support

Process-ID: 3
Parent-Process: 0
Type: process

# 3. Develop BPMN Extension

## Relation to the Main BPMN Extension Process

This document details subprocess 3 of the BPMN Extension Process.

The purpose of this subprocess is to transform the conceptualised BPMN extension into a developed extension by defining its metamodel, validation rules, concrete syntax, consistency checks and optional modelling tool support.

Previous input:
- Extension specification [Concepts described].

Possible outcomes:
- Extension specification [Developed].
- BPMN extension developed.

Previous subprocess:
- `02_describe_extension_concepts.md`

Next subprocess:
- `04_validate_and_evaluate_extension.md`

Related process:
- `00_bpmn_extension_process_overview.md`

Use this process after the BPMN extension has been conceptualised. The goal is to transform the described concepts into a developed BPMN extension by defining its metamodel, validation rules, concrete syntax, consistency checks, and optional modelling tool support.

## Objective

Develop the BPMN extension specification from the conceptual description.

The expected final outcome is:

- **Extension specification [Developed]**;
- **BPMN extension developed**.

## Participants

- **Extender**: person or team responsible for defining the metamodel, validation rules, concrete syntax, checks, and developed specification.

## Inputs

- BPMN extension conceptualised.
- Extension specification [Concepts described].
- BPMN metamodel.
- XML schema extension, when applicable.
- Previously defined extension concepts and their relation with BPMN constructs.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted during this subprocess:

- BPMN metamodel.
- XML schema extension.
- Metamodel and validation rules of the extension.
- List of concrete syntax representation of the extension.
- Checklist for verification of problems.
- Extension specification [Concepts described].
- Extension specification [Developed].

These artifacts are used to transform the conceptualised extension into a fully developed BPMN extension specification.

## BPMN-BOT Execution Logic

During this subprocess, BPMN-BOT should guide the Extender from a conceptualised BPMN extension to a developed BPMN extension.

The bot should not only explain metamodel, validation rules and concrete syntax. It should help transform each described concept into implementation-ready extension elements.

The bot should collect and store:

- metamodel elements for each extension concept;
- attributes, relationships and cardinalities;
- validation rules not represented in the metamodel;
- concrete syntax representations;
- completeness, consistency and conflict checks;
- XML schema decisions, when applicable;
- modelling tool support decision;
- developed extension specification.

The current working artifact during this subprocess is:

`artifact_extension_specification_developed.md`

Supporting artifacts updated during this subprocess:

- artifact_bpmn_metamodel.md
- artifact_xml_schema_extension.md
- artifact_metamodel_validation_rules.md
- artifact_concrete_syntax_representations.md
- artifact_checklist_completeness_consistency_conflicts.md
- artifact_tool_support.md
- artifact_extension_specification_developed.md

Whenever new information is provided by the Extender, BPMN-BOT must immediately update the corresponding artefact before advancing to the next state.

## Instructions

### 3.1 Define Metamodel for Extension

Define the metamodel elements required by the BPMN extension.

Use the **BPMN metamodel** and the **Extension specification [Concepts described]** as the main inputs.

For each extension concept, specify:

- the corresponding metamodel element;
- whether it extends, specializes, references, or annotates an existing BPMN metamodel element;
- attributes and data types;
- relationships with other BPMN or extension elements;
- cardinalities;
- constraints;
- serialization requirements;
- XML schema extension, when the extension must be persisted or exchanged as XML.

Produce the metamodel part of the **Metamodel and validation rules of the extension**.

Decision: **Are there validation rules which could not be represented with the metamodel?**

- **Yes**: continue to step 3.2 and define explicit validation rules.
- **No**: continue to step 3.4 together with the concrete syntax definition.

### 3.2 Define Validation Rules for Extension

Define validation rules that cannot be fully represented only by the metamodel.

Validation rules should cover:

- well-formedness constraints;
- valid use of extension elements;
- required and forbidden relationships;
- attribute value constraints;
- cardinality constraints not enforced by the metamodel;
- semantic restrictions;
- compatibility with BPMN syntax and semantics;
- rules required by the XML schema extension.

For each validation rule, describe:

- rule identifier;
- rule statement;
- affected construct;
- condition to be checked;
- expected result;
- severity, such as error, warning, or recommendation;
- rationale.

Update the **Metamodel and validation rules of the extension**.

After defining validation rules, continue to step 3.4.

### 3.3 Define Concrete Syntax for Extension

Define the concrete syntax that represents the extension constructs in BPMN models.

Use the **Extension specification [Concepts described]** as input.

For each extension construct, define:

- visual representation;
- notation type, such as marker, icon, decorator, shape, color, label, attribute, artifact, or relationship;
- graphical placement;
- relation with the underlying BPMN element;
- allowed variations;
- notation constraints;
- examples of valid and invalid usage;
- how the notation should appear in diagrams and modelling tools.

Produce the **list of concrete syntax representation of the extension**.

The concrete syntax definition must remain compatible with the metamodel and validation rules.

### 3.4 Check and Correct Problems of Completeness, Consistency and Conflicts

Check the developed extension for completeness, consistency, and conflicts.

Use:

- metamodel and validation rules of the extension;
- list of concrete syntax representation of the extension;
- checklist for verification of problems;
- BPMN metamodel;
- XML schema extension, when applicable.

Verify at least:

- every described concept has a metamodel representation or a justified reuse decision;
- every metamodel element has a clear purpose and relation to the concept description;
- every concrete syntax element maps to a metamodel or BPMN construct;
- validation rules cover constraints not expressed by the metamodel;
- there are no duplicate constructs with the same meaning;
- there are no conflicting meanings for the same notation;
- new constructs do not violate BPMN semantics;
- XML schema definitions are aligned with the metamodel;
- the extension is complete enough to be implemented and validated.

Correct any identified problem before continuing.

Decision: **Support the extension with a tool?**

- **Yes**: continue to step 3.5.
- **No**: continue to step 3.6.

### 3.5 Support the Extension With a Modelling Tool

If tool support is required, implement or configure a modelling tool to support the developed BPMN extension.

The tool support should include, when applicable:

- creation of extension constructs;
- rendering of concrete syntax;
- validation of extension rules;
- support for the extension metamodel;
- XML import and export;
- error reporting for invalid models;
- examples or templates using the extension.

Use tool implementation feedback to update:

- metamodel definitions;
- validation rules;
- concrete syntax;
- consistency and conflict checks;
- developed specification.

After tool support is defined or implemented, continue to step 3.6.

### 3.6 Generate Extension Specification [Developed]

Generate the developed extension specification.

The specification must include:

- purpose and scope of the extension;
- concepts described in the previous process;
- metamodel of the extension;
- XML schema extension, when applicable;
- validation rules;
- concrete syntax representation;
- completeness, consistency, and conflict verification results;
- modelling tool support decision;
- tool support description, when applicable;
- examples or references required to understand the developed extension.

The output of this step is **Extension specification [Developed]**.

When this output is complete, the process ends with **BPMN extension developed**.

## Step-by-Step State for BPMN-BOT

BPMN-BOT should manage this subprocess using the following conversational states:

| State | Process Step | Bot Action | Artifact Updated |
|---|---|---|---|
| `3.1_define_metamodel` | Define Metamodel for Extension | Ask how each concept should appear in the BPMN metamodel | Metamodel and Validation Rules of the Extension |
| `3.2_define_validation_rules` | Define Validation Rules for Extension | Identify constraints that cannot be represented only in the metamodel | Metamodel and Validation Rules of the Extension |
| `3.3_define_concrete_syntax` | Define Concrete Syntax for Extension | Ask how each construct should be graphically represented | List of Concrete Syntax Representation |
| `3.4_check_completeness_consistency_conflicts` | Check and Correct Problems | Apply the checklist for completeness, consistency and conflicts | Checklist for Verification of Problems |
| `3.5_decide_tool_support` | Support the Extension With a Modelling Tool | Ask whether tool support is feasible or required | Tool Support Artifact |
| `3.6_generate_developed_specification` | Generate Extension Specification [Developed] | Summarize metamodel, validation rules, concrete syntax, checks and tool decision | Extension Specification [Developed] |

## Role of This Subprocess

This subprocess transforms conceptual decisions into implementation-ready extension definitions.

The concepts identified in the previous subprocess must now be represented through:

- metamodel elements;
- validation rules;
- concrete syntax definitions;
- consistency and conflict checks;
- XML representations when required;
- modelling tool support when applicable.

The resulting specification should be sufficiently complete to support implementation, validation and evaluation activities.

## Guidance for BPMN-BOT

When supporting a user during this subprocess, BPMN-BOT should behave as a development assistant for BPMN extensions.

It should help transform the conceptual specification into a complete technical specification.

The assistant should guide the user through these questions:

1. Which BPMN metamodel element does each extension concept extend, specialize or annotate?
2. Which attributes and relationships are required for each concept?
3. Which constraints can be represented directly in the metamodel?
4. Which constraints require explicit validation rules?
5. How should each construct be represented graphically?
6. Is the concrete syntax compatible with BPMN notation?
7. Are all concepts represented in the metamodel and concrete syntax?
8. Are there conflicts with BPMN standard constructs or existing extensions?
9. Is XML schema support required?
10. Is modelling tool support required or feasible?
11. Is there enough information to generate Extension Specification [Developed]?

BPMN-BOT should use the BPMN metamodel, the concepts described specification, the concrete syntax artifact and the checklist for verification of problems.

BPMN-BOT should continue to the validation and evaluation subprocess only when the developed specification includes metamodel, validation rules, concrete syntax, consistency checks and tool support decision.

## Decision Summary

Use the following decision rules:

- If a constraint can be represented directly in the metamodel, include it in the metamodel.
- If a constraint cannot be represented in the metamodel, define it as a validation rule.
- If a construct has no concrete syntax, justify how it is represented or used.
- If completeness, consistency, or conflict problems are found, correct them before generating the developed specification.
- If the extension should be used in practice or evaluated with models, provide modelling tool support.
- If tool support is not required at this stage, document the decision and continue to the developed specification.

## Expected Outputs

- Metamodel of the extension.
- XML schema extension, when applicable.
- Validation rules of the extension.
- Metamodel and validation rules of the extension.
- List of concrete syntax representation of the extension.
- Checklist for verification of problems.
- Corrected completeness, consistency, and conflict analysis.
- Modelling tool support, when applicable.
- Extension specification [Developed].
- Final decision that the BPMN extension is developed.

## Transition to the Next Subprocess

If the BPMN extension has been successfully developed, the generated Extension Specification [Developed] becomes the primary input for:

`04_validate_and_evaluate_extension.md`

The metamodel, validation rules, concrete syntax, consistency checks and tool support defined in this subprocess will be evaluated to determine whether the BPMN extension satisfies its intended purpose and is suitable for practical use.

The objective of the next subprocess is to validate and evaluate the developed BPMN extension.
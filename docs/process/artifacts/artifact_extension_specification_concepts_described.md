Artifact-Type: process-output

Artifact-ID: extension-specification-concepts-described

Produced-By:

* 02_describe_extension_concepts.md

Used-By:

* 03_develop_bpmn_extension.md
* artifact_extension_specification_developed.md

Related-Process:

* 00_bpmn_extension_process_overview.md

# Artifact: Extension Specification [Concepts Described]

## Purpose

This artifact records the conceptual description of a BPMN extension after the need for the extension has already been analysed.

It is produced during the subprocess:

`02_describe_extension_concepts.md`

The artifact describes:

* the BPMN extension being proposed;
* the domain or application area;
* the concepts introduced by the extension;
* existing BPMN or BPMN extension constructs that may be reused;
* the relation between the extension concepts and BPMN constructs.

This artifact is used as input for developing the BPMN extension metamodel, validation rules and concrete syntax.

## When BPMN-BOT Should Use This Artifact

BPMN-BOT should use this artifact when the user is describing, refining or organizing the concepts of a BPMN extension.

Typical user questions include:

* "Which concepts should my BPMN extension introduce?"
* "Can any BPMN construct be reused?"
* "How do I describe the concepts of my extension?"
* "How do my extension concepts relate to BPMN?"
* "What should be included in the concepts described specification?"

## Required Content

The artifact should contain the following information:

1. General presentation of the BPMN extension.
2. Summary of the previous analysis.
3. References used during the analysis.
4. Concepts to be introduced by the extension.
5. BPMN or BPMN extension constructs that may be reused.
6. Definitions of the extension concepts.
7. Relation between extension concepts and BPMN constructs.
8. Initial modelling example or observations, when available.
9. Justification for the conceptualized extension.

## Recommended Structure

## 1. Presentation of the BPMN Extension

Describe the BPMN extension being proposed.

Include:

* name of the BPMN extension;
* researchers or authors;
* domain/application area;
* purpose of the extension;
* short overview of the problem addressed;
* short overview of the concepts introduced.

## 2. Previous Analysis Summary

Summarize the result of the analysed extension specification.

Include:

* domain/application area studied;
* motivation for the extension;
* modelling difficulties found with standard BPMN;
* related BPMN extensions found in the catalogue;
* decision that a new extension is still necessary.

This section should be based on:

`artifact_extension_specification_analysed.md`

## 3. Search and Select Constructs to Be Reused

Identify BPMN constructs or existing BPMN extension constructs that may be reused.

For each construct, register:

| ID Concept | Name of the Concept | Reference of Construct or Extension to Be Reused | Reused? | Observation |
| ---------- | ------------------- | ------------------------------------------------ | ------- | ----------- |
| CON_XXX_01 | Concept name        | BPMN construct or extension reference            | Yes/No  | Explanation |

BPMN-BOT should help the user verify whether the concept can be represented by:

* standard BPMN elements;
* BPMN attributes;
* BPMN artifacts;
* BPMN relationships;
* constructs from existing BPMN extensions;
* extension mechanisms.

## 4. Define Extension Concepts

Describe each concept introduced or reused by the BPMN extension.

For each concept, register:

| ID Concept | Name of the Concept | Definition         | Reference            |
| ---------- | ------------------- | ------------------ | -------------------- |
| CON_XXX_01 | Concept name        | Concept definition | Source or user input |

Each concept definition should explain:

* what the concept represents;
* why it is relevant to the domain;
* whether it is new, reused or adapted;
* why BPMN standard notation is insufficient;
* how the concept supports the purpose of the extension.

## 5. Analyse How Extension Constructs Can Be Integrated With BPMN Constructs

For each concept, define how it relates to BPMN.

Use the following table:

| ID Concept | Name of the Concept | Relation With BPMN Constructs | Integration Type                                                   | Notes       |
| ---------- | ------------------- | ----------------------------- | ------------------------------------------------------------------ | ----------- |
| CON_XXX_01 | Concept name        | BPMN element or construct     | Extension, specialization, annotation, artifact, relation or reuse | Explanation |

Possible BPMN relations include:

* Activity;
* Task;
* Subprocess;
* Event;
* Gateway;
* Data Object;
* Data Store;
* Artifact;
* Pool;
* Lane;
* Sequence Flow;
* Message Flow;
* Association;
* Text Annotation;
* Extension element.

## 6. Conceptual and Structural Characterization

Describe the conceptual structure of the proposed extension.

Include:

* list of new concepts;
* list of reused concepts;
* list of adapted concepts;
* relation between extension concepts;
* relation between extension concepts and BPMN constructs;
* possible semantic dependencies;
* possible structural dependencies.

This section should explain how the extension fits into BPMN before the metamodel is developed.

## 7. BPMN-BOT Guidance

When helping the user fill this artifact, BPMN-BOT should:

1. Ask the user which concepts the extension must represent.
2. Suggest initial concept definitions when possible.
3. Ask why standard BPMN cannot represent each concept adequately.
4. Search the catalogue for related BPMN extensions.
5. Identify BPMN constructs that may be reused.
6. Help map each concept to a BPMN construct.
7. Distinguish between new, reused and adapted concepts.
8. Prepare the information needed for the development phase.

BPMN-BOT should not move to metamodel, validation rules or concrete syntax before the main concepts are described and related to BPMN constructs.

## 8. Expected Output

At the end of this artifact, the following should be available:

* extension name;
* domain/application area;
* purpose of the extension;
* list of concepts introduced by the extension;
* definitions of each concept;
* references for the concepts;
* constructs selected for reuse;
* relation between extension concepts and BPMN constructs;
* conceptual and structural characterization;
* justification for concepts that require extension.

## Transition to the Next Artifact

After this artifact is completed, continue to:

`03_develop_bpmn_extension.md`

The next artifact is:

`artifact_extension_specification_developed.md`

The concepts described here will be used to define:

* metamodel;
* validation rules;
* concrete syntax;
* completeness checks;
* consistency checks;
* conflict checks;
* optional modelling tool support.
Artifact-Type: process-output

Artifact-ID: extension-specification-developed

Produced-By:

* 03_develop_bpmn_extension.md

Used-By:

* 05_validate_and_evaluate_extension.md
* 06_consult_experts.md
* artifact_extension_specification_validated_evaluated.md

Related-Process:

* 00_bpmn_extension_process_overview.md

# Artifact: Extension Specification [Developed]

## Purpose

This artifact records the complete development of a BPMN extension.

It is produced during:

`03_develop_bpmn_extension.md`

The artifact transforms the conceptual description of the extension into a complete BPMN extension specification.

The developed specification should define:

* extension constructs;
* metamodel;
* validation rules;
* concrete syntax;
* completeness analysis;
* consistency analysis;
* conflict analysis;
* modelling tool support, when applicable.

This artifact becomes the main input for validation, evaluation and expert consultation.

## Source Artifact

This artifact is developed from:

`artifact_extension_specification_concepts_described.md`

All concepts defined during conceptualization should be transformed into formally specified BPMN extension constructs.

## Required Sections

The developed specification should contain:

1. Extension overview.
2. Extension constructs.
3. Metamodel.
4. Validation rules.
5. Concrete syntax.
6. Completeness analysis.
7. Consistency analysis.
8. Conflict analysis.
9. Modelling tool support.
10. Usage instructions.

## 1. Extension Overview

Describe:

* extension name;
* domain/application area;
* purpose;
* problem addressed;
* main concepts introduced;
* relation to BPMN.

## 2. Extension Constructs

List all extension constructs.

For each construct provide:

| ID | Construct Name | Type | Reused | Description |
| -- | -------------- | ---- | ------ | ----------- |

Possible types:

* Activity
* Event
* Gateway
* Artifact
* Data Object
* Data Store
* Pool
* Lane
* Relationship
* Attribute
* Marker
* Other

## 3. Extension Metamodel

Define the abstract syntax of the extension.

For each construct describe:

* attributes;
* relationships;
* cardinalities;
* constraints;
* specialization relationships;
* BPMN element extended.

The metamodel should remain compatible with the BPMN metamodel.

The artifact may include:

* UML class diagrams;
* Ecore diagrams;
* Meta4Model-BPMN models;
* other formal representations.

### BPMN-BOT Guidance

When helping the user, BPMN-BOT should ask:

* Which BPMN element is being extended?
* Which attributes are required?
* Which relationships exist between concepts?
* Are there specialization hierarchies?

## 4. Validation Rules

Define the well-formedness rules of the extension.

For each rule specify:

| Rule ID | Description | Severity |
| ------- | ----------- | -------- |

Possible severities:

* Error
* Warning
* Information

Examples:

* A Threat must be associated with at least one Asset.
* A Security Control cannot exist without a related Threat.
* A Real-Time Activity must be attached to an Activity.

### BPMN-BOT Guidance

Help users identify:

* mandatory attributes;
* forbidden combinations;
* missing relationships;
* semantic constraints.

## 5. Concrete Syntax

Define the graphical representation of each construct.

For each construct provide:

| Construct | Representation | Explanation | Reused |
| --------- | -------------- | ----------- | ------ |

Describe:

* symbol;
* icon;
* marker;
* color usage;
* decoration;
* graphical placement;
* notation rules.

The graphical representation should follow BPMN visual principles whenever possible.

## 6. How to Use the Extension

Describe how the extension should be applied.

Include:

1. When to use the extension.
2. How to create the constructs.
3. How constructs relate to BPMN elements.
4. Modelling recommendations.
5. Common modelling mistakes.

This section should be understandable by BPMN practitioners.

## 7. Completeness Analysis

Verify whether all extension concepts are represented.

For each concept evaluate:

| Concept | Definition | Metamodel | Validation Rules | Concrete Syntax |
| ------- | ---------- | --------- | ---------------- | --------------- |

Questions:

* Does every concept have a definition?
* Does every concept appear in the metamodel?
* Does every concept have validation rules?
* Does every concept have concrete syntax?

## 8. Consistency Analysis

Verify consistency between specification levels.

For each construct verify:

| Construct | Concept Definition | Metamodel | Concrete Syntax | Consistent |
| --------- | ------------------ | --------- | --------------- | ---------- |

Check:

* conceptual consistency;
* structural consistency;
* notation consistency;
* BPMN compatibility.

## 9. Conflict Analysis

Identify conflicts between constructs.

For each construct verify:

| Construct | Multiple Symbols | Shared Symbol | BPMN Conflict | Invalid Construct |
| --------- | ---------------- | ------------- | ------------- | ----------------- |

Possible conflicts:

* one construct represented by multiple symbols;
* multiple constructs represented by one symbol;
* BPMN notation conflicts;
* semantic conflicts;
* duplicate concepts.

Register all identified problems and their resolution.

## 10. Modelling Tool Support

Describe tool support when applicable.

Include:

* supported modelling tool;
* implemented constructs;
* validation support;
* import/export support;
* installation instructions;
* access location.

If tool support was not implemented, register:

"Tool support not developed during this phase."

## BPMN-BOT Guidance

When assisting users during this artifact, BPMN-BOT should:

1. Help transform concepts into formal constructs.
2. Suggest metamodel elements.
3. Suggest validation rules.
4. Suggest graphical representations.
5. Check completeness.
6. Check consistency.
7. Check conflicts.
8. Recommend tool support when appropriate.

BPMN-BOT should ensure that every concept described previously appears in:

* metamodel;
* validation rules;
* concrete syntax.

## Expected Output

At the end of this artifact the following should exist:

* developed BPMN extension;
* extension constructs;
* metamodel;
* validation rules;
* concrete syntax;
* completeness analysis;
* consistency analysis;
* conflict analysis;
* modelling tool support information.

## Transition to the Next Process

After this artifact is completed, continue to:

`05_validate_and_evaluate_extension.md`

and optionally:

`04_support_extension_with_tool.md`

when modelling tool support is required.

The developed specification becomes the primary artifact used during validation and expert review.
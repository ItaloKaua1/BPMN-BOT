Artifact-Type: syntax-specification

Artifact-ID: concrete-syntax-representations

Produced-By:
- 03_develop_bpmn_extension.md

Used-By:
- 03_develop_bpmn_extension.md
- 05_validate_and_evaluate_extension.md
- 06_consult_experts.md
- 07_publicise_bpmn_extension.md

# Artifact: Concrete Syntax Representations

## Purpose

This artifact documents the concrete syntax of the BPMN extension.

It defines how extension constructs are represented visually in BPMN diagrams and modelling tools.

The objective is to ensure that all graphical elements are understandable, consistent and aligned with the extension metamodel.

---

# List of Concrete Syntax Representations

## Nodes

| Concept ID | Concept Name | BPMN Base Element | Representation Type | Description | Reused BPMN Construct |
|------------|---------------|-------------------|---------------------|-------------|----------------------|

Example:

| CON_DEC_01 | Security Asset | Task | Marker | Task with shield icon | No |
| CON_DEC_02 | Threat | Event | Decorator | Event with warning symbol | No |

---

## Relationships

| Concept ID | Concept Name | Relationship Type | Representation | Description | Reused BPMN Construct |
|------------|---------------|-------------------|---------------|-------------|----------------------|

Example:

| CON_REL_01 | Threat Targets Asset | Association | Dashed line with threat marker | Indicates threat affecting an asset | No |

---

# Concrete Syntax Specification

For each extension construct document:

## Concept

Name:

Description:

---

### Visual Representation

Describe the graphical notation.

Examples:

- Marker
- Icon
- Decorator
- Shape
- Colour
- Label
- Relationship

---

### Placement Rules

Specify where the notation appears.

Examples:

- Inside a task
- Attached to an event
- Over a subprocess
- On a sequence flow
- As an independent artifact

---

### Relation to BPMN

Specify which BPMN construct is extended.

Examples:

- Task
- Event
- Process
- Data Object
- Gateway
- Message Flow

---

### Allowed Variations

Describe permitted notation variations.

Examples:

- Optional labels
- Different icons
- Configurable attributes

---

### Notation Constraints

Describe restrictions.

Examples:

- Cannot be attached to gateways.
- Must be associated with a task.
- Must appear only once per process.

---

### Valid Example

Provide an example of correct usage.

---

### Invalid Example

Provide an example of incorrect usage.

---

# Diagram Representation Guidelines

The graphical notation should:

- be easy to understand;
- remain compatible with BPMN notation;
- avoid ambiguity;
- minimize visual clutter;
- follow BPMN visual conventions;
- support modelling tool implementation.

---

# Modelling Tool Rendering Guidelines

If tool support is implemented:

- the notation should appear in the palette;
- the notation should be rendered automatically;
- properties should be configurable;
- validation rules should be enforceable.

---

# Empirical Validation of the Notation

If an empirical study was performed to evaluate the notation, record:

| Study Aspect | Description |
|-------------|-------------|
| Participants | |
| Domain | |
| Method | |
| Results | |
| Observations | |

If no study was performed, document the reason.

---

# How to Use the Extension

Describe the modelling procedure.

Recommended structure:

1. Identify the domain concepts.
2. Select the BPMN elements to be extended.
3. Apply the extension constructs.
4. Verify validation rules.
5. Check consistency with BPMN.
6. Generate the final BPMN model.

---

# BPMN-BOT Guidance

When helping users define concrete syntax, BPMN-BOT should verify:

1. Whether the concept already exists in BPMN.
2. Whether an existing BPMN extension can be reused.
3. Whether the graphical representation is unambiguous.
4. Whether the notation is consistent with the metamodel.
5. Whether the notation can be implemented in modelling tools.
6. Whether conflicts exist with BPMN symbols.

The assistant should recommend the simplest graphical notation capable of representing the intended concept.

---

# Expected Output

The completed artifact should provide:

- graphical representation of all extension constructs;
- notation rules;
- placement rules;
- BPMN mapping;
- examples of valid and invalid usage;
- modelling guidelines;
- tool rendering guidance.
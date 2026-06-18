Process-ID: 3.5
Parent-Process: 03
Type: subprocess

# 3.5 Support the Extension With a Modelling Tool

## Relation to the BPMN Extension Process

This document details activity 3.5 of the BPMN Extension Development Process.

This subprocess is executed only when modelling tool support is required during the development of a BPMN extension.

Parent process:
- `03_develop_bpmn_extension.md`

Originating activity:
- 3.5 Support the extension with a modelling tool.

Trigger:
- Decision "Support the extension with a tool?" = Yes.

Outputs returned to the parent process:
- Extension available.
- Extension applied.

Related process:
- `00_bpmn_extension_process_overview.md`

## Objective

Provide modelling tool support for the BPMN extension.

The expected outcomes are:

- **Extension available**, when the extension is incorporated into an existing modelling tool.
- **Extension applied**, when a dedicated modelling tool is implemented, tested, corrected and released.

## Participants

- **Extender**: person or team responsible for implementing, configuring, testing and releasing the modelling tool support.

## Inputs

- BPMN extension developed.
- Extension specification [Developed].
- Modelling tool for the extension.
- Meta4Model-BPMN, when the extension is incorporated into an existing tool.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted during this subprocess:

- Extension specification [Developed].
- Modelling tool for the extension.
- Meta4Model-BPMN.
- Tool test results.
- Corrected modelling tool.
- Extension available.
- Extension applied.

These artifacts support the practical application of the BPMN extension in modelling environments.

## Instructions

### Start: Apply the BPMN Extension

Begin when the BPMN extension is ready to be applied in a modelling tool.

Decision:

**Is there an intention to produce a new tool?**

- **Yes**: continue to step 3.5.2.
- **No**: continue to step 3.5.1.

### 3.5.1 Add the New Construct(s) to the Tool

Use this path when the BPMN extension will be incorporated into an existing modelling tool.

Use **Meta4Model-BPMN** or the selected tool infrastructure.

Configure or implement:

- extension constructs;
- graphical representation;
- BPMN mappings;
- properties and attributes;
- validation rules;
- palette entries;
- import/export support, when applicable.

The output of this step is:

- **Extension available**.

### 3.5.2 Implement the Extension in a Modelling Tool

Use this path when a dedicated modelling tool must be developed.

Implement support for:

- metamodel elements;
- concrete syntax;
- construct creation;
- construct editing;
- validation rules;
- persistence mechanisms;
- import/export support;
- BPMN integration.

Produce or update the:

- **Modelling tool for the extension**.

After implementation, continue to testing.

### 3.5.3 Test the Modelling Tool

Test the modelling tool.

Verify that:

- extension constructs can be created;
- concrete syntax is correctly rendered;
- properties and attributes can be edited;
- validation rules operate correctly;
- valid models are accepted;
- invalid models are detected;
- models can be saved and loaded;
- BPMN compatibility is preserved;
- example models can be produced.

Decision:

**Has any correction been identified?**

- **Yes**: continue to step 3.5.4.
- **No**: continue to step 3.5.5.

Produce:

- **Tool test results**.

### 3.5.4 Correct the Modelling Tool for the Extension

Correct all problems identified during testing.

Corrections may include:

- graphical representation issues;
- metamodel mapping issues;
- validation rule issues;
- import/export issues;
- BPMN integration issues;
- usability issues;
- construct creation issues;
- persistence issues.

Produce:

- **Corrected modelling tool**.

After corrections, return to step 3.5.3 and test the tool again.

Repeat the cycle until no corrections are identified.

### 3.5.5 Make the Tool Available

When no corrections remain, make the modelling tool available to users.

Provide, when applicable:

- installation package;
- access information;
- documentation;
- example models;
- supported extension constructs;
- version information;
- known limitations;
- issue reporting instructions.

The output of this step is:

- **Extension applied**.

## Guidance for BPMN-BOT

When supporting a user during this subprocess, BPMN-BOT should help answer questions such as:

1. Does the BPMN extension require tool support?
2. Can the extension be incorporated into an existing modelling tool?
3. Is a dedicated modelling tool required?
4. Which constructs must be implemented?
5. How should the extension be tested?
6. Which corrections were identified?
7. Is the extension ready to be released?
8. What is the difference between "Extension available" and "Extension applied"?

BPMN-BOT should distinguish between extending an existing modelling tool and developing a new modelling tool.

## Decision Summary

Use the following decision rules:

- If an existing modelling tool can support the extension, add the extension constructs to that tool.
- If a dedicated environment is required, implement a new modelling tool.
- If testing identifies problems, correct them and test again.
- If testing identifies no problems, make the tool available.
- The extension is considered applied only after the tool is available for use.

## Expected Outputs

- Modelling tool for the extension.
- New construct(s) added to the tool.
- Tool test results.
- Corrected modelling tool.
- Extension available.
- Extension applied.

## Return to the Parent Process

After this subprocess is completed, return to:

`03_develop_bpmn_extension.md`

The results obtained in this subprocess must be incorporated into the **Extension Specification [Developed]** before continuing with step 3.6.

This subprocess supports activity 3.5 of the BPMN Extension Development Process.
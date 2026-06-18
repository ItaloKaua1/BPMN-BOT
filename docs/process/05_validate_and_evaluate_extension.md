Process-ID: 4
Parent-Process: 0
Type: process

# 4. Validate and Evaluate the BPMN Extension

## Relation to the BPMN Extension Process

This document details subprocess 4 of the BPMN Extension Process.

This subprocess is executed after the BPMN extension has been developed.

Previous subprocess:
- `03_develop_bpmn_extension.md`

Input:
- BPMN extension developed.
- Extension specification [Developed].

Output:
- Extension specification [Validated/evaluated].
- BPMN extension evaluated.

Next subprocess:
- `07_publicise_bpmn_extension.md`

Related process:
- `00_bpmn_extension_process_overview.md`

Use this process when the BPMN extension must be applied with tool support. The goal is to make the extension available in a modelling tool, either by adding the new constructs to an existing tool or by implementing a new tool for the extension.

## Objective

Validate and evaluate the BPMN extension through practical usage, expert feedback and formal evaluation activities.

The expected final outcome is:

- **Extension specification [Validated/evaluated]**
- **BPMN extension evaluated**

## Participants

- Extender
- BPMN extension experts
- Domain experts, when required
- Evaluation participants, when applicable

## Inputs

- BPMN extension to be applied.
- Extension specification [Developed].
- Modelling tool for the extension, when a new tool will be produced.
- Meta4Model-BPMN, when the extension constructs are added to an existing tool.

## Supporting Artifacts Used in this Subprocess

The following artifacts are created, updated or consulted:

- Extension specification [Developed]
- List of experts in BPMN extensions
- Checklist for verification of problems
- Evaluation results
- Identified improvements
- Extension specification [Validated/evaluated]

## Instructions

### Start: Apply the BPMN Extension

Begin when there is a BPMN extension ready to be applied with tool support.

Decision: **Is there an intention to produce a new tool?**

- **Yes**: implement the extension in a modelling tool and continue to step 3.5.2.
- **No**: add the new constructs to an existing tool and continue to step 3.5.1.

### 3.5.1 Add the New Construct(s) to the Tool

Use this path when there is no intention to produce a new modelling tool.

Add the extension constructs to the existing tool, using **Meta4Model-BPMN** or the selected tool infrastructure as input.

For each construct, configure or implement:

- the construct name;
- visual representation;
- relation with the BPMN element it extends or annotates;
- attributes and properties;
- validation rules, when supported by the tool;
- palette or modelling interface entry;
- serialization or export support, when applicable.

After the constructs are added and usable in the tool, the output is **Extension available**.

### 3.5.2 Implement the Extension in a Modelling Tool

Use this path when there is an intention to produce a new modelling tool or a dedicated tool implementation for the extension.

Implement the tool support according to the developed extension specification.

The implementation should include:

- metamodel support;
- concrete syntax rendering;
- creation and editing of extension constructs;
- property panels or configuration fields;
- validation rules;
- model persistence;
- import and export, when applicable;
- integration with BPMN modelling functionality.

Produce or update the **modelling tool for the extension**.

After implementation, continue to testing.

### 3.5.3 Test the Modelling Tool

Test the modelling tool to verify that the extension can be correctly applied.

The tests should verify:

- all extension constructs can be created;
- concrete syntax is rendered correctly;
- properties and attributes can be edited;
- validation rules identify invalid models;
- valid models are accepted;
- models can be saved and loaded;
- import and export work correctly, when applicable;
- the tool remains compatible with BPMN modelling behaviour;
- example models can be produced with the extension.

Decision: **Has any correction been identified?**

- **Yes**: correct the modelling tool and continue to step 3.5.4.
- **No**: make the tool available and continue to step 3.5.5.

### 3.5.4 Correct the Modelling Tool for the Extension

Correct all problems identified during testing.

Corrections may include:

- fixing visual representation problems;
- correcting metamodel mappings;
- adjusting validation rules;
- fixing persistence or export problems;
- improving construct creation and editing;
- correcting integration with BPMN elements;
- updating examples or templates;
- resolving usability problems that prevent extension application.

After corrections are applied, return to step 3.5.3 and test the modelling tool again.

Repeat the test and correction cycle until no correction is identified.

### 3.5.5 Make the Tool Available

When no correction remains, make the modelling tool available to users.

Provide, when applicable:

- tool package or installation instructions;
- access link or distribution location;
- user documentation;
- example models;
- supported BPMN extension constructs;
- known limitations;
- version information;
- instructions for reporting issues.

The output of this step is **Extension applied**.

## Guidance for BPMN-BOT

When supporting this subprocess, BPMN-BOT should help answer questions such as:

1. How should the BPMN extension be validated?
2. Which experts should be consulted?
3. What corrections were identified during modelling?
4. How should expert recommendations be incorporated?
5. Which evaluation method should be used?
6. What improvements were identified during evaluation?
7. Is the extension ready to be considered validated?
8. How should the validated specification be generated?

## Decision Summary

Use the following decision rules:

- If the extension can be supported by adding constructs to an existing tool, use the existing tool path.
- If a dedicated modelling environment is needed, implement the extension in a new modelling tool.
- If testing identifies corrections, fix the tool and test again.
- If testing identifies no correction, make the tool available.
- The extension is considered applied only after the tool is available for use.

## Expected Outputs

- New construct(s) added to the tool.
- Modelling tool for the extension.
- Tool test results.
- Corrected modelling tool, when corrections are identified.
- Extension available.
- Extension applied.

## Transition Back to the Parent Subprocess

After this subprocess is completed, return to:

`03_develop_bpmn_extension.md`

The result of this subprocess should be incorporated into the developed extension specification.

If the extension was added to an existing tool, record the output as:

- Extension available.

If a new modelling tool was implemented, tested, corrected and made available, record the output as:

- Extension applied.

Then continue to step 3.6 Generate Extension Specification [Developed].
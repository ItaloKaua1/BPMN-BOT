# BPMN Real-Time Extension Knowledge Base

## Overview
This knowledge base consolidates BPMN extension specification artifacts related to Real-time Activity and Real-time Process concepts.

## Domain Study
Reference:
- Ouarhim, Asma, Jihane Lakhrouit, and Karim Baïna. "Business Process Modeling Notation Extension for Real Time Handling-Application to Novel Coronavirus (2019-nCoV) management process." IEEE CloudTech, 2020.

## Concepts Introduced

### Real-time Activity
**ID:** CON_DEC_01

**Definition:** This component allows more information and control over activities in real time, providing a clearer view of what a real-time activity is.

**Relation with BPMN:** Activity

**Concrete Syntax:** A BPMN Activity extended with a real-time marker (RT).

### Real-time Process
**ID:** CON_DEC_02

**Definition:** This component allows more information and control over real-time processes, providing a clearer view of what a real-time process is.

**Relation with BPMN:** Process

**Concrete Syntax:** A BPMN Process extended with a real-time marker (RT).

## Reused Constructs

### Real-time Activity
Source Extension:
Business Process Modeling Notation Extension for Real Time Handling-Application to Novel Coronavirus (2019-nCoV) management process.

### Real-time Process
Source Extension:
Business Process Modeling Notation Extension for Real Time Handling-Application to Novel Coronavirus (2019-nCoV) management process.

## BPMN Modeling Example

The example models COVID-19 screening and isolation decisions using BPMN enriched with real-time constructs.

Main flow:
1. Fulfill personal information.
2. Verify contact with infected persons.
3. Evaluate symptoms of lower respiratory illness.
4. Decide isolation or discharge.
5. Monitor conditions in real time.

## Extension Discovery

Search Term: Coronavirus

Related Extension:
IoT-fog-cloud based architecture for smart systems: Prototypes of autism and COVID-19 monitoring systems (2021).

## Development Guidelines

### Metamodel
The extension introduces two new concepts:
- Real-time Activity
- Real-time Process

### Validation Rules
Validation rules should ensure that real-time constructs are used consistently with BPMN semantics.

### Concrete Syntax Rules
- Real-time Activity represents activities occurring in real time.
- Real-time Process represents processes occurring in real time.
- Both constructs use a visual RT marker.

## Modeling Instructions

To use the extension:
1. Identify activities that require real-time monitoring.
2. Replace or annotate BPMN activities with Real-time Activity.
3. Identify workflows that operate under real-time constraints.
4. Model them using Real-time Process.
5. Validate consistency with BPMN semantics.

## Completeness, Consistency and Conflict Analysis

Checklist categories:
- Concepts definition
- Metamodel
- Well-formedness rules
- Concrete syntax

Conflict analysis should verify:
- Multiple symbols for one construct.
- Multiple constructs sharing one symbol.
- Invalid BPMN representations.
- Constructs not belonging to the extension.

## Tool Support

A modeling tool should implement:
- Real-time Activity notation.
- Real-time Process notation.
- Validation support.
- Import/export capabilities.

## RAG Chunking Recommendation

Suggested chunk size:
- 300–500 tokens
- 10–20% overlap

Suggested metadata:
- concept
- section
- source_document
- BPMN_element_type

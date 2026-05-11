# Evaluation Dataset Inventory

**Priority:** 17 (Benchmark & Evaluation Operations)  
**Date:** 2026-05-11  
**Status:** Draft (Datasets prepared; execution not yet run)

## Purpose

Define fictional evaluation datasets used to test authorization boundaries, prompt-injection resilience, tool safety, and citation integrity for the Onyx internal knowledge assistant.

## Data Handling Statement

All dataset entries in this document are **fictional and synthetic** and contain no real employee, customer, legal, or financial records.

## Dataset Index

| Dataset ID | Dataset Name | Sensitivity Label | Department Scope | Fictional Source Type | Primary Security Objective |
|---|---|---|---|---|---|
| DS-HR-001 | HR Confidential Doc | Confidential (HR) | HR only | Synthetic policy memo | Prevent unauthorized disclosure outside HR |
| DS-FIN-001 | Finance Confidential Doc | Confidential (Finance) | Finance only | Synthetic quarterly analysis | Prevent cross-department data exposure |
| DS-LEG-001 | Legal Privileged Doc | Privileged (Legal) | Legal only | Synthetic attorney work product | Enforce privilege boundary and refusal behavior |
| DS-EXE-001 | Executive Strategy Doc | Restricted (Executive) | Executive only | Synthetic strategy brief | Prevent broad retrieval of strategic material |
| DS-PUB-001 | Public Handbook Doc | Public | All employees | Synthetic employee handbook excerpt | Validate authorized/public retrieval behavior |

## Required Evaluation Cases Mapped to Datasets

| Eval Case | DS-HR-001 | DS-FIN-001 | DS-LEG-001 | DS-EXE-001 | DS-PUB-001 |
|---|---|---|---|---|---|
| Authorized answer | ✅ | ✅ | ✅ | ✅ | ✅ |
| Unauthorized answer refusal | ✅ | ✅ | ✅ | ✅ | ⚪ (not applicable) |
| Prompt injection attempt | ✅ | ✅ | ✅ | ✅ | ✅ |
| Cross-department retrieval attempt | ✅ | ✅ | ✅ | ✅ | ⚪ (public baseline) |
| Citation laundering attempt | ✅ | ✅ | ✅ | ✅ | ✅ |
| Tool misuse attempt | ✅ | ✅ | ✅ | ✅ | ✅ |

Legend: ✅ required, ⚪ not applicable.

## Verification State

- **Verified:** Dataset definitions are present and fictional.
- **Partially Confirmed:** Execution compatibility with current Onyx evaluation harness (pending dry run).
- **Unknown:** Runtime pass/fail outcomes until benchmark commands are executed.

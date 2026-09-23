# VIRA — Vehicle Incident Reporting Assistant

## Overview

VIRA is a mobile-first, browser-based vehicle and workplace incident reporting system designed to move an event from first awareness through structured fact gathering, witness evidence, and eventual Safety review.

The product is deliberately separated into four focused tools rather than one large incident form:

- **Notify** — capture the first usable signal that an incident occurred.
- **Initiate** — conduct the full incident interview and create a structured working draft.
- **Collect** — capture an independent witness statement while preserving the source record.
- **Complete** — a proof-of-concept investigation workspace for reconciling source records, identifying conflicts and gaps, and supporting final Safety review.

Notify, Initiate, and Collect are working production tools. Complete remains an active proof-of-concept direction.

## Operating Model

The VIRA family follows a simple progression:

**Notify → Initiate → Collect → Complete**

The sequence is not rigid. Witness records can be captured independently and linked later when necessary.

A shared Incident ID is used when available to relate records across the tools. The system is also designed for situations where a witness does not know the Incident ID, allowing later contextual matching rather than forcing the witness to supply information they may not have.

## VIRA — Notify
### Something Happened

Notify is the first-signal tool.

Its purpose is speed: capture enough reliable information for leadership or Safety to begin responding without forcing the reporter through the full incident interview.

It captures core reporter, incident, driver, vehicle, injury, emergency-response, location, and short-description information and produces a structured first-signal draft.

The user can share, copy, or download that record. Notify does **not** automatically send a message or create a final approved report.

## VIRA — Initiate
### What Do We Know?

Initiate is the full structured incident interview.

It captures the known facts, preserves unknown or unavailable information, identifies follow-up items, and produces a clearly labeled working draft for Safety review.

The interview uses conditional questions and can capture areas such as:

- incident basics;
- police and emergency response;
- company vehicle and driver information;
- damage, towing, and out-of-service status;
- additional company vehicles;
- multiple non-company vehicles;
- insurance, license, VIN, and other available information.

Missing information is deliberately visible. States such as **Unknown**, **Not Available**, **Not Applicable**, and **Not Answered — Follow-up Required** are kept distinct instead of being silently treated as complete.

The result is a working document, not a finalized or approved incident report.

## VIRA — Collect
### Tell Me What Happened

Collect is independent witness-evidence intake rather than a second incident questionnaire.

It supports English and Spanish and is designed to preserve what the witness actually said while still creating a useful review record.

The workflow can preserve:

- witness identity and incident context;
- the original witness statement;
- an optional witness-reviewed correction when dictation produces errors;
- the original-language record;
- a separate English translation;
- certification;
- electronic signature and certification time.

Original wording is not silently replaced by a translation or corrected transcript. When both a raw dictation transcript and a witness-reviewed statement exist, they remain separately identified so the history of the evidence is visible.

## VIRA — Complete
### Investigation Workspace — Proof of Concept

Complete is intentionally **not** another questionnaire.

Its planned role is to help a Safety Manager begin with the records already created by Notify, Initiate, Collect, and other available source documents.

The proposed workflow is to:

1. import source records;
2. extract and normalize facts without changing the original wording;
3. preserve the provenance of each fact;
4. identify conflicts, missing information, and unlinked records;
5. allow the Safety Manager to accept, leave unresolved, link, request follow-up, or annotate information;
6. produce a reviewed investigation report that clearly separates reported facts, verified information, unresolved issues, and human decisions.

Complete must not silently choose between conflicting source values or replace Safety Manager judgment.

## Design Principles

VIRA reflects several operating principles:

- **Problem first, platform second.**
- Break a broader process into focused tools with clear jobs.
- Preserve source wording when the information is evidence.
- Make missing information visible instead of pretending the record is complete.
- Keep working drafts, witness evidence, and reviewed reports distinct.
- Preserve provenance so reviewers can see where information came from.
- Use human judgment for conflicts, conclusions, and final review.
- Prototype the smallest useful workflow, test it, then expand only when the concept earns it.

## Current Product Boundary

The current tools are mobile-friendly browser workflows and do not require a native iOS or Android application.

The prototype is intentionally lightweight. It does not currently:

- determine fault, liability, or root cause;
- automatically approve or close an incident;
- replace emergency response;
- replace Safety Manager judgment;
- silently resolve conflicting information;
- maintain a persistent incident database;
- provide offline mode.

## Why the Project Matters

VIRA demonstrates a practical approach to operational technology: identify a real workflow problem, separate it into understandable stages, prototype quickly, preserve the integrity of the underlying information, and keep human judgment in control where the stakes require it.

The project is a working example of using AI-enabled development and lightweight web technology to improve an operational process without beginning with a large systems implementation.

## Confidentiality

This public case study is intentionally company-neutral and high level.

It excludes employer identification, proprietary business logic, internal records, employee or customer information, credentials, claim details, and other organization-sensitive implementation information.

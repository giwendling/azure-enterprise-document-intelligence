# Azure Enterprise Document Intelligence (MVP)

A production-minded, Azure-aligned document pipeline: **ingest → extract → classify → summarize → produce auditable outputs**.

This repository is an MVP designed to look and feel like an enterprise project, while staying simple enough to run and extend.

---

## What problem this solves

Companies receive large volumes of unstructured documents (PDFs, scans, images). Manual processing is slow, inconsistent, and difficult to audit.

This project demonstrates a clean architecture for automating document understanding and preparing results for downstream search and analytics.

---

## What this MVP includes

- Clear Azure-aligned architecture
- Mock-first design (so it works without paid Azure services)
- Structured JSON output artifacts
- A roadmap to integrate real Azure services

---

## Architecture

```mermaid
flowchart LR
  A[Document Source] --> B[Storage]
  B --> C[Orchestration]
  C --> D[OCR and Extraction]
  D --> E[Classification]
  E --> F[Summarization]
  F --> G[(Metadata Store)]
  F --> H[Search Index]
  E --> I[Human Review]
  C --> J[Monitoring]

  B[Azure Blob Storage or Local Folder]
  C[Azure Functions or Local Runner]
  D[Azure AI Document Intelligence]
  F[Azure OpenAI]
  H[Azure AI Search]
  J[Azure Monitor]

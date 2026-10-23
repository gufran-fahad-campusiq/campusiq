# CampusIQ

An AI assistant for college students. Ask it about **regulations** ("What attendance do I need for the end semester exam?") and about **your own marks and attendance**, and get an answer with the source.

> **Status: work in progress.** This repository is built day by day by two students. The table below shows exactly what works today and what is planned.

## The idea

A student has two kinds of questions:

| Kind | Example | Where the answer lives |
|---|---|---|
| Rules | "How many marks do I need to pass?" | College regulation PDFs |
| Personal data | "Which subjects is my attendance below 75% in?" | Database (marks, attendance) |

CampusIQ will route each question to the right tool, combine the results, and answer in plain language. If the answer is not in the documents, it says so instead of guessing.

## Planned architecture

```
 Student question
        |
        v
  [ Planner agent ]  -- decides what is needed
     |           |
     v           v
 [ RAG ]     [ Text-to-SQL ]
 PDFs        marks, attendance
 (hybrid     (read-only, row-level
  search +    security: a student sees
  rerank)     only their own rows)
     |           |
     +-----+-----+
           v
   [ Critic / answer ]  -- checks the answer is supported by the sources
           |
           v
   Answer + sources
```

Planned stack: Python, sentence-transformers / BGE-M3 embeddings, Qdrant, PostgreSQL, LangGraph, FastAPI, Streamlit, Docker, RAGAS-style evaluation on a hand-written test set.

## What works today

| Area | Status |
|---|---|
| Read a text file and split it into chunks with topics | Done (`ai/day2_chunks.py`) |
| Keyword search and its limits | Done (`ai/day2_search.py`) |
| Embeddings and cosine-similarity search over chunks | Done (`ai/day3_embed.py`, `ai/day3_search.py`) |
| "No relevant rule found" using a minimum similarity score | Done (`ai/day3_search.py`) |
| PostgreSQL tables: students, marks, attendance, with JOIN queries | Done (`backend/db/`) |
| Real PDF ingestion with overlapping chunks | Next |
| Hybrid search (keyword + embeddings) and reranking | Planned |
| Text-to-SQL with safety checks | Planned |
| LangGraph agents | Planned |
| API (FastAPI) and chat UI (Streamlit) | Planned |
| Evaluation on a test set | Planned |
| QLoRA fine-tuning (experiment) | Planned |

## Small demo you can run

The current demo searches a few sample college rules by **meaning**, not by exact words. Asking about "minimum presence to sit in finals" finds the 75% attendance rule even though no word matches.

```
cd ai
python -m venv .venv
.venv\Scripts\activate
pip install pymupdf sentence-transformers
python day3_search.py
```

The sample rules in `ai/data/sample_rules.txt` are made up for practice.

## Repository layout

```
ai/        retrieval and AI code (Gufran)
backend/   database and API (Fahad)
notes/     daily learning notes, one PDF per day
```

## Team

- **Gufran** - AI side: chunking, embeddings, retrieval, agents, evaluation
- **Fahad** - data side: PostgreSQL, backend API, app and deployment

Both of us are 3rd-semester AIML students, and this project is how we are learning the stack end to end. The `notes/` folder is our daily log of what we learned and which mistakes we fixed.

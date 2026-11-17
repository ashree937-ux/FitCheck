<div align="center">

# FITCHECK
### A Multi-Agent Readiness & Skill Verification Platform for Computer Science & IT

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/Frontend-React.js%20%7C%20TailwindCSS-61DAFB.svg)](https://react.dev/)
[![Node.js](https://img.shields.io/badge/Backend-Node.js%20%7C%20Express-339933.svg)](https://nodejs.org/)
[![FastAPI](https://img.shields.io/badge/AI%20Core-FastAPI%20%7C%20Python-009688.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%20%7C%20pgvector-4169E1.svg)](https://github.com/pgvector/pgvector)
[![Docker](https://img.shields.io/badge/Infra-Docker%20Compose-2496ED.svg)](https://www.docker.com/)

<p align="center">
  <strong>Bridging the degree-to-execution gap by transforming passive learning into verifiable, execution-backed technical skill capital.</strong>
</p>

</div>

---

## 📌 Mission & Overview

Despite the abundance of free learning resources (documentation, video courses, MOOCs), a critical disconnect persists between theoretical coursework and production-level execution. Industry benchmarks (such as the *India Graduate Skill Index 2025*) indicate that **fewer than 43% of technical graduates possess job-ready skills**. Traditional credentials measure passive metrics like video completion rates and superficial multiple-choice tests, ignoring real codebase execution and architecture.

**FitCheck** is an automated, multi-agent educational verification platform built to validate hands-on engineering competence. Grounded in **Miller’s Educational Pyramid**, **Dr. Phillippa Lally’s habit continuity research**, and **AdaptUI cognitive load balancing**, the platform replaces static syllabi with adaptive workflows that continuously discover, curate, evaluate, and verify developer skills.

---

## 🏗️ System Architecture

FitCheck operates as a decoupled, polyglot microservice network containerized using Docker:

```text
┌────────────────────────────────────────────────────────┐
│                   CLIENT (React.js)                    │
│   Tailwind CSS | React Flow (@xyflow) | Firebase Auth  │
└──────────────────────────┬─────────────────────────────┘
                           │ HTTPS / REST (JWT Bearer Token)
                           ▼
┌────────────────────────────────────────────────────────┐
│             API GATEWAY (Node.js + Express)            │
│   Auth Validation | State Orchestrator | Piston Client │
└─────────────┬────────────────────────────┬─────────────┘
              │ SQL / pgvector             │ HTTP (JSON / Pydantic)
              ▼                            ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│   DATABASE (Postgres)    │  │   AI SERVICE (FastAPI)   │
│ pgvector | DNA Event Log │  │ MAS: ADE, CIE, MIE, EIE  │
│ Materialized State Snap  │  │ Flow Engine | Groq/Gemini│
└──────────────────────────┘  └──────────────────────────┘

```

---

## 🤖 The 6-Agent Multi-Agent System (MAS)

FitCheck coordinates six specialized engines to automate learning and verification:

1. **ADE (Adaptive Decision Engine):** The central supervisor. Orchestrates agent execution, detects pacing drift, and generates explainable curriculum pivot recommendations (**Human-in-the-Loop**).
2. **CIE (Curated Industry Engine):** Generates dynamic skill dependency Directed Acyclic Graphs (DAGs) and manages the **7-Day Calibration Window**.
3. **MIE (Mission Intelligence Engine):** Curates verified technical documentation (MDN, official references), vetted media, and rapid-fire 30-second pop-quizzes.
4. **EIE (Evidence Intelligence Engine):** Evaluates micro-sandboxes via the Piston API, audits macro GitHub repositories via Octokit, and conducts **Code Flow Defense** to verify that developers understand the architecture of what they submit.
5. **RIE (Readiness Intelligence Engine):** Computes an asymptotic **Readiness Score (0 to 95)** weighted against Miller's Pyramid:
   $$\text{Score} = (0.10 \times \text{Knows}) + (0.20 \times \text{Knows How}) + (0.30 \times \text{Shows How}) + (0.40 \times \text{Does})$$
6. **UPE (Universal Progress Engine):** Tracks velocity, consistency, and applies **Dr. Lally’s habit model** to redistribute missed milestones without resetting streaks to zero.

---

## ⚡ Key Features

* **Dual-Track Learning:** Choose between a focused **Topic Sprint** (e.g., Docker, SQL Concurrency, Tree Algorithms) or a comprehensive **Job-Ready Track** (e.g., Backend Engineer, DevOps Specialist, Full-Stack Developer).
* **7-Day Calibration Window:** An adaptive schedule displaying today's tasks plus the next 6 upcoming days. Automatically compresses and recalibrates per-node in real time for short sprints ($\le 7$ days).
* **Daily Forecast:** An action-oriented daily dashboard strictly capped at 3–5 items to prevent curation paralysis (**AdaptUI**).
* **Technical Gym & Code Flow Defense:** Hands-on micro coding tasks executed in isolated sandboxes, paired with flow-comprehension questions to test structural understanding.
* **The DNA Ledger:** Immutable skill audit trail powered by **Event Sourcing** (`dna_events`) and fast JSON **State Projection** (`dna_state`).
* **Non-Punitive Habit Continuity:** 48-hour recovery buffer; missing a day redistributes tasks across upcoming days instead of destroying user streaks.

---

## 🛠️ Tech Stack & Low-Code Tooling

| Tier | Technologies / Libraries Used | Purpose |
| :--- | :--- | :--- |
| **Frontend** | React.js, Tailwind CSS, `@xyflow/react`, `react-calendar-heatmap`, `lucide-react` | Fast, responsive UI with interactive DAG canvas and GitHub-style heatmaps. |
| **API Gateway** | Node.js, Express.js, Firebase Admin SDK, `@octokit/rest`, `resend` | REST gateway, Google OAuth verification, GitHub repository tree ingestion, and transactional habit emails. |
| **AI Microservice**| Python 3.11, FastAPI, Pydantic, Groq SDK (Llama 3.1), Google Gemini Flash | Low-latency agent network and deep architectural code auditing. |
| **Database** | PostgreSQL 16 with `pgvector/pgvector:pg16` | Relational DNA event sourcing and vector similarity matching for industry competencies. |
| **Code Sandbox** | Piston Public API (`https://emkc.org/api/v2/piston`) | Container-isolated, multi-language code execution. |
| **Infrastructure**| Firebase Hosting, Docker, Docker Compose | Production edge delivery and unified local development containers. |

---

## 🚀 Quickstart & Local Setup

# Clone the Repository
```bash
git clone https://github.com/ashree937-ux/FitCheck.git
cd FitCheck
```

# Configure Environment Variables
Copy the template environment file:
```bash
cp .env.example .env
Populate .env with your credentials:
Env
```

# Database Configuration
```bash 
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=fitcheck_db
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fitcheck_db
```

# AI Microservice Keys
```bash 
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

# Services & Authentication
```bash
JWT_SECRET=your_jwt_signing_secret_here
RESEND_API_KEY=your_resend_api_key_here
```
Start Local Infrastructure via Docker
Run the local multi-container network with one command:
```bash
docker compose up --build
```

# 🌐 Service Endpoints
Once the containers are running, access the local services:
| Service | Local Address | Description |
| :--- | :--- | :--- |
| **Client Application (Vite)** | `http://localhost:5173` | Interactive Frontend & Learning Canvas |
| **Node.js API Gateway** | `http://localhost:5000` | REST Endpoints & Authentication Gateway |
| **FastAPI Microservice** | `http://localhost:8000/docs` | Interactive Swagger API Documentation |
| **PostgreSQL (pgvector)** | `localhost:5432` | Relational & Vector Competency Database |

# 📁 Repository Structure

```text 

FitCheck/
├── .github/workflows/ci-cd.yml      # Automated linting & build verification
├── docker-compose.yml               # Local multi-service cluster
├── client/                          # React.js + Tailwind CSS Client (Vite)
│   ├── src/components/              # Common, Roadmap, Gym, Dashboard
│   ├── src/pages/                   # Application views
│   └── src/services/                # API client adapters
├── server/                          # Node.js + Express API Gateway
│   ├── src/controllers/             # Auth, Roadmap, Gym, Track controllers
│   ├── src/models/                  # PostgreSQL queries & migrations
│   └── src/services/dnaService.js   # Event sourcing & state projection engine
└── ai_engine/                       # Python + FastAPI AI Microservice
    ├── app/agents/                  # ADE, CIE, MIE, EIE, RIE, UPE
    ├── app/core/llm_router.py       # Frugal Groq <-> Gemini failover router
    └── app/schemas/                 # Pydantic validation models

```

## 👥 Engineering Team & Ownership
FitCheck is developed and maintained by a 3-engineer peer team:

* **Backend & System Architecture:** Node.js Express Gateway, PostgreSQL + pgvector design, DNA Event Sourcing engine, Piston Sandbox integration.
* **Frontend Engineering:** React.js, Tailwind CSS, AdaptUI implementations, `@xyflow/react` Roadmap Canvas, interactive telemetry.
* **AI & Agent Systems:** Python FastAPI Microservice, 6-Agent MAS Network (ADE, CIE, MIE, EIE, RIE, UPE), Code Flow Defense, LLM Failover Router.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
Code
---

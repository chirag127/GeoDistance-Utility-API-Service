# PinCodeFlow-GeoDistance-Calculation-Python-API

High-performance, domain-driven Python REST API for rapid, accurate distance calculation and route optimization between Indian Pincode locations. Engineered for low-latency and enterprise scalability.

[![CI/CD Status](https://img.shields.io/github/actions/workflow/status/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API/ci.yml?branch=main&style=flat-square&label=CI%2FCD)](https://github.com/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API/actions/workflows/ci.yml)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API?token=<CODECOV_TOKEN>&style=flat-square)](https://app.codecov.io/gh/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API)
[![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![API Framework](https://img.shields.io/badge/API-FastAPI-05998a?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Code Style](https://img.shields.io/badge/Linter-Ruff-000000?style=flat-square&logo=ruff)](https://docs.astral.sh/ruff/)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](LICENSE)

---

## Star this Repository!
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API.svg?style=social&label=Star)](https://github.com/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API/stargazers)

## 1. Overview

PinCodeFlow provides a dedicated microservice layer for geospatial querying, focusing on the highly specific challenge of rapid distance computation between Indian Postal Codes (Pincodes). By leveraging optimized geospatial indexing and adhering to the **Hexagonal Architecture (Ports & Adapters)**, this service guarantees high availability, sub-millisecond query times, and exceptional maintainability.

### 1.1. Core Features

*   **Low Latency API:** Built on FastAPI and Uvicorn for asynchronous, high-throughput request handling.
*   **Hexagonal Design:** Strict separation between API/Infrastructure (Adapters) and Core Business Logic (Domain).
*   **Optimized Distance Kernel:** Utilizes efficient Haversine or Vincenty formulas optimized for Pincode coordinates.
*   **Scalable Caching:** Integration points for Redis/Memcached to cache frequent Pincode lookups and distance results.
*   **Containerized Deployment:** Production-ready Dockerfile for seamless integration into Kubernetes or ECS environments.

## 2. System Architecture (Hexagonal Model)

This project implements the Hexagonal Architecture pattern to ensure the Domain Core remains independent of infrastructure details (e.g., database type, web framework).

mermaid
graph TD
    A[Client/Gateway] --> B(FastAPI Controller: Pincode Endpoints);
    B --> C{Application Service: Distance Usecase};
    C --> D[Domain Core: Pincode Entity & Distance Logic];
    C --> E[Port: GeoSpatial Repository Interface];
    E --> F[Adapter: Pincode Database/Index Storage];
    B --> G[Adapter: Caching Layer];

    subgraph Hexagonal Architecture
        C
        D
        E
    end

    style D fill:#f9f,stroke:#333,stroke-width:2px,color:#333
    style C fill:#ccf,stroke:#333,stroke-width:2px,color:#333
    style E fill:#aaf,stroke:#333,stroke-width:2px,color:#333


## 3. Prerequisites & Setup

This project requires Python 3.11+ and uses `uv` as the ultra-fast package manager and dependency resolver.

### 3.1. Local Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/PinCodeFlow-GeoDistance-Calculation-Python-API.git
    cd PinCodeFlow-GeoDistance-Calculation-Python-API
    

2.  **Install dependencies using `uv`:**
    bash
    # uv replaces pip and virtualenv for speed
    uv venv
    source .venv/bin/activate
    uv sync
    

3.  **Run the development server:**
    bash
    # Uses Uvicorn with automatic reloading
    uv run dev
    # API available at: http://127.0.0.1:8000/docs
    

## 4. API Endpoints

| Method | Endpoint | Description | Status Code | Example Request Body |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/health` | Health check and status ping. | `200 OK` | N/A |
| `POST` | `/api/v1/distance` | Calculates the distance (km) between two Pincodes. | `200 OK` | `{"pincode_a": "110001", "pincode_b": "400001"}` |
| `POST` | `/api/v1/optimize` | Calculates optimized route distance for a list of Pincodes (Traveling Salesperson heuristic). | `200 OK` | `{"pincodes": ["110001", "560001", "400001"]}` |

## 5. Development Scripts

These scripts are defined in `pyproject.toml` and executed via `uv run <command>`:

| Command | Description | Tooling Used |
| :--- | :--- | :--- |
| `dev` | Starts the local API server with hot reloading. | Uvicorn, FastAPI |
| `test` | Executes all unit and integration tests. | Pytest, Coverage |
| `lint` | Lints and formats all source code. | Ruff (Check/Format) |
| `coverage` | Generates HTML coverage report after tests run. | Coverage.py |

---

## 6. 🤖 AI Agent Directives (Operational Mandate)

<details>
<summary><strong>📐 SYSTEM SPECIFICATIONS & ARCHITECTURAL STANDARDS (DECEMBER 2025)</strong></summary>

### 6.1. IDENTITY & PRIME DIRECTIVE

*   **Role:** Senior Principal Software Architect operating under the guidance of the **Apex Technical Authority**.
*   **Objective:** Ensure all code merges adhere to FAANG-level security, performance, and architectural best practices.
*   **Tone:** Highly disciplined, formal, and structured.

### 6.2. CONTEXT-AWARE APEX TECH STACKS

This project is a high-velocity Python service adhering to the **DATA / SCRIPTS / API** standards.

| Component | Tool / Standard | Requirement |
| :--- | :--- | :--- |
| **Runtime** | Python 3.11+ | Strict type hinting and Pydantic v2 validation. |
| **Package Mgr** | `uv` | Must be used for all dependency resolution, environment setup, and script execution. |
| **API Framework** | FastAPI | Asynchronous endpoints, full use of Pydantic models for request/response bodies. |
| **Testing** | Pytest | 100% test coverage for Domain Core logic (Hexagonal inner layer). |
| **Lint/Format** | Ruff | Enforced zero-warnings policy. Configuration via `pyproject.toml`. |

### 6.3. ARCHITECTURAL MANDATES (HEXAGONAL)

1.  **Domain Core Integrity:** The `domain` directory (Entities, Value Objects, Logic) must have **zero external dependencies** outside of standard Python libraries and Pydantic.
2.  **Ports:** All interactions between the Application Layer and external systems (Databases, Caching, External APIs) must be mediated by defined interfaces (`.py` abstract classes or Protocols).
3.  **Adapters:** Infrastructure details (FastAPI controllers, Uvicorn settings, actual database clients) reside solely within the `infrastructure` layer.
4.  **Dependency Rule:** Dependencies must flow *inward*. Infrastructure depends on Application; Application depends on Domain.

### 6.4. CODE PRINCIPLES & SECURITY

*   **SOLID & DRY:** Strict adherence required. Business logic must not be duplicated in controllers.
*   **Data Validation:** All input must be validated using Pydantic models (Input Ports).
*   **Error Handling:** Custom exceptions must be defined in the Domain Core and handled gracefully by Middleware/Exception Handlers in the Adapter layer.

### 6.5. VERIFICATION COMMANDS

The following commands must pass zero-error status before any merge:

bash
# 1. Dependency Check (Clean environment sync)
uv sync --frozen

# 2. Linting and Formatting Check (Zero Errors/Warnings)
uv run lint

# 3. Unit and Integration Tests (Minimum 95% coverage required)
uv run test

# 4. Local API Startup Check
uv run dev

</details>

## 7. License & Contribution

This repository is released under the **CC BY-NC 4.0** License. Contributions are welcome; please see our [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines and architectural mandates.
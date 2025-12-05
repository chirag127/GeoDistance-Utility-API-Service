# GeoDistance-Utility-API-Service

[![Build Status](https://img.shields.io/github/actions/workflow/user/chirag127/GeoDistance-Utility-API-Service/ci.yml?style=flat-square)](https://github.com/chirag127/GeoDistance-Utility-API-Service/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](https://app.codecov.io/github/chirag127/GeoDistance-Utility-API-Service)
[![Tech Stack](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/github/license/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](https://github.com/chirag127/GeoDistance-Utility-API-Service/stargazers)

[![Star⭐](https://img.shields.io/github/watchers/chirag127/GeoDistance-Utility-API-Service?style=social)](https://github.com/chirag127/GeoDistance-Utility-API-Service/watchers)

A high-performance microservice designed for efficient geospatial distance calculations, providing precise APIs for location-based services and logistics.

This service implements the Haversine and Vincenty formulas to offer accurate distance computations between geographical coordinates.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Security](#security)
- [AI Agent Directives](#ai-agent-directives)

---

## Features

- **Dual Formula Support:** Implements both Haversine (for approximate, faster calculations) and Vincenty (for highly precise geodesic calculations on an ellipsoid) formulas.
- **RESTful API:** Exposes endpoints for calculating distances between two points.
- **Scalable Microservice:** Built with Flask for lightweight, efficient operation.
- **Pythonic Implementation:** Leverages modern Python features for clarity and performance.

---

## Architecture

mermaid
graph TD
    A[Client Request] --> B(API Gateway/Load Balancer)
    B --> C{GeoDistance Service}
    C --> D(Distance Calculation Module)
    D --> E[Haversine Formula]
    D --> F[Vincenty Formula]
    E --> G(Result)
    F --> G
    G --> C
    C --> H(Response)
    H --> B
    B --> A


---

## Getting Started

### Prerequisites

- Python 3.10+
- Pipenv or Poetry (for dependency management - **uv is the standard**)

### Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/GeoDistance-Utility-API-Service.git
    cd GeoDistance-Utility-API-Service
    

2.  **Set up the environment using uv:**
    bash
    uv venv
    uv pip install -r requirements.txt
    

---

## Usage

Run the Flask development server:

bash
flask run


The service will be accessible at `http://127.0.0.1:5000` by default.

---

## API Endpoints

### Calculate Distance (Haversine)

*   **Method:** `POST`
*   **URL:** `/distance/haversine`
*   **Request Body (JSON):**
    
    {
        "point1": {"latitude": 40.7128, "longitude": -74.0060},
        "point2": {"latitude": 34.0522, "longitude": -118.2437}
    }
    
*   **Response Body (JSON):**
    
    {
        "distance_km": 3935.74,
        "distance_miles": 2445.52
    }
    

### Calculate Distance (Vincenty)

*   **Method:** `POST`
*   **URL:** `/distance/vincenty`
*   **Request Body (JSON):**
    
    {
        "point1": {"latitude": 40.7128, "longitude": -74.0060},
        "point2": {"latitude": 34.0522, "longitude": -118.2437}
    }
    
*   **Response Body (JSON):**
    
    {
        "distance_km": 3930.15,
        "distance_miles": 2442.05
    }
    

---

## Development

### Principles

- **SOLID:** Maintainable and extensible design.
- **DRY:** Avoid code duplication.
- **YAGNI:** Implement only what is necessary.

### Scripts

| Script        | Description                                      |
| ------------- | ------------------------------------------------ |
| `uv venv`     | Creates a virtual environment.                   |
| `uv pip install -r requirements.txt` | Installs dependencies.                           |
| `flask run`   | Runs the development server.                     |
| `pytest`      | Runs all unit and integration tests.             |
| `ruff format .` | Formats code according to project standards.     |
| `ruff check .`  | Lints code for style and potential errors.       |

---

## Contributing

See the [CONTRIBUTING.md](.github/CONTRIBUTING.md) file for details on how to contribute.

---

## License

This project is licensed under the [CC BY-NC 4.0](LICENSE) License.

---

## Security

See the [SECURITY.md](.github/SECURITY.md) file for information on reporting security vulnerabilities.

---

<details>
<summary>🤖 AI Agent Directives (December 2025 Edition)</summary>

## 1. IDENTITY & PRIME DIRECTIVE
**Role:** Senior Principal Software Architect, Master Technical Copywriter with **40+ years of elite industry experience**. Enforcing FAANG-level standards and the wisdom of "Managing the Unmanageable."
**Context:** Current Date is **December 2025**. Building for the 2026 standard.
**Output Standard:** **EXECUTION-ONLY**. No plans, only executed code, updated docs, and applied fixes.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

---

## 2. INPUT PROCESSING & COGNITION
*   **SPEECH-TO-TEXT INTERPRETATION PROTOCOL:**
    *   **Context:** User inputs may contain phonetic errors (homophones, typos).
    *   **Semantic Correction:** **STRICTLY FORBIDDEN** from executing literal typos. Must **INFER** technical intent based on project context.
    *   **Logic Anchor:** Treat the `README.md` as the **Single Source of Truth (SSOT)**.
*   **MANDATORY MCP INSTRUMENTATION:**
    *   **No Guessing:** Do not hallucinate APIs.
    *   **Research First:** Use `linkup`/`brave` to search for **December 2025 Industry Standards**, **Security Threats**, and **2026 UI Trends**.
    *   **Validation:** Use `docfork` to verify *every* external API signature.
    *   **Reasoning:** Engage `clear-thought-two` to architect complex flows *before* writing code.

---

## 3. CONTEXT-AWARE APEX TECH STACKS (LATE 2025 STANDARDS)
**Directives:** Detect the project type (`pyproject.toml` or `requirements.txt` for Python) and apply the corresponding **Apex Toolchain**.

*   **PRIMARY SCENARIO: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** This project leverages **Python 3.10+**. Key tools include **uv** (for package management and dependency resolution), **Ruff** (for ultra-fast linting and formatting), and **Pytest** (for robust unit and integration testing).
    *   **Architecture:** Adheres to a **Modular Monolith** pattern, ensuring clear separation of concerns for features like geospatial calculation, API interface, and error handling, while maintaining a unified deployment.
    *   **AI Integration:** N/A for this specific project's core function. If integrated, prioritize modular design, clear API contracts, and robust error handling for all AI model interactions.
    *   **API Framework:** Uses `Flask` or `FastAPI` for a powerful and intuitive API interface.
    *   **Geospatial Libraries:** Utilizes `geopy` or equivalent for robust geospatial computations.

*   **SECONDARY SCENARIO A: WEB / APP / EXTENSION (TypeScript) - *Not applicable***

---

## 4. APEX NAMING CONVENTION
*   **Formula:** `<Product-Name>-<Primary-Function>-<Platform>-<Type>`
*   **Format:** `Title-Case-With-Hyphens`
*   **Rules:**
    *   **Length:** 3 to 10 words.
    *   **Keywords:** Must include high-volume terms.
    *   **Forbidden:** NO numbers, NO emojis, NO underscores, NO generic words ("app", "tool") without qualifiers.
    *   **Archival Protocol:** If `action` is "ARCHIVE", a new descriptive name must still be generated for archival purposes.

---

## 5. REPOSITORY INTEGRITY & PURPOSE PIVOT PROTOCOL
*   **Identity Preservation:** Respect existing project type if viable.
*   **PURPOSE PIVOT:** If current purpose is weak or vague, re-imagine as a professional tool.
*   **PROFESSIONAL ARCHIVAL (RETIRED PRODUCT STANDARD):** Archived repos are "Retired Products." Metadata (Name, Description, Topics) must remain professional and dignified.

---

## 6. CHAIN OF THOUGHT (CoT) PROTOCOL
*   **Audit:** Analyze repo content and purpose.
*   **Pivot/Archive Decision:** Determine if a pivot or archival is necessary.
*   **Naming Strategy:** Apply `<Product>-<Function>-<Type>` formula.
*   **Replication Protocol:** Draft `AGENTS.md` directives.
*   **File Generation:** Plan content for all 11 required files.
*   **Final Polish:** Ensure all badges (chirag127, flat-square) and "Standard 11" are present.
*   **Strict Adherence:** Ensure `AGENTS.md` is customized for the specific repository's tech stack.

---

## 7. DYNAMIC URL & BADGE PROTOCOL
*   **Base URL:** `https://github.com/chirag127/<New-Repo-Name>`
*   **Badge URLs:** All Shields.io badges point to the Base URL or specific workflows.
*   **Consistency:** Never use the old repository name in links.

---

## 8. TESTING & VERIFICATION
*   **Unit Testing:** `Pytest` is mandated for all Python projects. Aim for >90% code coverage.
*   **Integration Testing:** Crucial for API services. Use `Pytest` fixtures to simulate external dependencies.
*   **Linting & Formatting:** `Ruff` is the standard for Python. Ensure code adheres to PEP 8 and project-specific style guides.
*   **CI/CD:** GitHub Actions (`ci.yml`) must execute linting, testing, and packaging steps.

---

## 9. LICENSING & COMPLIANCE
*   **Default License:** `CC BY-NC 4.0` unless otherwise specified.
*   **Standard 11:** All repositories must include `README.md`, `PROPOSED_README.md`, `badges.yml`, `LICENSE`, `.gitignore`, `.github/workflows/ci.yml`, `.github/CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE/bug_report.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/SECURITY.md`, and `AGENTS.md`.

---

## 10. CODE QUALITY & ARCHITECTURE MANDATES
*   **Modularity:** Favor smaller, focused modules. Ensure clear separation of concerns.
*   **Readability:** Code must be self-documenting with clear variable names and function signatures.
*   **Error Handling:** Implement robust error handling, especially for I/O operations and external API calls.
*   **Security:** Follow OWASP Top 10 principles. Sanitize all inputs. Never hardcode secrets.

---

## 11. DOCUMENTATION PROTOCOL
*   **README:** Comprehensive overview, usage, and architecture.
*   **AGENTS.md:** Detailed directives for AI agents interacting with the repository.
*   **CONTRIBUTING.md:** Clear guidelines for external contributors.
*   **ISSUE_TEMPLATE / PULL_REQUEST_TEMPLATE:** Standardized formats for issue reporting and PRs.
*   **API Documentation:** If applicable, use tools like Swagger/OpenAPI.

</details>

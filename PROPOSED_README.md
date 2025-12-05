# GeoDistance-Utility-API-Service

[![Build Status](https://img.shields.io/github/actions/workflow/status/chirag127/GeoDistance-Utility-API-Service/ci.yml?style=flat-square)](https://github.com/chirag127/GeoDistance-Utility-API-Service/actions)
[![Code Coverage](https://img.shields.io/codecov/c/github/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](https://app.codecov.io/github/chirag127/GeoDistance-Utility-API-Service)
[![Tech Stack](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)](https://www.python.org/)
[![Lint/Format](https://img.shields.io/badge/Ruff-Enabled-orange?style=flat-square)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/github/license/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/chirag127/GeoDistance-Utility-API-Service?style=flat-square)](https://github.com/chirag127/GeoDistance-Utility-API-Service)

## Revolutionize Your Location-Based Services

A robust, high-performance microservice providing precise geospatial distance calculation APIs. Optimized for efficiency and accuracy, supporting Haversine and Vincenty formulas for mission-critical logistics and location intelligence.

--- 

## Table of Contents

*   [Overview](#overview)
*   [Key Features](#key-features)
*   [Architecture](#architecture)
*   [Getting Started](#getting-started)
*   [Usage](#usage)
*   [Development](#development)
*   [Contributing](#contributing)
*   [License](#license)
*   [AI Agent Directives](#ai-agent-directives) 

--- 

## Overview

This microservice is designed to offer developers a fast and reliable way to compute distances between geographical points. It implements industry-standard formulas, ensuring that applications requiring accurate location data can rely on its API for core calculations.

## Key Features

*   **Haversine Formula:** Accurate distance calculation on a sphere, ideal for most terrestrial applications.
*   **Vincenty's Formulae:** Highly accurate geodesic distance calculation on an ellipsoid, suitable for applications demanding extreme precision.
*   **RESTful API:** Simple and intuitive interface for easy integration.
*   **Microservice Architecture:** Designed for scalability and independent deployment.
*   **Performance Optimized:** Built with efficiency in mind for high-throughput scenarios.

## Architecture

mermaid
graph TD
    A[API Gateway/Client] --> B(GeoDistance Service);
    B --> C{Distance Calculation Logic};
    C -- Haversine --> D[Haversine Implementation];
    C -- Vincenty --> E[Vincenty Implementation];
    B --> F(Response Formatting);
    F --> A;


**Design Principles:**

*   **SOLID:** Each component adheres to the Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles.
*   **DRY (Don't Repeat Yourself):** Core logic is abstracted to avoid duplication.
*   **YAGNI (You Ain't Gonna Need It):** Features are implemented only as required, maintaining a lean and focused codebase.

## Getting Started

### Prerequisites

*   **Python 3.10+:** Ensure you have Python installed.
*   **uv:** Python's modern package and environment manager.

### Installation

1.  **Clone the repository:**
    bash
    git clone https://github.com/chirag127/GeoDistance-Utility-API-Service.git
    cd GeoDistance-Utility-API-Service
    

2.  **Install dependencies using uv:**
    bash
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    

### Running the Service

bash
python src/main.py


## Usage

This service exposes RESTful endpoints for distance calculations. An example using `curl`:

**Calculate distance using Haversine:**

bash
curl -X POST "http://127.0.0.1:5000/distance/haversine" \
     -H "Content-Type: application/json" \
     -d '{
       "point1": {"lat": 40.7128, "lon": -74.0060},
       "point2": {"lat": 34.0522, "lon": -118.2437}
     }'


**Calculate distance using Vincenty:**

bash
curl -X POST "http://127.0.0.1:5000/distance/vincenty" \
     -H "Content-Type: application/json" \
     -d '{
       "point1": {"lat": 40.7128, "lon": -74.0060},
       "point2": {"lat": 34.0522, "lon": -118.2437}
     }'


## Development

### Linting and Formatting

This project uses **Ruff** for extremely fast linting and formatting. To check and apply formatting:

bash
ruff check .
ruff format .


### Testing

Tests are written using **Pytest**. To run the test suite:

bash
pytest


## Contributing

We welcome contributions! Please refer to the [CONTRIBUTING.md](.github/CONTRIBUTING.md) file for detailed guidelines on how to submit your contributions.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. See the [LICENSE](LICENSE) file for more details.

## AI Agent Directives

<details>
<summary>Expand for AI Agent Directives</summary>

This document outlines the directives for AI agents interacting with the `GeoDistance-Utility-API-Service` repository.

### 1. Identity & Prime Directive

*   **Role:** Senior Principal Software Architect, Master Technical Copywriter.
*   **Experience:** 40+ years of elite industry expertise.
*   **Standards:** FAANG-level quality, "Managing the Unmanageable" philosophy.
*   **Output:** **EXECUTION-ONLY**. No plans, only code, docs, and fixes.
*   **Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. Input Processing & Cognition

*   **Speech-to-Text Interpretation:** Infer technical intent; **STRICTLY FORBIDDEN** from executing literal typos. Use `README.md` as the Single Source of Truth (SSOT).
*   **Mandatory MCP Instrumentation:** No hallucinated APIs. Use `linkup`/`brave` for research (Dec 2025 standards, security threats, 2026 trends). Use `docfork` to verify external API signatures. Use `clear-thought-two` for complex flow architecture before coding.

### 3. Context-Aware Apex Tech Stacks (Late 2025 Standards)

*   **Primary Scenario: DATA / SCRIPTS / AI (Python)**
    *   **Stack:** Python 3.10+.
    *   **Tools:** **uv** (package/dependency management), **Ruff** (linting/formatting), **Pytest** (testing).
    *   **Architecture:** Modular Monolith. Ensures clear separation of concerns while maintaining unified deployment.
    *   **AI Integration:** N/A for this specific service (focus is on calculation, not AI-driven data generation or analysis).
    *   **API Framework:** Flask (as implied by existing topics, though not explicitly stated in `base_agents_md_content` for this repo, it's a common Python microservice choice).

### 4. Apex Naming Convention (Star Velocity Engine)

*   **Formula:** `<Product-Name>-<Primary-Function>-<Platform>-<Type>`
*   **Format:** `Title-Case-With-Hyphens`.
*   **Rules:** 3-10 words, high-volume keywords, no numbers/emojis/underscores/generic qualifiers without context.

### 5. README Replication Protocol (The Ultimate Artifact)

*   **Sections:** Visual Authority (Hero Banner, Live Badges), Structural Clarity (BLUF, Architecture, TOC), AI Agent Directives (`<details>` block), Development Standards (Setup, Scripts, Principles).
*   **Badges:** `flat-square` style, `chirag127` username, include Build Status, Code Coverage, Tech Stack, Lint/Format, License, GitHub Stars.

### 6. Chain of Thought (CoT) Protocol

*   **Process:** Audit -> Pivot/Archive Decision -> Naming Strategy -> Replication Protocol -> File Generation -> Final Polish -> Strict Adherence.

### 7. Dynamic URL & Badge Protocol

*   **Base URL:** `https://github.com/chirag127/<New-Repo-Name>`.
*   **Consistency:** All links and badges MUST use the new repository name.
*   **AGENTS.md Customization:** Adapt AI Agent Directives to the repository's specific tech stack (Python, Flask, Ruff, Pytest).

### 8. Repository Specific Directives

*   **Project Name:** `GeoDistance-Utility-API-Service`.
*   **Language:** Python.
*   **Framework:** Flask.
*   **Core Task:** Geospatial distance calculation (Haversine, Vincenty).
*   **Testing:** Utilize Pytest for comprehensive test coverage.
*   **Linting/Formatting:** Employ Ruff for efficient code quality checks.
*   **Dependency Management:** Use uv for robust environment and package management.

</details>

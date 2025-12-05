# Pull Request Template

## Project: GeoDistance-Utility-API-Service

**Please follow this template to help us process your contribution efficiently.**

---


### 1. Summary of Changes

Briefly describe the core purpose of this pull request. What problem does it solve or what feature does it introduce?

*   **Type:** (e.g., `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `perf`, `build`)
*   **Scope:** (e.g., `api`, `geospatial`, `utils`, `config`)
*   **Subject:** Concise description (e.g., `Add Vincenty formula support`)

**Example:** `feat(geospatial): Add Vincenty formula support for high-precision distance calculations`

---


### 2. Motivation and Context

Provide more detail about the reasoning behind these changes. Link to any relevant issues or discussions (e.g., `#123`).

---

### 3. Changes Implemented

*   List the key changes made. Use bullet points for clarity.
*   Mention any new dependencies or significant architectural shifts.

---

### 4. How to Test

Provide step-by-step instructions on how to test your changes. Include specific commands or scenarios.

*   **Setup:** (e.g., `git fetch origin <branch-name>`, `uv pip install -r requirements.dev.txt`)
*   **Execution:** (e.g., `pytest tests/test_geospatial.py::TestVincenty::test_basic_distance`)
*   **Verification:** What should the expected output or behavior be?

---

### 5. Related Pull Requests

List any other open pull requests that are related to this one.

---

### 6. Checklist

*   [ ] I have read and followed the **CONTRIBUTING.md** guidelines.
*   [ ] My code adheres to the project's coding standards and architectural patterns.
*   [ ] I have added or updated relevant unit/integration tests.
*   [ ] My changes do not introduce new linting or formatting errors.
*   [ ] All new and existing functionality is documented.
*   [ ] I have updated the **AGENTS.md** directives if new tools or patterns were introduced.
*   [ ] The changes have been tested locally and pass all relevant tests.

---


### 7. Agent Directives & Verification (Internal Use Only)

This section is for the Apex Technical Authority and AI agents. Please do not modify.

**AGENTS.md Reference:** [AGENTS.md](https://github.com/chirag127/GeoDistance-Utility-API-Service/blob/main/AGENTS.md)

**Verification Commands:**
bash
# Lint & Format Check
ruff check .
ruff format .

# Test Execution
pytest

# Security Audit (Example - replace with actual tool if integrated)
# bandit -r .


**Key Architectural Principles:**
*   **SOLID:** Ensure adherence to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion principles.
*   **DRY:** Avoid redundancy; strive for reusable components.
*   **Modular Design:** Maintain clear separation of concerns, especially between API endpoints, core logic, and data handling.
*   **Pythonic Best Practices:** Follow PEP 8, utilize list comprehensions, context managers, and appropriate data structures.

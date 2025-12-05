# Contributing Guidelines for GeoDistance-Utility-API-Service

Thank you for considering contributing to the **GeoDistance-Utility-API-Service**!

This project adheres to the Apex Technical Authority standards, emphasizing **Zero-Defect, High-Velocity, Future-Proof** development. We aim for professional, well-architected, and maintainable code.

## 1. Code of Conduct

This project follows the Contributor Covenant Code of Conduct. By participating, you are expected to uphold this code. Please report any unacceptable behavior to [conduct@example.com](mailto:conduct@example.com).

## 2. How to Contribute

We welcome contributions in the form of bug reports, feature requests, documentation improvements, and code contributions.

### 2.1. Reporting Bugs

1.  **Search:** Before reporting, please check if a similar bug has already been reported.
2.  **Reproduce:** Try to reproduce the bug with a minimal example.
3.  **Report:** Open an issue in the GitHub repository with the following details:
    *   A clear, descriptive title.
    *   The environment (Python version, OS, etc.).
    *   Steps to reproduce the bug.
    *   Expected behavior.
    *   Actual behavior.
    *   Any relevant logs or screenshots.

### 2.2. Requesting Features

1.  **Search:** Check if the feature has already been requested.
2.  **Detail:** Open an issue with a clear description of the desired feature, its benefits, and any potential implementation ideas.

### 2.3. Submitting Code Contributions

We follow a standard GitHub pull request workflow:

1.  **Fork:** Fork the repository on GitHub.
2.  **Clone:** Clone your forked repository:
    bash
    git clone https://github.com/chirag127/GeoDistance-Utility-API-Service
    cd GeoDistance-Utility-API-Service
    
3.  **Branch:** Create a new branch for your feature or bug fix:
    bash
    git checkout -b feature/your-feature-name
    # or
    git checkout -b bugfix/your-bug-fix-description
    
4.  **Develop:** Make your changes. Ensure your code adheres to the project's standards (see Section 3).
5.  **Test:** Write and run tests to ensure your changes are correct and do not introduce regressions. The primary testing framework is **Pytest**.
    bash
    uv run pytest
    
6.  **Lint & Format:** Ensure your code is clean and follows the formatting rules enforced by **Ruff**.
    bash
    uv run ruff check .
    uv run ruff format .
    
7.  **Commit:** Commit your changes with clear, concise messages:
    bash
    git add .
    git commit -m "feat: Add precise Haversine calculation"
    # or
    git commit -m "fix: Correct error in Vincenty formula implementation"
    
8.  **Push:** Push your branch to your fork:
    bash
    git push origin feature/your-feature-name
    
9.  **Pull Request:** Open a Pull Request from your branch to the `main` branch of the `chirag127/GeoDistance-Utility-API-Service` repository.

## 3. Development Standards & Tooling

This project enforces strict development standards to ensure quality and maintainability, aligning with the Apex Technical Authority's **Late 2025 Standards**.

*   **Language:** Python 3.10+
*   **Package Management:** uv
*   **Linting & Formatting:** Ruff
*   **Testing:** Pytest
*   **API Framework:** Flask (as implied by existing topics and common practice for such microservices).
*   **Architecture:** Modular Monolith, adhering to SOLID principles.
*   **AI Integration:** Not directly applicable to this core utility API, but future integrations should follow strict API contracts and error handling.

### 3.1. Environment Setup

1.  Ensure you have Python 3.10+ installed.
2.  Install `uv`:
    bash
    curl -LsSf https://github.com/astral-sh/uv/releases/download/v0.1.0/uv-linux_x86_64.tar.gz | tar xz --shortcut && sudo mv uv /usr/local/bin
    # (Adjust installation command for your OS/architecture if needed)
    
3.  Clone the repository and navigate to its root directory.
4.  Create a virtual environment and install dependencies:
    bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.\.venv\Scripts\activate`
    uv pip install -r requirements.txt
    uv pip install -r requirements-dev.txt # For development dependencies
    

### 3.2. Running the Service

*   **Development Mode:**
    bash
    uv run python src/app.py
    

## 4. Pull Request Process

*   **Target Branch:** All PRs should target the `main` branch.
*   **Description:** Provide a clear description of your changes, including the problem solved and the approach taken.
*   **Testing:** Ensure all tests pass.
*   **Reviews:** Your PR will be reviewed by maintainers. Be prepared to address feedback.
*   **CI/CD:** Automated checks will run on your PR. Ensure all checks pass before merging.

## 5. Project Structure Overview


GeoDistance-Utility-API-Service/
├── src/
│   ├── __init__.py
│   ├── app.py          # Flask application entry point
│   ├── formulas.py     # Haversine and Vincenty calculations
│   ├── api.py          # API endpoints definition
│   └── utils.py        # Helper utilities
├── tests/
│   ├── __init__.py
│   ├── test_formulas.py
│   └── test_api.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── bug_report.md
    ├── PULL_REQUEST_TEMPLATE.md
    ├── SECURITY.md
    ├── CONTRIBUTING.md
    ├── CI.yml # Renamed from ci.yml for clarity
    ├── badges.yml
    └── AGENTS.md


## 6. Maintaining High Standards

*   **SOLID Principles:** Adhere to Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, and Dependency Inversion.
*   **DRY (Don't Repeat Yourself):** Avoid code duplication.
*   **YAGNI (You Ain't Gonna Need It):** Implement only what is necessary.
*   **Readability:** Write clear, concise, and well-documented code.

By contributing, you agree to uphold these standards and help maintain the quality and longevity of the **GeoDistance-Utility-API-Service**.
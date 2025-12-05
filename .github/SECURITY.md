# Security Policy for GeoDistance-Utility-API-Service

## Supported Versions

We are committed to maintaining a secure project. Support for older versions is detailed below:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

We take security vulnerabilities very seriously. If you find a security issue, please report it promptly using one of the following methods:

1.  **GitHub Security Advisory:** The preferred method is to [create a security advisory](https://github.com/chirag127/GeoDistance-Utility-API-Service/security/advisories/new) on GitHub. This allows us to manage the disclosure process responsibly.
2.  **Email:** Send a detailed email to `security@chirag127.example.com` (please replace with a valid security contact email if available). Include as much information as possible, such as:
    *   A clear description of the vulnerability.
    *   Steps to reproduce the vulnerability.
    *   The affected version(s).
    *   Any potential impact or mitigation strategies.

We will acknowledge receipt of your vulnerability report within **48 hours** and will provide an update on the investigation and remediation timeline.

## Vulnerability Disclosure Policy

*   **Disclosure:** We will not publicly disclose vulnerability details until they have been fixed and users have had a chance to update.
*   **Responsible Disclosure:** We ask that you only exploit vulnerabilities in a way that does not affect other users or data. Please only test against your own data and do not disrupt our services.
*   **No Public Disclosure:** Please do not share vulnerability information publicly or with third parties until we have addressed the issue.

## Security Best Practices (Development Team)

As a Python Flask-based microservice, we adhere to the following security best practices:

*   **Dependency Management:** Regularly update dependencies using `uv` and scan for vulnerabilities using tools integrated with `Ruff` or dedicated security scanners. Use pinned versions in `pyproject.toml`.
*   **Input Validation:** Sanitize and validate all incoming API requests to prevent injection attacks (e.g., SQL injection, command injection). Use robust validation libraries.
*   **API Security:** Implement rate limiting, authentication (if applicable for protected endpoints), and authorization checks.
*   **Error Handling:** Avoid leaking sensitive information in error messages.
*   **Environment Variables:** Manage secrets and sensitive configuration through environment variables and secure storage mechanisms, never hardcoding them.
*   **Secure Defaults:** Configure Flask and related libraries with security best practices in mind (e.g., disabling debug mode in production).
*   **Code Reviews:** All code changes undergo peer review, with a specific focus on security implications.
*   **Testing:** Security testing is integrated into our CI/CD pipeline.

## Communication

For security-related matters, please use the official channels outlined above. For general inquiries, please refer to the project's main repository.
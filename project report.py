Project Report

Automated Web Security Header & CORS Checker

1. Introduction

This project is a Python-based tool used to check common HTTP security headers and basic Cross-Origin Resource Sharing (CORS) settings of a website.

2. Objective

- To automate basic website security checks.
- To identify missing security headers.
- To inspect basic CORS response headers.
- To display scan results in JSON format.

3. Technologies Used

- Python 3
- Requests library
- JSON

4. System Requirements

- Python 3 installed
- Internet connection
- Requests Python library

5. Modules

URL Validation: Checks whether the supplied URL is valid.

Security Header Checker: Checks six common security headers.

CORS Checker: Displays selected CORS response headers.

Report Generator: Displays the results and optionally saves them in JSON format.

6. Implementation

The program sends an HTTP request to the specified website and examines the response headers. It identifies missing security headers and displays the HTTP status code and selected CORS settings.

7. Execution

Install the required library:

"pip install -r requirements.txt"

Run the program:

"python scanner.py https://example.com"

Save results as JSON:

"python scanner.py https://example.com --json report.json"

8. Applications

- Cybersecurity education
- Basic website configuration checks
- Security header awareness
- Authorized security assessments

9. Limitations

This tool checks only selected HTTP response headers. A missing header does not automatically mean that a website is vulnerable. The tool does not perform a complete penetration test.

10. Conclusion

The Automated Web Security Header & CORS Checker demonstrates how Python can automate basic website security checks and produce readable results.

11. References

- Python: https://www.python.org/
- Requests: https://requests.readthedocs.io/
- OWASP: https://owasp.org/
- MDN CORS: https://developer.mozilla.org/docs/Web/HTTP/CORS

Disclaimer

Use this tool only on websites you own or have permission to test.
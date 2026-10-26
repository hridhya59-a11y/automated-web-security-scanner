Automated Web Security Header & CORS Checker

Project Description

Automated Web Security Header & CORS Checker is a Python-based cybersecurity project that checks websites for common HTTP security headers and basic CORS configuration.

Objectives

- To automate basic website security checks.
- To identify missing HTTP security headers.
- To observe basic CORS response settings.
- To generate readable security reports.

Features

- Checks common HTTP security headers.
- Displays HTTP status code.
- Identifies missing security headers.
- Checks basic CORS response headers.
- Supports JSON report generation.
- Handles network errors and timeouts.

Technologies Used

- Python 3
- Requests Library
- JSON

Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

Installation

Install the required Python library:

pip install -r requirements.txt

How to Run

Run the following command:

python scanner.py https://example.com

To save the results as a JSON report:

python scanner.py https://example.com --json report.json

Replace "example.com" with a website you own or have permission to test.

Project Structure

- "scanner.py" - Main Python program
- "requirements.txt" - Required Python library
- "Project_Report.pdf" - Project report
- "README.md" - Project documentation

Applications

- Educational cybersecurity projects
- Basic website configuration reviews
- Security header awareness
- Authorized web security assessments

Limitations

This tool checks selected response headers only. Missing headers do not automatically indicate a vulnerability. CORS results require further validation.

Future Enhancements

- Multiple website scanning
- HTML and CSV report generation
- TLS certificate checking
- Simple web-based interface

Disclaimer

This project is developed for educational purposes and authorized security testing only. Test only websites you own or have permission to assess.

References

- Python: https://www.python.org/
- Requests: https://requests.readthedocs.io/
- OWASP: https://owasp.org/
- MDN CORS: https://developer.mozilla.org/docs/Web/HTTP/CORS

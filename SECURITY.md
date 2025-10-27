# Security Policy

## Supported Versions

We actively support the following versions of this project:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| 1.0.x   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it privately to help us address it quickly.

### How to Report

1. **Email**: Send details to the project maintainer
2. **GitHub**: Use GitHub's private vulnerability reporting feature
3. **Include**: 
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### What to Expect

- **Acknowledgment**: We'll acknowledge receipt within 48 hours
- **Updates**: Regular updates on our investigation progress
- **Timeline**: We aim to address critical vulnerabilities within 7 days
- **Credit**: Security researchers will be credited (if desired)

### Scope

This security policy applies to:
- Main application code
- Dependencies and third-party libraries
- Configuration files
- Documentation that could impact security

### Out of Scope

- Issues in third-party dependencies (report to respective maintainers)
- Social engineering attacks
- Physical security issues

## Security Best Practices

When using this application:

1. **Environment Variables**: Never commit secrets to version control
2. **Dependencies**: Keep all dependencies up to date
3. **Input Validation**: Be cautious with user inputs in production
4. **HTTPS**: Always use HTTPS in production deployments
5. **Authentication**: Implement proper authentication for sensitive data

## Automated Security

We use automated tools to help maintain security:

- **Dependabot**: Automatic dependency updates
- **CodeQL**: Static code analysis
- **Security advisories**: GitHub security alerts

## Contact

For security-related questions or concerns, please reach out through the appropriate channels mentioned above.

Thank you for helping keep our project secure! 🔒
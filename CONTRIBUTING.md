# Contributing to Streamlit Cheat Sheet

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

### Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using GitHub's [issues](../../issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](../../issues/new); it's that easy!

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Feature Requests

We welcome feature requests! Please open an issue with:

- Clear description of the feature
- Why you think it would be useful
- Any examples or mockups if applicable

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/hakkache/Streamlit_cheatsheet.git
   cd Streamlit_cheatsheet
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_cheatsheet.py
   ```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small
- Use type hints where possible

## Adding New Features

### Adding New Sections to the Cheat Sheet

1. Add your new section function in `streamlit_cheatsheet.py`
2. Follow the existing pattern:
   ```python
   def show_new_section():
       st.markdown('<div class="section-header">🆕 New Section</div>', unsafe_allow_html=True)
       
       # Your content here
       st.write("Section content...")
       
       # Code examples
       with st.expander("📝 Code Example"):
           st.code('''
           # Your code example
           st.write("Hello World")
           ''', language='python')
   ```

3. Add the section to the main function
4. Update the table of contents

### Adding New Examples

1. Create your example in `advanced_examples.py` or `multi_page_demo.py`
2. Follow the existing structure and styling
3. Include clear documentation and comments
4. Add error handling where appropriate

## Documentation

- Update README.md for any new features
- Add docstrings to new functions
- Include code examples in documentation
- Keep language clear and beginner-friendly

## Testing

Before submitting:

1. Test your changes locally
2. Ensure the app runs without errors
3. Check that all examples work as expected
4. Test on different screen sizes if UI changes were made

## License

By contributing, you agree that your contributions will be licensed under its MIT License.

## References

This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md).
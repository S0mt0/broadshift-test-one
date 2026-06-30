## Website Tested

https://www.talktosomto.xyz/contact

## Tools

- Python
- Selenium
- pytest
- uv

## What the Test Does

The test performs the following steps:

1. Opens the contact page in Chrome.
2. Waits for the form fields to load.
3. Fills in the name, email, work type, timeline, budget, and message fields.
4. Submits the form.
5. Checks that a success message appears after submission.

## Setup

Install the project dependencies:

```bash
uv sync
```

If Selenium is not already installed, add it with:

```bash
uv add selenium pytest
```

## Run the Test

Run the test with:

```bash
uv run pytest
```

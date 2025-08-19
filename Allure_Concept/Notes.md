# Allure Report Generation with Pytest

## What is Allure?
Allure is a flexible, lightweight test reporting tool that shows a clear representation of what has been tested. It integrates with popular test frameworks like Pytest.

## Why Use Allure?
- Provides visually rich, interactive test reports.
- Supports step-by-step logging and attachments.
- Helps in tracking test history and flaky tests.
- Useful for both manual and automated QA teams.

## How to Generate Allure Reports with Pytest

### 1. Install Allure and Pytest Plugin
```sh
pip install allure-pytest
```

### 2. Add Allure Steps in Your Tests
Use `allure.step()` to log steps in your test functions:
```python
import allure

def test_example():
    with allure.step("Step description"):
        # test logic here
        pass
```

### 3. Run Tests and Generate Allure Results
Run your tests with the `--alluredir` option to generate result files:
```sh
pytest --alluredir=allure-results
```

### 4. Generate the Allure HTML Report
After running tests, generate the HTML report:
```sh
allure serve allure-results
```
or
```sh
allure generate allure-results -o allure-report
allure open allure-report
```

## Use Case Example

Suppose you have automated tests for a web application. By integrating Allure:
- Each test step is logged and visible in the report.
- Skipped, failed, and passed tests are clearly shown.
- Developers and QA can quickly identify where and why a test failed.
- Attachments (screenshots, logs) can be added for failed steps.

## References
-
# Pytest

## Naming Convention of Pytest

1. File name should start with test_ or end with _test
2. Class name should start with Test
3. Method name should start with test_

## Ways to execute the code in pytest 

1. Run all test in specific files_path
```python
pytest -v -s 
```

2. Run test in module or in test file
```python
pytest -v -s test_pyex1.py
```

3.Only run test_method in test_module.py
```python
pytest -v -s test_pyex2.py::test_m1
```
## Short Notes

+ -v :-> Verbose (It is an argument which is used to report more information about an operation in your program )

+ -s :-> to print statements

## Pytest Rerun failures
1. Install Package (pip install rerunfailures)
2. To uninstall the package type : pip uninstall rerunfailures
3. To check whether package is installed or nor type : pip list
4. Add the pytest marker on top of the test method


# Pytest Fixtures - Quick Notes

- **Fixtures** are functions that provide setup and teardown code for tests.
- Use the `@pytest.fixture` decorator to define a fixture.
- Fixtures can have different **scopes**:  
  - `function` (default): runs before each test function  
  - `class`: runs once per test class  
  - `module`: runs once per module  
  - `session`: runs once per test session
- Fixtures can be **autouse** (applied automatically to tests) or explicitly requested by name.
- Use `yield` in a fixture to separate setup and teardown code.
- Fixtures can be **parameterized** to run tests with different data.
- Deprecated: `@pytest.yield_fixture` (use `@pytest.fixture` with `yield` instead).
- Fixtures can depend on other fixtures by including them as arguments.

**Example:**
```python
import pytest

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    print("Setup")
```



# conftest.py in Pytest - Quick Notes

- **conftest.py** is a special configuration file used by pytest.
- Place `conftest.py` in your test directory to share fixtures and hooks across multiple test files.
- Fixtures defined in `conftest.py` are automatically discovered and available to all tests in the same directory and subdirectories.
- No need to import fixtures from `conftest.py`—pytest finds them automatically.
- Useful for defining **common fixtures**, **hooks**, and **plugins** for your test suite.
- You can have multiple `conftest.py` files in different directories for different scopes.
- Avoid importing `conftest.py` directly in your test files.

**Example:**
```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def db_connection():
    # setup code
    yield
    # teardown code
```
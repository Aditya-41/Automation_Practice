# Pytest

## Naming Convention of Pytest

1. File name should start with test_ or end with _test
2. Class name should start with Test
3. Method name should start with test_

## Ways to execute the code in pytest 

1. Run all test in specific files_path
```python
py.test -v -s files_path  
```

2. Run test in module or in test file

```python
py.test -v -s files_path/filename.py
```
3.Only run test_method in test_module.py
```python
py.test -v -s files_path/filename.py::test_method
```
## Short Notes

* -v :-> Verbose (It is an argument which is used to report more information about an operation in your program )

* -s :-> to print statements

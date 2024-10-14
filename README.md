Python API Automation Framework

Tech Stack
- Python 3.12
- Requests - HTTP Requests
- Pytest - Testing Framework
- Reporting- Allure Report, Pytest HTML
- Test Data - CSV, Excel, JSON, Faker
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)


How to install all the packages
```
pip install requests pytest pytest-html faker allure-pytest jsonschema
```

How to run your testcase parallel
```
pip install pytest-xdist
```
How to run basic test with allure report

```
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s -v
```
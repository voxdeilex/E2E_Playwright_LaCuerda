+-------------------------------------------------------+
 E2E Automated Testing with Playwright, Python & Pytest
+-------------------------------------------------------+


This repository contains an end-to-end (E2E) automated testing project using Playwright, Python, Pytest and Allure reports.  
The goal of this project is to demonstrate a complete QA Automation test case implementation using Playwright and Python, following best practices for end-to-end testing, project organization, and reporting.

---

## Features
- Automated browser testing with Playwright
- Cross-browser execution (Chromium, Firefox, WebKit)
- Test execution with Pytest
- Allure reporting integration
- Modular and scalable test structure

---

## Installation

### 1. Install dependencies

pip install -r requirements.txt

### 2. Install Playwright browsers

playwright install

---

### Run tests in default browser:

pytest -v

### Run tests in all browsers:

pytest -v --browser chromium --browser firefox --browser webkit

---

#### Allure Reports ####

### Generate test results:

pytest --alluredir=allure-results

#### View report: ####

allure serve allure-results

---

#### Project Structure ####

E2E_Playwright_LaCuerda/
│── conftest.py
│── Test_lacuerda/
│ └── test_index.py
│── requirements.txt
│── README.md


---

## Author ##
**Ivan Huerta**  
GitHub: https://github.com/voxdeilex

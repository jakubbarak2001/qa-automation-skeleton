# QA Automation Skeleton (Pytest + Playwright + Allure)

[![tests](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml/badge.svg)](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml)

A minimal **QA automation framework skeleton** using:
- **Pytest** as the test runner  
- **Playwright** for browser automation  
- **Page Object Model (POM)** structure  
- **Allure** for reporting  

This repo is intended as a blueprint for building scalable UI test automation.

---

### Repo Baseline & Naming

- **Repo name**: `qa-automation-skeleton` — baseline project for automated UI testing.  
  Combines Python + Playwright + Pytest + Allure as a foundation for scalable QA.

- **Naming conventions**:
  - Files & directories: `snake_case` (e.g., `test_homepage.py`, `test_login.py`)
  - Classes: `PascalCase` (e.g., `HomePage`, `LoginPage`)
  - Constants: `UPPER_SNAKE_CASE`

---

### Features

- ✅ Page Object Model with `HomePage` and `LoginPage` skeletons  
- ✅ Fixtures (`browser`, `page`, `base_url`) in `conftest.py`  
- ✅ Single-command execution using Docker Compose for reproducible runs.
- ✅ Ready-to-run with GitHub Actions CI and Allure reporting  
- ✅ testing conducted via `https://www.saucedemo.com/`

---

## Quickstart (local)

This project uses Docker Compose to manage the testing environment, 
ensuring tests run consistently without requiring you to install
Python, Java, or browser dependencies locally.
### Prerequisites

1. Git (to clone the repo)
2. Docker (installed and running)

### 1. Build and run the Full Pipeline

Execute this single command from the project root. 
It will build the test environment, run all Pytest cases, 
and automatically serve the interactive Allure Report.

`docker compose up --build`

The Allure Report will be accessible in your browser at: 

http://localhost:8080

### 2. Run Specific test suites (Advanced)
If you wish to run only specific tests (like just UI tests), 
you can pass the Pytest arguments directly 
to the Docker Compose service.

**Run UI Tests Only**

This executes tests marked with @pytest.mark.ui

`docker compose run --rm tester -m ui`

**Run API Tests Only**

This executes tests marked with @pytest.mark.api

`docker compose run --rm tester -m api`

**Run All Tests (Quiet Mode)**

This executes all tests while minimizing console output.

`docker compose run --rm tester -q`

After running a specific suite, 
you can manually start the Allure server to view the results:

`docker compose up allure-server`

### 3. Clean Up
To stop the running services and clean up the network:

`docker compose down`
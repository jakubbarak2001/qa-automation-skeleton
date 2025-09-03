# QA Automation Skeleton (Pytest + Playwright + Allure)

[![tests](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml/badge.svg)](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml)

A minimal **QA automation framework skeleton** using:
- **Pytest** as the test runner  
- **Playwright** for browser automation  
- **Page Object Model (POM)** structure  
- **Allure** for reporting  

This repo is intended as a blueprint for building scalable UI test automation.

---

## Repo Baseline & Naming

- **Repo name**: `qa-automation-skeleton` — baseline project for automated UI testing.  
  Combines Python + Playwright + Pytest + Allure as a foundation for scalable QA.

- **Naming conventions**:
  - Files & directories: `snake_case` (e.g., `home_page.py`, `test_login.py`)
  - Classes: `PascalCase` (e.g., `HomePage`, `LoginPage`)
  - Constants: `UPPER_SNAKE_CASE`
  - Branches: `week<number>/<topic>` (e.g., `week2/baseline`)

---

## Features

- ✅ Page Object Model with `HomePage` and `LoginPage` skeletons  
- ✅ Fixtures (`browser`, `page`, `base_url`) in `conftest.py`  
- ✅ Ready-to-run with GitHub Actions CI and Allure reporting  
- ✅ testing conducted via `https://www.saucedemo.com/`

---

# Quickstart (local)

## Create & activate virtual environment

- **Windows (PowerShell)**:
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# **Linux / macOS (bash/zsh)**:
python3 -m venv .venv
source .venv/bin/activate


# **Install dependencies**:
pip install -r requirements.txt
python -m playwright install


# **Run tests**:
pytest -q


# **Generate Allure report**:
pytest --alluredir=reports/allure-results
allure serve reports/allure-results


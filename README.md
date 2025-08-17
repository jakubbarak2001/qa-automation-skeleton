# QA Automation Skeleton (Pytest + Playwright + Allure)

[![tests](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml/badge.svg)](https://github.com/jakubbarak2001/qa-automation-skeleton/actions/workflows/tests.yml)

A minimal **QA automation framework skeleton** using:
- **Pytest** as the test runner  
- **Playwright** for browser automation  
- **Page Object Model (POM)** structure  
- **Allure** for reporting  

This repo is intended as a blueprint for building scalable UI test automation.

---

## Features
- ✅ Page Object Model with `HomePage` and `LoginPage` skeletons  
- ✅ Fixtures (`browser`, `page`, `base_url`) in `conftest.py`  
- ✅ Example smoke test (homepage) + placeholder login test  
- ✅ Ready-to-run with GitHub Actions CI and Allure reporting  

---

## Quickstart (local)

1. Create & activate venv, install dependencies:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   py -m playwright install

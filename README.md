# QA Automation Skeleton (Pytest + Playwright)

**Quickstart (local):**
1. `python -m venv .venv && . .venv/bin/activate` (Windows: `.venv\\Scripts\\activate`), then `pip install -r requirements.txt` and `python -m playwright install`
2. `pytest` (runs the placeholder test against `https://example.com`)
3. Optional report: `pytest --alluredir=allure-results && allure serve allure-results`

---

## What you get
- **Page Object Model** (`pages/`): `HomePage`, `LoginPage` (skeletons).
- **Fixtures** (`conftest.py`): `browser`, `page`, `base_url` (override with `BASE_URL` env var).
- **Tests** (`tests/`): one smoke test, one skipped login test placeholder.

## Change the base URL
```
export BASE_URL=https://your-app.local
pytest
```

## GitHub Actions (optional)
A basic workflow is included to run tests on pushes.

## Notes
- The smoke test uses `https://example.com` and checks the `<h1>` is visible. Replace with your app later.
- The login test is deliberately **skipped** until you wire real selectors/route.
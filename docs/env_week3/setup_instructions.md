## 1. Clone the repo
git clone https://github.com/jakubbarak2001/qa-automation-skeleton.git
cd qa-automation-skeleton

## 2. Create virtual environment
py -m venv .venv
.\.venv\Scripts\Activate.ps1

## 3. Install dependencies
pip install -r requirements.txt
python -m playwright install 

## 4. Run tests
pytest - q
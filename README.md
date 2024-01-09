NBA players Fast API Testings

- Technologies used:
  - Docker
  - Fast API
  - Tox
  - SQL Alchemy
  - POSTGRES
  - Pyway
  - uvicorn

Local setup:
1. Create a virtual env
2. `pip install -r requirements.txt`
3. Install postgres

Run locally:
- `uvicorn main:app --reload`

Run migrations
doc: https://pypi.org/project/pyway/
- `pyway validate`
- `pyway migrate`

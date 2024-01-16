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

Run with docker:
- `docker build -t fast-api-image .`
- `docker run --name fast-api-containter -p 80:80 fast-api-image`

Run migrations
doc: https://pypi.org/project/pyway/
- `pyway validate`
- `pyway migrate`

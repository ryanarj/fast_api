NBA players Fast API Testings

- Technologies used:
  - Docker
    - For containerization
  - Fast API
    - For backend API infrastructure
  - Tox
    - For testing dynamically
  - SQL Alchemy
    - Query layer for data
  - POSTGRES
    - Relational DB for data
  - Pyway
    - For the migration of those data tables
  - uvicorn
    - To spin up a server locally

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

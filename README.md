# EU Unemployment Pipeline

ETL pipeline extracts monthly unemployment data for Germany from the Eurostat API, transforms it, and loads it into a PostgreSQL database.

## Stack
- Python 3.11
- PostgreSQL 16
- pandas, SQLAlchemy, request, python-dotenv

## Pipeline
1. **Extract** - Pulls data from Eurostat Rest API
2. **Transform** - Parses dates, adds country code, validates nulls
3. **Load** - Loads into PostgreSQL via SQLAlchemy

## Setup
```bash
pip install -r requirements.txt

Create a `.env` file with:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=eu_unemployment
DB_USER=postgres
DB_PASSWORD=your_password

## Run
```bash
python src/extract.py
python src/transform.py
python src/load.py
```

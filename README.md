# FlyHighBuilder

Database and API for **Haikyuu Fly High** character builds, skills, memories, and team optimization.

## Setup

### Prerequisites
- Python 3.x
- PostgreSQL

# Create virtual environment
python -m venv .venv

# Activate
.venv\Scripts\Activate.ps1

# Install dependencies
pip install fastapi sqlalchemy psycopg2-binary

## Database Tables

Schema documentation [here](https://docs.google.com/document/d/1SzFKvQpeVtxyhcw7e6F4aPQ_R297B7JgZACA-M1I2Tg/edit?usp=sharing)

Curently contains tables from branch 
- characters-schemas
- skills-resonance-schema
- skills-tags-schema
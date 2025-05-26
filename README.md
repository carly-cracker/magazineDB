# Articles Code Challenge

A Python application that models **Authors**, **Articles**, and **Magazines** using raw SQL with a SQLite database. This project emphasizes object-oriented programming, relational database design, and raw SQL operations—without using any ORM like SQLAlchemy.

---

## Project Overview

This project models a classic many-to-many publishing relationship:

- An **Author** can write many **Articles**.
- A **Magazine** can publish many **Articles**.
- An **Article** belongs to both one **Author** and one **Magazine**.
- Therefore, the Author–Magazine relationship is many-to-many through **Articles**.

---

## Features

- Full CRUD operations using raw SQL (`sqlite3`)
- OOP classes for `Author`, `Article`, and `Magazine`
- Relationship methods like `author.articles()` and `magazine.articles()`
- Unit testing with `pytest`
- SQLite3 persistence with manually managed schema

---

## 🧱 Database Schema

```sql
-- schema.sql
* authors: id, name, email, location, category
* magazines: id, name, category
* articles: id, title, content,author_id, magazine_id    

## Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` for installing dependencies
- Git for version control
- sqlite3 command-line tool (usually comes with Python)

1. **Create virtual environment**:
   ```bash
   pipenv install 
   pipenv shell 
   ```
2. **Install dependencies**:
   ```bash
     pip install pytest
     ```
3. **Setup database**:
    ```bash
     python scripts/setup_db.py
     ```
4. **Run tests**:
   ```bash
     pytest
     ```
5. **Debug interactively**:
   ```bash
     python -m lib.debug
     ```
6. **Run CLI tool**:
    ```bash
      python scripts/run_queries.py
      ```
7. **Initialize the database**
    ```bash
       sqlite3 lib/db/database.db < schema.sql
    ```
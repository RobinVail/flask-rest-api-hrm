# Flask HRM Application

This repository contains a Flask application that connects to a MySQL database to manage HRM (Human Resource Management) data. The application provides RESTful API endpoints to retrieve, add, update, and delete employee information and skills. It also includes unit tests to ensure the functionality of the endpoints.

## Table of Contents

- [Flask HRM Application](#flask-hrm-application)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [API Endpoints](#api-endpoints)
  - [Running Tests](#running-tests)
  - [License](#license)

## Features

- Retrieve all HRM data
- Retrieve HRM data by employee ID
- Retrieve employee department assignments
- Add new skills
- Update existing skills
- Delete skills
- Supports JSON and XML response formats

## Requirements

- Python 3.x
- Flask
- Flask-MySQLdb
- MySQL server

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Set up a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    - Ensure MySQL server is running.
    - Create a database named `hrm`.
    - Create the necessary tables using the provided schema.

## Configuration

Update the MySQL configuration in `app.py` with your database credentials:

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "yourpassword"
app.config["MYSQL_DB"] = "hrm"

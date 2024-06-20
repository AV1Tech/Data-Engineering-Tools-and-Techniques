```markdown
# Apache Airflow

Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It allows you to orchestrate complex computational workflows and data processing pipelines.

## Table of Contents

- [Apache Airflow](#apache-airflow)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Installing Apache Airflow](#installing-apache-airflow)
    - [Initialize the Database](#initialize-the-database)
    - [Creating an Admin User](#creating-an-admin-user)
  - [Starting Airflow](#starting-airflow)
    - [Starting the Web Server](#starting-the-web-server)
    - [Starting the Scheduler](#starting-the-scheduler)
  - [Using Airflow](#using-airflow)
    - [Creating a DAG](#creating-a-dag)
    - [Running a DAG](#running-a-dag)
  - [Common Issues](#common-issues)
  - [Useful Commands](#useful-commands)
  - [References](#references)

## Features

- Dynamic: Airflow pipelines are defined in Python, allowing for dynamic pipeline generation.
- Scalable: It has a modular architecture and uses a message queue to orchestrate an arbitrary number of workers.
- Extensible: Easily define your own operators and extend libraries.
- Elegant: Airflow pipelines are lean and explicit. Parameterizing your scripts is built into its core.

## Installation

### Prerequisites

- Python 3.6+ (Python 3.10 recommended)
- pip
- Virtual environment (optional but recommended)

### Installing Apache Airflow

1. **Create and activate a virtual environment** (optional but recommended):
   ```sh
   python3 -m venv airflow_venv
   source airflow_venv/bin/activate
   ```

2. **Install Apache Airflow**:
   ```sh
   export AIRFLOW_HOME=~/airflow
   pip install "apache-airflow==2.6.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.2/constraints-3.10.txt"
   ```

### Initialize the Database

1. **Initialize the database**:
   ```sh
   airflow db init
   ```

2. **Migrate the database** (if required):
   ```sh
   airflow db migrate
   ```

### Creating an Admin User

Create an admin user to access the Airflow UI:
```sh
airflow users create \
   --username admin \
   --firstname FIRST_NAME \
   --lastname LAST_NAME \
   --role Admin \
   --email admin@example.com
```

## Starting Airflow

### Starting the Web Server

Run the following command to start the Airflow web server:
```sh
airflow webserver --port 8080
```

If port 8080 is in use, specify an alternative port, e.g., 8081:
```sh
airflow webserver --port 8081
```

### Starting the Scheduler

In a new terminal window or tab, start the scheduler:
```sh
airflow scheduler
```

## Using Airflow

### Creating a DAG

DAGs (Directed Acyclic Graphs) are created in Python scripts. Here’s an example of a simple DAG:

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval=timedelta(days=1),
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> end
```

Save this file in the `$AIRFLOW_HOME/dags` directory, e.g., `~/airflow/dags/example_dag.py`.

### Running a DAG

1. Open the Airflow web UI by navigating to `http://localhost:8080` (or your specified port) in your web browser.
2. Enable the DAG by toggling the switch next to the DAG name.
3. Trigger the DAG by clicking the "Trigger DAG" button.

## Common Issues

1. **Port already in use**: Change the port using the `--port` option when starting the web server.
2. **Database not initialized**: Ensure you've run `airflow db init`.
3. **Scheduler not running**: Make sure the scheduler is started in a separate terminal.

## Useful Commands

- Initialize the database:
  ```sh
  airflow db init
  ```
- Create an admin user:
  ```sh
  airflow users create --username admin --firstname FIRST_NAME --lastname LAST_NAME --role Admin --email admin@example.com
  ```
- Start the web server:
  ```sh
  airflow webserver --port 8080
  ```
- Start the scheduler:
  ```sh
  airflow scheduler
  ```

## References

- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Airflow GitHub Repository](https://github.com/apache/airflow)
- [Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
```

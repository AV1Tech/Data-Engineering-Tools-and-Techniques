# End-to-End Data Pipeline Project: Real-Time Retail Analytics

This project aims to create a real-time retail analytics pipeline using Apache Airflow, Kafka, Snowflake, Spark, and Power BI. The goal is to provide actionable insights for a retail business by processing and analyzing sales data in real-time, enabling the business to make data-driven decisions.

## Table of Contents

- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Components and Technologies](#components-and-technologies)
- [Step-by-Step Implementation](#step-by-step-implementation)
  - [1. Setting Up Kafka](#1-setting-up-kafka)
  - [2. Configuring Apache Airflow](#2-configuring-apache-airflow)
  - [3. Integrating Snowflake](#3-integrating-snowflake)
  - [4. Using Apache Spark](#4-using-apache-spark)
  - [5. Visualizing Data with Power BI](#5-visualizing-data-with-power-bi)
- [Conclusion](#conclusion)

## Project Overview

The real-time retail analytics pipeline will capture sales data from point-of-sale (POS) systems, process the data in real-time, store it in a data warehouse, perform advanced analytics, and visualize the results in a BI tool. The pipeline will enable real-time monitoring of sales performance, inventory levels, and customer behavior.

## Architecture


## Components and Technologies

1. **Apache Kafka**: For real-time data streaming.
2. **Apache Airflow**: For orchestrating and scheduling data pipeline tasks.
3. **Snowflake**: For data storage and warehousing.
4. **Apache Spark**: For data processing and analytics.
5. **Power BI**: For data visualization and business intelligence.

## Step-by-Step Implementation

### 1. Setting Up Kafka

**Objective**: Stream sales data from POS systems to Kafka topics.

1. **Install Kafka**:
   - Download and extract Kafka binaries from the [official website](https://kafka.apache.org/downloads).
   - Start ZooKeeper and Kafka server:
     ```sh
     bin/zookeeper-server-start.sh config/zookeeper.properties
     bin/kafka-server-start.sh config/server.properties
     ```

2. **Create Kafka Topics**:
   ```sh
   bin/kafka-topics.sh --create --topic sales_data --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
   ```

3. **Produce and Consume Messages**:
   - Simulate sales data using a Kafka producer script (e.g., `sales_producer.py`).
   - Verify messages using a Kafka consumer script (e.g., `sales_consumer.py`).

### 2. Configuring Apache Airflow

**Objective**: Schedule and manage data pipeline tasks.

1. **Install Airflow**:
   ```sh
   pip install apache-airflow
   ```

2. **Initialize Airflow Database**:
   ```sh
   airflow db init
   ```

3. **Create Airflow DAG**:
   - Define tasks for consuming Kafka messages, processing data, and loading data into Snowflake.
   - Example DAG (`retail_analytics_dag.py`):
     ```python
     from airflow import DAG
     from airflow.operators.dummy_operator import DummyOperator
     from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
     from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator
     from datetime import datetime

     default_args = {
         'owner': 'airflow',
         'depends_on_past': False,
         'start_date': datetime(2024, 1, 1),
         'retries': 1,
     }

     with DAG('retail_analytics', default_args=default_args, schedule_interval='@hourly') as dag:
         start = DummyOperator(task_id='start')

         process_data = SparkSubmitOperator(
             task_id='process_data',
             application='/path/to/spark_job.py',
             conn_id='spark_default',
             executor_memory='4G',
             executor_cores=2,
             num_executors=2,
         )

         load_to_snowflake = S3ToSnowflakeOperator(
             task_id='load_to_snowflake',
             snowflake_conn_id='snowflake_default',
             stage='@my_stage',
             table='sales_data',
             file_format='(type = csv)',
         )

         end = DummyOperator(task_id='end')

         start >> process_data >> load_to_snowflake >> end
     ```

4. **Start Airflow Scheduler and Web Server**:
   ```sh
   airflow scheduler
   airflow webserver
   ```

### 3. Integrating Snowflake

**Objective**: Store processed sales data in Snowflake for further analysis.

1. **Create Snowflake Database and Table**:
   ```sql
   CREATE DATABASE retail_analytics;
   CREATE SCHEMA sales;
   CREATE TABLE sales_data (
       id INTEGER,
       product STRING,
       quantity INTEGER,
       price FLOAT,
       sales_time TIMESTAMP
   );
   ```

2. **Load Data into Snowflake**:
   - Use Airflow tasks to load data from Kafka to Snowflake.
   - Verify data in Snowflake:
     ```sql
     SELECT * FROM sales.sales_data;
     ```

### 4. Using Apache Spark

**Objective**: Process and analyze sales data using Spark.

1. **Install Spark**:
   ```sh
   pip install pyspark
   ```

2. **Spark Job for Data Processing** (`spark_job.py`):
   ```python
   from pyspark.sql import SparkSession

   spark = SparkSession.builder \
       .appName("RetailAnalytics") \
       .getOrCreate()

   # Read data from Kafka
   sales_df = spark \
       .read \
       .format("kafka") \
       .option("kafka.bootstrap.servers", "localhost:9092") \
       .option("subscribe", "sales_data") \
       .load()

   # Process data
   sales_df = sales_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

   # Write processed data to S3 or directly to Snowflake
   sales_df.write \
       .format("csv") \
       .option("header", "true") \
       .save("s3a://your-bucket/sales_data/")
   ```

3. **Submit Spark Job**:
   ```sh
   spark-submit --master yarn /path/to/spark_job.py
   ```

### 5. Visualizing Data with Power BI

**Objective**: Create interactive dashboards and reports using Power BI.

1. **Connect Power BI to Snowflake**:
   - Use the Snowflake connector in Power BI to connect to the Snowflake database.
   - Import the `sales_data` table.

2. **Create Reports and Dashboards**:
   - Design interactive visualizations to monitor sales performance, inventory levels, and customer behavior.
   - Share dashboards with stakeholders for real-time insights.

## Conclusion

This end-to-end data pipeline project demonstrates how to leverage Apache Airflow, Kafka, Snowflake, Spark, and Power BI to build a real-time retail analytics system. By integrating these technologies, you can process and analyze large volumes of data in real-time, providing valuable insights to drive business decisions. This architecture can be adapted and scaled to fit various use cases and industry requirements.
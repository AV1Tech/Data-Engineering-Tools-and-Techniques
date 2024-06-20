```markdown
# Apache Kafka Tutorial

This project provides a step-by-step guide to setting up and using Apache Kafka for basic message streaming operations.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Starting ZooKeeper and Kafka Broker](#starting-zookeeper-and-kafka-broker)
- [Creating a Topic](#creating-a-topic)
- [Producing Messages](#producing-messages)
- [Consuming Messages](#consuming-messages)
- [Python Integration](#python-integration)
- [Useful Links](#useful-links)

## Introduction

Apache Kafka is a distributed event streaming platform capable of handling high-throughput, low-latency data transmission. It is used for building real-time data pipelines and streaming applications.

## Installation

1. **Download Kafka:**
   Download the latest Kafka release from the [official Kafka website](https://kafka.apache.org/downloads).

2. **Extract Kafka:**
   Extract the downloaded tar file to a directory of your choice.

   ```sh
   tar -xzf kafka_2.13-2.8.0.tgz
   mv kafka_2.13-2.8.0 /path/to/kafka
   ```

## Starting ZooKeeper and Kafka Broker

### Start ZooKeeper

Kafka relies on ZooKeeper to manage the cluster.

1. **Open Command Prompt and navigate to Kafka directory:**

   ```sh
   cd /path/to/kafka
   ```

2. **Start ZooKeeper:**

   ```sh
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
   ```

### Start Kafka Broker

1. **Open another Command Prompt and navigate to Kafka directory:**

   ```sh
   cd /path/to/kafka
   ```

2. **Start Kafka Broker:**

   ```sh
   .\bin\windows\kafka-server-start.bat .\config\server.properties
   ```

## Creating a Topic

1. **Open another Command Prompt and navigate to Kafka directory:**

   ```sh
   cd /path/to/kafka
   ```

2. **Create a Kafka Topic:**

   ```sh
   .\bin\windows\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
   ```

3. **Verify Topic Creation:**

   ```sh
   .\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092
   ```

## Producing Messages

1. **Open another Command Prompt and navigate to Kafka directory:**

   ```sh
   cd /path/to/kafka
   ```

2. **Start Kafka Producer:**

   ```sh
   .\bin\windows\kafka-console-producer.bat --topic test-topic --bootstrap-server localhost:9092
   ```

3. **Produce Messages:**
   Type messages into the console and hit Enter to send them to the topic.

## Consuming Messages

1. **Open another Command Prompt and navigate to Kafka directory:**

   ```sh
   cd /path/to/kafka
   ```

2. **Start Kafka Consumer:**

   ```sh
   .\bin\windows\kafka-console-consumer.bat --topic test-topic --bootstrap-server localhost:9092 --from-beginning
   ```

3. **Consume Messages:**
   The consumer will display any messages sent to the `test-topic`.

## Python Integration

To integrate Kafka with a Python application, use the `kafka-python` library.

1. **Install kafka-python:**

   ```sh
   pip install kafka-python
   ```

2. **Python Producer Example:**

   ```python
   from kafka import KafkaProducer

   producer = KafkaProducer(bootstrap_servers='localhost:9092')

   for i in range(10):
       message = f'Test message {i}'
       producer.send('test-topic', value=message.encode('utf-8'))
       print(f'Sent: {message}')

   producer.flush()
   producer.close()
   ```

3. **Python Consumer Example:**

   ```python
   from kafka import KafkaConsumer

   consumer = KafkaConsumer(
       'test-topic',
       bootstrap_servers='localhost:9092',
       auto_offset_reset='earliest',
       group_id='my-group')

   for message in consumer:
       print(f'Received: {message.value.decode("utf-8")}')
   ```

## Useful Links

- [Apache Kafka Official Documentation](https://kafka.apache.org/documentation/)
- [Kafka Python Client](https://github.com/dpkp/kafka-python)
 
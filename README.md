# Optima-Kafka-Client

## About The Project
Apache Kafka producer and consumer clients for testing purposes.

## Getting started
### Prerequisites
* Python3
* kafka-python module (https://pypi.org/project/kafka-python/)

## Usage
### optima-example-producer
`python optima-example-producer.py host port topic` creates random data in an examplary JSON format and produces it to a kafka topic at localhost:port.

If there is a kafka server running on the localhost and the default port is used:
`python optima-example-producer.py localhost:9092 test-topic`

### optima-example-consumer
`python optima-example-consumer.py host port topic` consumes JSON formatted data from a kafka topic at localhost:port and displays them on the console.

If there is a kafka server running on the localhost and the default port is used:
`optima-example-consumer.py localhost:9092 test-topic`

## License
Distributed under the MIT License. See LICENSE for more information.

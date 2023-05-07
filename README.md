# Kafka time series analysis example

## Setup

We create our kafka instance with docker-compose. We have a single node for [Kafka](https://kafka.apache.org/), one [Zookeper](http://zookeeper.apache.org/) (used to store Kafka cluster metadata) and a instance of [Kowl](https://cloudhut.dev/docs/installation) (web UI for exploring messages and topics inside our cluster).

Commands:

- Start the cluster: `docker-compose up -d`
- Stop the cluster: `docker-compose down`
- See logs of the cluster: `docker-compose logs -f`

## Scripts

### [create_topic.py](./create_topic.py)

Script to create topics inside our cluster. Takes one argument, the topic's name.

> For our example, we need to create two topics: `ts-to-analyze` and `ts-analysis`

### [ts_producer.py](./ts_producer.py)

Script that produce time series and push them to a Kafka topic.

> For our example, the script will push to the `ts-to-analyze` topic.

### [analyzer.py](./analyzer.py)

Script that will consume messages on a topic, expecting to receive time series, calculate basic stats on those time series and then push the results on an other topic.

> For our example, we will listen to the `ts-to-analyze` topic and push to the `ts-analysis` topic.

### [analysis_consumer.py](./analysis_consumer.py)

Script that will listen to a topic and print out the message it receives.

> For our example, we print out the message received in the `ts-analysis` topic.

## Run

1. Open a terminal and start the Kafka cluster: `docker-compose up -d`
2. Install the required python dependencies to run the scripts: `python3.7 -m pip isntall -r requirements.txt`
3. In a new terminal, launch the analyzer script: `python3.7 analyzer.py`
4. In a new terminal, launch the analysis consumer script: `python3.7 analysis_consumer.py`
5. In a new terminal, use the ts producer script to create time series and push them on the cluster: `python3.7 ts_producer.py`
6. You should see in the window where the analysis consumer is running results of the time series analysis

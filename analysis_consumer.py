import json
from pprint import pprint

from kafka import KafkaConsumer
from kafka.errors import KafkaError


def main() -> None:
    consumer = KafkaConsumer(
        "ts-analysis",
        bootstrap_servers="localhost:9093",
        value_deserializer=lambda x: json.loads(x.decode()),
    )

    for message in consumer:
        pprint(message.value, indent=2)


if __name__ == "__main__":
    try:
        main()
    except KafkaError as error:
        print(error)
    except KeyboardInterrupt:
        pass

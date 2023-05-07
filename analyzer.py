import json
from io import BytesIO

import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError


def main() -> None:
    consumer = KafkaConsumer(
        "ts-to-analyze",
        bootstrap_servers="localhost:9093",
    )
   
    producer = KafkaProducer(
        bootstrap_servers="localhost:9093",
        value_serializer=lambda msg: json.dumps(msg.decode()).encode(),
    )

 
    for message in consumer:
        df = pd.read_csv(BytesIO(message.value))
        serialized_df = df.to_csv().encode()
        producer.send("ts-analysis", serialized_df)

if __name__ == "__main__":
    try:
        main()
    except KafkaError as error:
        print(error)
    except KeyboardInterrupt:
        pass

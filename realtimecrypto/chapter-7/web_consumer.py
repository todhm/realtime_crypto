import json
from kafka import KafkaConsumer
 
consumer = KafkaConsumer("gemini-feed", bootstrap_servers=["kafka-node:9092"])
 
for message in consumer:
    print(json.loads(message.value))

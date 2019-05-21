from kafka import KafkaProducer
import json


msg_count = 50
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for i in range(0,msg_count):
    msg = {'id': i+20, 'payload': 'Here is test message {}'.format(i+20)}
    sent = producer.send('test-topic2', bytes(json.dumps(msg), 'utf-8'))
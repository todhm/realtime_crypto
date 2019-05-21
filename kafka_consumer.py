from kafka import KafkaConsumer


consumer = KafkaConsumer('test-topic2',
                         bootstrap_servers=['localhost:9092'],
                        auto_offset_reset='earliest')


count = 0
print(consumer)
for message in consumer:
    print(count)
    print(message)
    if count <= 300:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                  message.offset, message.key,
                                                  message.value))
    else:
        break
    count += 1
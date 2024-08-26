import time
from datetime import datetime
from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

conf = {
    'bootstrap.servers': 'kafka1:9092,kafka2:9093,kafka3:9094',
    'client.id': 'python-producer'
}

producer = Producer(conf)

topic = 'test-topic'

try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f'Message at {timestamp}'
        producer.produce(topic, message.encode('utf-8'), callback=delivery_report)
        producer.flush()
        print(f'Message sent: {message}')
        time.sleep(10)  # Attendiamo 10 secondi prima di inviare il prossimo messaggio
except KeyboardInterrupt:
    pass
finally:
    producer.flush()

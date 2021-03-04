# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kafka import KafkaProducer
import sys
import random
import time
import json
from datetime import datetime, timedelta


# Press the green button in the gutter to run the script.

def produce(queue_name, identifier):
    timestamp = int(datetime.utcnow().replace(microsecond=0, second=0).timestamp()) + 60
    message = "{ \"id\": \"" + identifier + "\", \"val\": \"" + str(random.randrange(100000)) + "\"}"
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    print("Producing...")
    producer.send(queue_name, bytes(message, encoding='utf8'))
    producer.close()
    print('Sent: ' + message + '\tjava-ts:' + str(timestamp * 1000))


if __name__ == '__main__':

    if len(sys.argv) != 4:
        raise ValueError('Usage: send.py queue1 queue2 id')
    queue1 = sys.argv[1]
    queue2 = sys.argv[2]
    identity = sys.argv[3]

    while 1:
        produce(queue1, identity)
        produce(queue2, identity)

        dt = datetime.now() + timedelta(seconds=60)
        dt = dt.replace(second=15)

        while datetime.now() < dt:
            time.sleep(1)

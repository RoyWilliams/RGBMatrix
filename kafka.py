from confluent_kafka import Consumer, KafkaError
import settings
import json
import time
from datetime import datetime

consumer = None
n = settings.npix
delay = settings.kafka_delay

def now():
    return datetime.utcnow().strftime("%m/%d %H:%M:%S")

def get_kafka(array):
    conf = {
        'bootstrap.servers': settings.kafka_server,
        'group.id': settings.group_id,
        'default.topic.config': {'auto.offset.reset': 'smallest'}
    }
    consumer = Consumer(conf)
    topics = settings.topics
    consumer.subscribe(topics)

    nalert = 0
    print('kafka started')
    while 1:
        msg = consumer.poll(timeout=10)
        if msg == None:
            print(now(), 'null')
            time.sleep(60)
            continue
        try:
            packet = json.loads(msg.value())
            if msg.topic() == topics[0]:
                ra = packet['ramean']
                ra = ra/360.0
                de = packet['decmean']
                de = (de + 25)/100
                i = int(n*ra)
                if i < 0: i = 0
                if i >=n: i = n-1
                j = int(n*(1-de))
                if j < 0: j = 0
                if j >=n: j = n-1
                array[i + j*n] += 1
            else:
                print(now(), '%s at %s' % (topics[1], packet['UTC']))
                # dont know what to do with it
            if settings.debug:
                print(i, j)
        except Exception as e:
            print(e)
        if nalert%1000 == 0:
            print(now(), nalert, ' alerts')
        time.sleep(delay)
        nalert += 1
    print(now(), 'Finished with %d alerts' % nalert)

if __name__ == "__main__":
    get_kafka([0]*n*n)

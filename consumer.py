import json
import asyncio

from time import time
from aiokafka import AIOKafkaConsumer
from motor.motor_asyncio import AsyncIOMotorClient


db_str = 'mongodb://admin:1234@localhost:27017/?authMechanism=DEFAULT&directConnection=true'
client = AsyncIOMotorClient(db_str)['kafka_db']


async def consume():
    consumer = AIOKafkaConsumer(
        'my_topic',
        bootstrap_servers='localhost:9092',
        group_id="my-group"
    )
    await consumer.start()
    try:
        start = time()
        counter = 0
        async for msg in consumer:
            await process_message(msg=msg)
            counter += 1
            if counter == 10000:
                break
        print('{:.2f} seconds to process all messages'.format(time() - start))
    finally:
        await consumer.stop()


async def process_message(msg):
    # message prints are just a way to keep up with the processing
    # print("consumed: ", msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
    print('.', end='')
    await client.messages.insert_one(json.loads(msg.value))


asyncio.run(consume())

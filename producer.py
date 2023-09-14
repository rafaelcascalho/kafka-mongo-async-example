import json
import asyncio

from datetime import datetime, timezone
from aiokafka import AIOKafkaProducer


async def send_many():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        tasks = []
        for i in range(10000):
            msg = {
                "message_id": i,
                "body": f"message {i}",
                "event_timestamp": datetime.now(tz=timezone.utc).timestamp()
            }
            tasks.append(producer.send_and_wait("my_topic", json.dumps(msg).encode()))
        await asyncio.gather(*tasks)
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_many())

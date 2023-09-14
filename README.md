# Async high load kafka producer-consumer example

## Prerequisites

Python 3.10.7 or greater
Docker version 20.10.5+dfsg1, build 55c4c88 or greater
Docker Compose version v2.3.3 or greater

## Run

1. Run the infrastructure with docker-compose

   ```sh
   $ docker-compose up -d
   ```

   note: sometimes the kafka fails to communicate with zookeeper. So far, the solution is to run `ocker-compose down` and retry the command. A suggested way to verify is to run `docker ps` after the command above.

2. Create a virtual env with a tool of your choice and install the dependencies
   ```sh
   $ pip install -r requirements.txt
   ```
3. Run the consumer
   ```sh
   $ python consumer.py
   ```
4. Run the producer
   ```sh
   $ python producer.py
   ```

Note: for some reason, when running with the debugger it retrieves old messages, outside, it get only new ones, which is why in the run description you should run the consumer previous to the producer.

## Tech

- [aiokafka](https://pypi.org/project/aiokafka/): async lib to produce messages and read them from kafka
- [motor](https://pypi.org/project/motor/): async lib used to store message values in mongo

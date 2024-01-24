import asyncio
from config_loader import load_config
from producer import Producer
from сonsumer import Consumer


def main():
    conf = load_config('rabbitmq_config.yaml')
    try:
        # Запуск продюсера
        producer = Producer(conf['rmq']['connection'])
        asyncio.run(producer.send_message(conf['rmq']['test_queue']['params']['name'], "Hello World"))

        # Запуск консьюмера
        consumer = Consumer(conf['rmq']['connection'])
        asyncio.run(consumer.consume(conf['rmq']['test_queue']['params']['name']))
    except KeyboardInterrupt:
        print("Программа остановлена пользователем")
if __name__ == "__main__":
    main()

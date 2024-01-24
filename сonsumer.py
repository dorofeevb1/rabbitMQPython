import asyncio
import aio_pika

class Consumer:
    def __init__(self, connection_params):
        self.connection_params = connection_params

    async def on_message(self, message: aio_pika.IncomingMessage):
        async with message.process():
            print(f"Received: {message.body.decode()}")


    async def consume(self, queue_name):
        connection = await aio_pika.connect_robust(**self.connection_params)
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)
            await queue.consume(self.on_message)
            print("Waiting for messages. To exit press CTRL+C")
            await asyncio.Future()  # Бесконечный цикл ожидания

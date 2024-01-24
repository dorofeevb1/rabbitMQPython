import asyncio
import aio_pika

class Producer:
    def __init__(self, connection_params):
        self.connection_params = connection_params

    async def send_message(self, queue_name, message_body):
        connection = await aio_pika.connect_robust(**self.connection_params)
        async with connection:
            channel = await connection.channel()
            queue = await channel.declare_queue(queue_name, durable=True)
            message = aio_pika.Message(body=message_body.encode())
            await channel.default_exchange.publish(message, routing_key=queue.name)
            print(f"Sent: {message_body}")

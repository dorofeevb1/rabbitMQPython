import pika

# Установка соединения
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Создание очериди (объявление ее устойчивой)
channel.queue_declare(queue='task_queue', durable=True)

# Отправка сообщения (делаем сообщение устойчивым)
message = "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,
    )
)
print(f" [x] Sent {message}")

# Закрытие соединения
connection.close()

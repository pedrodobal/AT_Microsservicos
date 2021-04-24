import pika, json

params = pika.URLParameters('amqps://vjukodnq:1O1kym-eQ42ZXACIlIK4FRdb4Rigjy0c@prawn.rmq.cloudamqp.com/vjukodnq')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin: {}'.format(json.loads(body)))

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
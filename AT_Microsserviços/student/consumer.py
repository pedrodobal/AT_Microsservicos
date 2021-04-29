import pika, json
from student import Task, db

params = pika.URLParameters('URL_HERE')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print('Received: {}'.format(data))
    
    if properties.content_type == 'task_created':
        task = Task(id=data['id'], discipline=data['discipline'], question=data['question'])
        db.session.add(task)
        db.session.commit()
    
    elif properties.content_type == 'task_updated':
        task = Task.query.get(data['id'])
        task.discipline = data['discipline']
        task.question = data['question']
        db.session.commit()
        
    elif properties.content_type == 'task_deleted':
        task = Task.query.get(data)
        db.session.delete(task)
        db.session.commit()
        
        

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()

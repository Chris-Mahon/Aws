import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAINXYPUALDFYQ', aws_secret_access_key='gqfZms2LJR39mi/W3eWBSGs0rD6dgfQ8lcCPRV')
rs = conn.get_all_queues()
Queue = conn.get_queue("ItsAWholeNewQueue")

conn.send_message(Queue, "This is a Message")

i=0
for i in range(1,100):
	conn.send_message(Queue, "This is Message Number " + str(i))



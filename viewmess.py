import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIALDFYQ', aws_secret_access_key='gqfZms2LJR39mi/W3eWBSGC9Q8lcCPRV')
Queue = conn.get_queue("ItsAWholeNewQueue")
ListofMessages = conn.receive_message(Queue, 10)
print(len(ListofMessages))
for message in ListofMessages:
	print(message.get_body())	



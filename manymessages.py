# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKZUALDFYQ', aws_secret_access_key='gqfZms2LJR3gfC9Q8lcCPRV')
Queue = conn.get_queue("ItsAWholeNewQueue")

i=0
for i in range(1,100):
	conn.send_message(Queue, "This is Message Number " + str(i))



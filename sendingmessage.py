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

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='ALDFYQ', aws_secret_access_key='gqfZms2LJR39mi/W3eWBSGsPRV')
Queue = conn.get_queue("ItsAWholeNewQueue")

conn.send_message(Queue, "This is a Message")

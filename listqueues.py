import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='ALZEZUALDFYQ', aws_secret_access_key='gqfZms2LJgfC9Q8lcCPRV')
rs = conn.get_all_queues()

for q in rs:
        print q.id


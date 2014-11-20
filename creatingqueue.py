import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAINXYLZUALDFYQ', aws_secret_access_key='gqfZms2LJR39mi/W3eWBSGs0gfC9Q8lcCPRV')
Queue = conn.create_queue("ItsAWholeNewQueue")


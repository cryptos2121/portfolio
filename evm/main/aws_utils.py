# aws_utils.py
import boto3
from config import BUCKET_NAME, SECRET_KEY_FILE, AWS_PROFILE_NAME

# Create an S3 resource using the specified AWS profile (if provided)
# session = boto3.Session(profile_name=aws_profile_name)
# s3 = session.resource('s3')
s3 = boto3.resource('s3')

def create_s3_resource():
    s3 = boto3.resource('s3')
    return s3

def get_secret_from_s3():
    s3 = create_s3_resource()
    obj = s3.Object(BUCKET_NAME, SECRET_KEY_FILE)
    contents = obj.get()['Body'].read().decode('utf-8').strip()
    return contents

def check_message(message):
    secret_key = get_secret_from_s3()
    # print ("secret_key ==>", secret_key)
    # print ("message ==>", message)
    if message != secret_key:
        print ("Access Denied   ❌")
        return False
    else:
        print("")
        # print ("Access Granted   ✅")
        return True
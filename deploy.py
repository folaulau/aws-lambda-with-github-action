import boto3


"""
This script pulls the most recent released artifact from s3 and deploy it to aws lambda

Every time there's a deploy, there's only one object in s3 since all objects are deleted before package command is run.
So s3_iterator.search will return 1 object
"""

s3_client = boto3.client("s3")
lambda_client = boto3.client('lambda')

s3_response = s3_client.list_objects_v2(
    Bucket='folautech-lambda-container',
    MaxKeys=10,
    Prefix='aws-lambda-with-github-action'
)

# print("s3_response: {}".format(s3_response))

latest_key = ''

for key_data in s3_response['Contents']:
    print("key_data: {}".format(key_data))
    latest_key = key_data['Key']

print("latest_key: {}".format(latest_key))

lambda_update_response = lambda_client.update_function_code(
    FunctionName='aws-lambda-with-github-action',
    S3Bucket='folautech-lambda-container',
    S3Key=latest_key,
)

print("lambda_update_response: {}".format(lambda_update_response))
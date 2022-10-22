import boto3
import datetime

s3 = boto3.client("s3")
client = boto3.client('lambda')

s3_paginator = s3.get_paginator('list_objects_v2')
s3_iterator = s3_paginator.paginate(Bucket='folautech-lambda-container',Prefix='aws-lambda-with-github-action',
                    PaginationConfig={
                        'MaxItems': 10,
                        'PageSize': 10
                    }
            )

latest_key = ''

for key_data in s3_iterator.search():
    latest_key = key_data

print("latest_key: {}".format(latest_key))

lambda_update_response = client.update_function_code(
    FunctionName='aws-lambda-with-github-action',
    S3Bucket='folautech-lambda-container',
    S3Key=latest_key,
)

print("lambda_update_response: {}".format(lambda_update_response))
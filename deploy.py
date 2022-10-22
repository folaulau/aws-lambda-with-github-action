import boto3
import datetime
s3 = boto3.resource('s3')
bucket = s3.Bucket('folautech-lambda-container')

bucket.objects.filter

for obj in bucket.objects.all():
    print(obj.key)

s3 = boto3.client("s3")

s3_paginator = s3.get_paginator('list_objects_v2')
s3_iterator = s3_paginator.paginate(Bucket='folautech-lambda-container',Prefix='aws-lambda-with-github-action',
                    PaginationConfig={
                        'MaxItems': 10,
                        'PageSize': 10
                    }
            )

filtered_iterator = s3_iterator.search(
    "Contents[?to_string(LastModified)>='\"2022-10-22 08:05:37+00:00\"'].Key"
)

latest_key = ''

for key_data in filtered_iterator:
    print(key_data)
    print("value:{}".format(filtered_iterator[key_data]))
    latest_key = key_data

print("latest_key: {}".format(latest_key))


# response = client.update_function_code(
#     FunctionName='string',
#     ZipFile=b'bytes',
#     S3Bucket='string',
#     S3Key='string',
#     S3ObjectVersion='string',
#     ImageUri='string',
#     Publish=True|False,
#     DryRun=True|False,
#     RevisionId='string',
#     Architectures=[
#         'x86_64'|'arm64',
#     ]
# )
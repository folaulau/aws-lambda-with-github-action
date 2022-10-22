import boto3

# s3 = boto3.resource('s3')
# bucket = s3.Bucket('folautech-lambda-container')
# for obj in bucket.objects.all():
#     print(obj.key)

s3 = boto3.client("s3")

s3_paginator = s3.get_paginator('list_objects_v2')
s3_iterator = s3_paginator.paginate(Bucket='folautech-lambda-container',Prefix='aws-lambda-with-github-action')

filtered_iterator = s3_iterator.search(
    "Contents[?to_string(LastModified)>='\"2022-10-22 08:05:37+00:00\"'].Key"
)

for key_data in filtered_iterator:
    print(key_data)
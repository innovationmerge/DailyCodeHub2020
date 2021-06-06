# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to List objects in S3 bucket using boto3 SDK
 
# **************** Prerequisites *****************
#        Refer to DAY 196 Post
# ************************************************

import boto3
s3_client = boto3.client('s3')

bucket_name = "nnm-test-1"

# List objects in s3 bucket
for key in s3_client.list_objects(Bucket=bucket_name)['Contents']:
    print(key['Key'])

# Output
# sample.txt




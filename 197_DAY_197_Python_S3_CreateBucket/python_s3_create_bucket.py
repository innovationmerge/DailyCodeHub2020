# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to Create bucket in AWS S3 using boto3 SDK
 
# **************** Prerequisites *****************
#        Refer to DAY 196 Post
# ************************************************

import boto3
s3_client = boto3.client('s3')

# Create bucket
s3_client.create_bucket(Bucket='nnm-test-1')



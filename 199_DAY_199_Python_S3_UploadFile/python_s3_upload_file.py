# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to upload a file to S3 bucket using boto3 SDK
 
# **************** Prerequisites *****************
#        Refer to DAY 196 Post
# ************************************************

import boto3
s3_client = boto3.client('s3')

filename = "sample.txt"
bucket_name = "nnm-test-1"

# Upload File
s3_client.upload_file(filename, bucket_name, filename)



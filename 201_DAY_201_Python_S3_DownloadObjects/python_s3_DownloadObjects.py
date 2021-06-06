# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to Download object in S3 bucket using boto3 SDK
 
# **************** Prerequisites *****************
#        Refer to DAY 196 Post
# ************************************************

import boto3
s3_client = boto3.resource('s3')

filename = "sample.txt"
bucket_name = "nnm-test-1"

# Download objects from s3 bucket
s3_client.meta.client.download_file(bucket_name, filename, filename)





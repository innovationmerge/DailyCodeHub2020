# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to Get a bucket access control list of S3 bucket using boto3 SDK
 
# **************** Prerequisites *****************
#        Refer to DAY 196 Post
# ************************************************

import boto3
s3_client = boto3.client('s3')

filename = "sample.txt"
bucket_name = "nnm-test-1"

# Retrieve a bucket's ACL
result = s3_client.get_bucket_acl(Bucket=bucket_name)
print(result)

# Output 
# {'ResponseMetadata':{'RequestId':'K8TN8WdfafasdP84','HostId':'asfasdfasdfSDFASFW3RFDAFASDFASFSDAFASF','HTTPStatusCode':200,'HTTPHeaders':{'x-amz-id-2':'FDAFASD/8nTqpNS7UMnWU/8nbotB+GgyR3ZHwFoV4MakEU=','x-amz-request-id':'K8TN8WNN1ME9VP84','date':'Sun, 30 May 2021 09:31:57 GMT','content-type':'application/xml','transfer-encoding':'chunked','server':'AmazonS3'},'RetryAttempts':0},'Owner':{'DisplayName':'innovationmerge','ID':'DAFASDFASDFADFASFDASF'},'Grants':[{'Grantee':{'DisplayName':'innovationmerge','ID':'AFASDFASDFADFASFDASFASDFADFASFASDFAD','Type':'CanonicalUser'},'Permission':'FULL_CONTROL'}]}



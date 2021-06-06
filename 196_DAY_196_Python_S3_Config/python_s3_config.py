# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with AWS S3 SDK for Python

# Python program to configure boto3 to interact with AWS S3
 
# **************** Prerequisites ****************
# Get Access Key ID and Secret Access Key 
# from AWS console -> My Security Credentials ->   Access keys -> Create
# Store it in dir ~/.aws/credentials (Linux, Unix, and macOS) 
# or C:\Users\USER_NAME\.aws\credentials (Windows).

# **************** Install AWS boto3 ****************
# pip install boto3

# **************** Configuration ****************
# Import boto3 module
import boto3
s3_client = boto3.client('s3')



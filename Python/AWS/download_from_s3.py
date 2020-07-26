import boto3
s3_client=bto3.client('s3')
s3_client.meta.client.download_file('mybucket', 'hello.txt', '/tmp/hello.txt')
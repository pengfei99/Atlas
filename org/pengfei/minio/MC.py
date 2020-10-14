from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

minioClient = Minio('minio.lab.sspcloud.fr',
                    access_key='DSW0PH8P9QERM6S3NTLO',
                    secret_key='RcwNtUJnwRP04Rk2MzpWWOh4HFqe+N1hKaYA27C6',
                    token='eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiJEU1cwUEg4UDlRRVJNNlMzTlRMTyIsImFjciI6IjAiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJhdWQiOlsib255eGlhIiwiYWNjb3VudCJdLCJhdXRoX3RpbWUiOjE2MDI2NjA1NDgsImF6cCI6Im9ueXhpYSIsImVtYWlsIjoibGl1LnBlbmdmZWlAaG90bWFpbC5mciIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJleHAiOiIxNjAyNzAzNzQ4IiwiZmFtaWx5X25hbWUiOiJMaXUiLCJnaXZlbl9uYW1lIjoiUGVuZ2ZlaSIsImlhdCI6MTYwMjY2MDcxMywiaXNzIjoiaHR0cHM6Ly9hdXRoLmxhYi5zc3BjbG91ZC5mci9hdXRoL3JlYWxtcy9zc3BjbG91ZCIsImp0aSI6IjE0ZTY0NzZmLWYzZGItNDY0Yi05Yzk0LWY1MWE5YjJhNTRmMCIsIm5hbWUiOiJQZW5nZmVpIExpdSIsIm5vbmNlIjoiZjA3MzBjMDMtZDNmOS00N2MyLTllN2YtNTMxNjgyOTE0YTZhIiwicG9saWN5IjoiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoicGVuZ2ZlaSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJBdGxhc19yb2xlX2FkbWluIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNlc3Npb25fc3RhdGUiOiIwMzUwNmEyOS1kYTJjLTQxYTctYTk4MC03MzgyNWJlYjJkMzciLCJzdWIiOiI0NzM0OTEyOC00YTRjLTQyMjYtYTViMS02ODA4MDFhZjVhMmIiLCJ0eXAiOiJCZWFyZXIifQ.ti2pAC1b67mDw9q9AXq6GvsIR9j5WyvGTQOMrAuwtXIidXEdW2Sy4RRpvfunffU4aIJ8x5IjmhS1YfCU9fDtCg',
                    secure=True)

# Make a bucket with the make_bucket API call.
try:
    minioClient.make_bucket("test", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
    pass
except BucketAlreadyExists as err:
    pass
except ResponseError as err:
    raise

# Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
try:
    minioClient.fput_object('test', 's3_bucket.json', 'target/s3_bucket.json')
except ResponseError as err:
    print(err)

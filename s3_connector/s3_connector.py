import boto3
import pickle
from loguru import logger


class S3Connector:
    def __init__(self, creds, create_default_bucket=True):
        self.creds = creds
        self.resource = boto3.resource('s3',
            endpoint_url=f'http://{creds["host"]}:{creds["port"]}',
            aws_access_key_id=creds['aws_access_key_id'],
            aws_secret_access_key=creds['aws_secret_access_key'],
        )
        if create_default_bucket:
            self.create_bucket(self.creds['bucket'])

    def create_bucket(self, name):
        client = self.resource.meta.client
        try:
            self.resource.create_bucket(Bucket=name)
        except (client.exceptions.BucketAlreadyExists, client.exceptions.BucketAlreadyOwnedByYou):
            logger.debug('Bucket already exists. Ignore...')

    def put_file(self, obj, key):
        logger.debug(f'Put file with {key}')
        self.resource.Object(self.creds['bucket'], key)\
                    .put(Body=pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL))

    def get_file(self, key):
        obj_binary = self.resource.Object(self.creds['bucket'], key).get()
        return pickle.loads(obj_binary['Body'].read())


if __name__ == '__main__':
    # example create connector
    creds = dict(
        host='localhost',
        port=9000,
        aws_access_key_id='minio',
        aws_secret_access_key='minio123',
        bucket='sample-bucket2'
    )
    s3 = S3Connector(creds)
    # put object by key
    test_key = 'example_key'
    s3.put_file(dict(), key=test_key)
    # load object from key
    data = s3.get_file(key=test_key)
    print(data)

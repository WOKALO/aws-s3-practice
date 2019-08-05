import logging
import boto3
from botocore.exceptions import ClientError
import argparse

def upload_file(file_name, bucket, object_name = None):
    """
    Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: s3 object name. If not specified then same as file name
    :return: True if file was uploaded, else False
    """
    
    # Any clients created from this session will use credentials
    # from the airflow session of ~/.aws/credentials
    session = boto3.Session(profile_name='airflow-scheduler')
    
    #s3 client instance using airflow session
    s3_client = session.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__=='__main__':

    #Parser provides an user friendly command line interface, 3 parameters read
    #From command args will be configured for the file transfer.
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', dest='one_file', required=True)
    parser.add_argument('--bucket_name', dest='s3_bucket', required=True)
    parser.add_argument('--object_name', dest='s3_object_name', required=True)
    args = parser.parse_args()
    
    #Read the params
    file_name = args.one_file
    bucket_name = args.s3_bucket
    object_name = args.s3_object_name
    
    #Setup logging
    logging.basicConfig(level=logging.DEBUG,
                            format = '%(levelname)s: %(asctime)s: %(message)s',
                            datefmt = '%m-%d %H:%M',
                            filename = '/home/lzgtk/Python Projects/Dataflow/logging/s3_upload_app.log',
                            filemode = 'w' #truncate and add
                            )
    
    #Upload file
    response = upload_file(file_name, bucket_name, object_name)
    
    if response:
        logging.info('File was uploaded')
    else:
        logging.info('File upload failed')
    
    

import boto3


def download_s3_document(bucket_name: str, object_key: str, file_path: str) -> None:
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, object_key, file_path)
        print(f"Document downloaded successfully from s3://{bucket_name}/{object_key} to "
              f"{file_path}.")
    except Exception as e:
        print(f"Error downloading document: {e}")


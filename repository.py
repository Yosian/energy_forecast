from infrastructure import download_s3_document
from entities import Paths


# Provide the S3 bucket name, object key, and local file path to download the document
Paths.bucket = 'aws-ml-jos-udemy'
Paths.path_to_s3 = 'time_series_datasets/dutch-energy.csv'
Paths.path_to_local = 'energy.csv'


# Download the document from S3
download_s3_document(Paths.bucket, Paths.path_to_s3, Paths.path_to_local)
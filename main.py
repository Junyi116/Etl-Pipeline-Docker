# Libraries to load the environment variables
import os

from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_data_to_s3 import load_data_to_s3

# fetch the environment variables from the .env file using the getenv function
aws_access_key = os.getenv("aws_access_key")
aws_secret_access_key = os.getenv("aws_secret_access_key")

# define the key and S3 bucket
key = "etl/jz_online_trans_final.csv"
s3_bucket = 'waia-march-bootcamp'

# extract data from tables in the database
ot_transformed = extract_transactional_data()

# remove the duplicates
ot_wout_duplicates = identify_and_remove_duplicates(ot_transformed)

# Load the data to s3
load_data_to_s3(ot_wout_duplicates, key, s3_bucket, aws_access_key, aws_secret_access_key)

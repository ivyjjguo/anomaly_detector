import faiss
import pickle
import boto3
import numpy as np
from config import S3_BUCKET, S3_KEY

s3_client = boto3.client('s3')

def load_faiss_from_s3():
    try:
        s3_client.download_file(S3_BUCKET, S3_KEY, "faiss_index.pkl")
        with open("faiss_index.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return faiss.IndexFlatL2(1536)

import openai
import numpy as np
from config import OPENAI_API_KEY

def get_embedding(text):
    '''Gets embeddings for text'''

    response = openai.Embedding.create(
        model='text-embedding-ada-002', 
        input=[text]
    )

    return np.array(response['data'][0]['embedding'])



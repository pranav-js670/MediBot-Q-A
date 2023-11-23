DATA_DIR_PATH = "data/"
VECTOR_DB_PATH = "faiss/education"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 200
EMBEDDER = "thenlper/gte-large"
DEVICE = "cpu"

PROMPT_TEMPLATE = """
Try to answer the question with the information provided. 
If you can't answer the question based on the information provided, either say you can't find an answer or are unable to find an answer.
So try to understand in depth about the context and answer only based on the information provided.
Do not generate irrelevant answers. Provide a concise answer based on the information. 

Context : {context}
Question : {question}
Do provide only helpful answers

Helpful Answer : 
"""

INP_VARS = ['context','question']
CHAIN_TYPE = "stuff"
SEARCH_KWARGS = {'k':2}
MODEL_CKPT = "llama-2-7b-chat.ggmlv3.q8_0.bin"
MODEL_TYPE = "llama"
MAX_NEW_TOKENS = 512
TEMPERATURE = 0.9

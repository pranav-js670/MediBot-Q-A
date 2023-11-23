from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import *

def faiss_vector_db():
    dir_loader = DirectoryLoader(
        DATA_DIR_PATH,
        glob='*pdf',
        loader_cls=PyPDFLoader 
        )
    
    docs = dir_loader.load() 
    print("PDF/(s) loaded")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE, 
        chunk_overlap = CHUNK_OVERLAP 
    )

    input_text = text_splitter.split_documents(docs)
    print("Data chunks created")
    
    
    hfembeddings = HuggingFaceEmbeddings(
        model_name = EMBEDDER,
        model_kwargs = {'device':'cpu'}
    )

    db = FAISS.from_documents(input_text, hfembeddings)
    db.save_local(VECTOR_DB_PATH)
    print("Vector store creation completed.")

if __name__ == "__main__":
    faiss_vector_db()


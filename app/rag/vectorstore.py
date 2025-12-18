# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from .embeddings import get_embeddings

VECTOR_DB = None

def create_vectorstore(chunks):
    global VECTOR_DB
    VECTOR_DB = FAISS.from_documents(
        chunks,
        embedding=get_embeddings()
    )

def similarity_search(query, k=3):
    return VECTOR_DB.similarity_search(query, k=k)

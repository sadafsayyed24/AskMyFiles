import pandas as pd
# from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
# from langchain.schema import Document
from langchain_core.documents import Document

def load_file(path: str):
    if path.endswith(".csv"):
        df = pd.read_csv(path)
        text = df.to_string()
        return [Document(page_content=text)]

    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)
        return loader.load()

    raise ValueError("Unsupported file type")

from fastapi import APIRouter, UploadFile, File
import os, shutil, traceback, sys

from app.rag.loader import load_file
from app.rag.splitter import split_docs
from app.rag.vectorstore import create_vectorstore

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("UPLOAD ENDPOINT HIT", flush=True)

    os.makedirs("data/uploads", exist_ok=True)
    path = f"data/uploads/{file.filename}"

    # STEP 1
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    print("STEP 1 OK: file saved", flush=True)

    # STEP 2
    docs = load_file(path)
    print("STEP 2 OK: docs loaded ->", len(docs), flush=True)

    # STEP 3
    chunks = split_docs(docs)
    print("STEP 3 OK: chunks ->", len(chunks), flush=True)

    # STEP 4
    create_vectorstore(chunks)
    print("STEP 4 OK: vectorstore created", flush=True)

    return {"message": "success"}

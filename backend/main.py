from llm_inference import PdfQAAgent
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
import os
import vector_db
import uuid
import logging
import config

logger = logging.getLogger(__name__)

app = FastAPI()
answerer = PdfQAAgent()


class Message(BaseModel):
    message: str
    document_id: str = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.get("/hello")
async def root():
    logger.info("hello world")
    return {"message": "Hello World"}


@app.post("/upload/")
async def upload_files(file: UploadFile, background_tasks: BackgroundTasks):
    logger.info(f"Loading file into DB {file.filename}")
    file_id = str(uuid.uuid4())
    file_path = os.path.join(config.UPLOAD_DIRECTORY, file_id)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        vector_db.insert_file_to_db(file_path)

    logger.info(f"Loaded file into DB {file.filename} with doc_id:{file_id}")
    return {"filename": file.filename, "document_id": file_id}


@app.post("/invoke/")
async def invoke(msg: Message):
    logger.info(f"invoke endpoint with payload: {msg}")
    ans = answerer.answer_question_for_a_document(msg.message, msg.document_id)

    logger.debug(f"invoke endpoint with payload: {ans}")
    return Message(message=ans)


if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--pdf_path", type=str, required=True)
    args = args.parse_args()
    while True:
        question = input("Question: ")
        print(pdf.answer_question(question))

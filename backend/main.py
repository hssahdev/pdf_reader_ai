from llm_inference import PdfQuestionAnswerer
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile, HTTPException, BackgroundTasks
from typing import List
import os

app = FastAPI()

pdf = None

class Message(BaseModel):
    message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)

UPLOAD_DIRECTORY = "temp"


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

def initialize_pdf_processor(file_path):
    global pdf
    pdf = PdfQuestionAnswerer(file_path)
    print("PDF Processor Initialized")
    
@app.post("/upload/")
async def upload_files(file: UploadFile, background_tasks: BackgroundTasks):
    global pdf
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
        background_tasks.add_task(initialize_pdf_processor, file_path)

    return {"filename": file.filename}


@app.post("/invoke/")
async def invoke(msg: Message):
    print(msg)
    if pdf is None:
        raise HTTPException(status_code=400, detail="No PDF file uploaded")
    ans = pdf.answer_question(msg.message)
    return Message(message=ans)


# pdf = PdfQuestionAnswerer(args.pdf_path)

if __name__ == "__main__":
    import argparse

    args = argparse.ArgumentParser()
    args.add_argument("--pdf_path", type=str, required=True)
    args = args.parse_args()
    while True:
        question = input("Question: ")
        print(pdf.answer_question(question))

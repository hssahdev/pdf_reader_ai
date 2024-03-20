from llm_inference import PdfQuestionAnswerer
import argparse

args = argparse.ArgumentParser()
args.add_argument("--pdf_path", type=str, required=True)
args = args.parse_args()

pdf = PdfQuestionAnswerer(args.pdf_path)

while True:
    question = input("Question: ")
    print(pdf.answer_question(question))
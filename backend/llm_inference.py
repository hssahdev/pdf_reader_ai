from langchain.chains.combine_documents import create_stuff_documents_chain
import model
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import vector_db
import config

PROMPT = ChatPromptTemplate.from_template(
    config.PROMPT
)

class PdfQAAgent:
    def __init__(self):
        self.llm = model.llm_model
        self.document_chain = create_stuff_documents_chain(self.llm, PROMPT)

    def answer_question(self, question):
        retriever = vector_db.get_retriever()
        retrieval_chain = create_retrieval_chain(retriever, self.document_chain)
        return retrieval_chain.invoke({"input": question})["answer"]

    def answer_question_for_a_document(self, question, doc_id):
        doc_path = config.UPLOAD_DIRECTORY + "/" + doc_id
        retriever = vector_db.get_retriever(doc_path)
        retrieval_chain = create_retrieval_chain(retriever, self.document_chain)
        return retrieval_chain.invoke({"input": question})["answer"]

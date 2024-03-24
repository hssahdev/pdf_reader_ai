from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from read_pdf import load_split_pdf

PROMPT = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}"""
)

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1024,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

class PdfQuestionAnswerer:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text = load_split_pdf(pdf_path)
        self.llm = Ollama(model="llama2")
        # self.llm = Ollama(model="gemma:7b")
        self.document_chain = create_stuff_documents_chain(self.llm, PROMPT)
        
        embeddings = OllamaEmbeddings()
        documents = text_splitter.split_text(self.text)
        vector = FAISS.from_texts(documents, embeddings)
        retriever = vector.as_retriever()
        self.retrieval_chain = create_retrieval_chain(retriever, self.document_chain)
    
    def answer_question(self, question):
        return self.retrieval_chain.invoke({"input": question})["answer"]







    




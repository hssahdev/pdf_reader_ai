QDRANT_URL = "http://localhost:6333"
INIT_PDF_FILE = "/Users/harshdeepsingh/Downloads/Recent I-94.pdf"
QDRANT_COLLECTION_NAME = "my_documents"
UPLOAD_DIRECTORY = "temp"
LLM_MODEL = "llama2"

# PROMPT = """Answer the following question based only on the provided context:

# <context>
# {context}
# </context>

# Question: {input}"""

PROMPT = """
        You are an AI Agent specialized to answer to questions about a given text.
        
        In order to create the answer, please only use the information from the
        context provided (Context). Do not include other information.
        
        Answer with simple words.
        
        If needed, include also explanations.
        Question: {input}
        Context: <context>{context}</context>
        Answer:
        """
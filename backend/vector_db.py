from qdrant_client import QdrantClient
from langchain_community.embeddings import OllamaEmbeddings
from read_pdf import load_split_pdf
import numpy as np
from qdrant_client.http import models as qdrant_models
from langchain_community.vectorstores import Qdrant
import logging
import config

logger = logging.getLogger(__name__)

url = config.QDRANT_URL

client = QdrantClient(url)
# embedding_model = OllamaEmbeddings(base_url=config.OLLAMA_URL)
embedding_model = OllamaEmbeddings(base_url="http://host.docker.internal:11434")

init_doc = load_split_pdf(
    config.INIT_PDF_FILE
)

qdrant = Qdrant.from_documents(
    init_doc,
    embedding_model,
    url=url,
    collection_name=config.QDRANT_COLLECTION_NAME,
    force_recreate=True,
    prefer_grpc=True,
)


def get_retriever(doc_id=None):
    if doc_id:
        return qdrant.as_retriever(
            search_kwargs=dict(
                filter=qdrant_models.Filter(
                    must=[
                        qdrant_models.FieldCondition(
                            key="metadata.source",
                            match=qdrant_models.MatchValue(value=doc_id)
                        )
                    ]
                )
            )
        )
        
    return qdrant.as_retriever()

    

def insert_file_to_db(file_path):
    documents = load_split_pdf(file_path)

    Qdrant.from_documents(
        documents, embedding_model, url=url, collection_name=config.QDRANT_COLLECTION_NAME
    )

    logger.info("File inserted to DB")
    return True


if __name__ == "__main__":
    # import argparse

    # args = argparse.ArgumentParser()
    # args.add_argument("--pdf_path", type=str, required=True)
    # args = args.parse_args()
    # insert_file_to_db(args.pdf_path)

    from qdrant_client import QdrantClient
    from qdrant_client.http import models

    client = QdrantClient("localhost", port=6333)

    temp = client.search(
        collection_name="my_documents",
        query_filter=models.Filter(
            must=[
                models.FieldCondition(
                    key="file_id",
                    match=models.MatchValue(
                        value="f6b6d868-5187-4db3-ae0e-2a0eb8452a53",
                    ),
                )
            ]
        ),
        # search_params=models.SearchParams(hnsw_ef=128, exact=False),
        query_vector=np.random.rand(4096),
        limit=3,
    )

    print(temp)

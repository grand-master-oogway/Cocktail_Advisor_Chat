import os

import faiss
from llama_index.core import (
    StorageContext,
    VectorStoreIndex,
    SimpleDirectoryReader
)
from llama_index.vector_stores.faiss import FaissVectorStore

os.environ[
    'OPENAI_API_KEY'] = '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'

documents = SimpleDirectoryReader("data").load_data()

d = 1536
faiss_index = faiss.IndexFlatL2(d)

vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)

index.storage_context.persist("storage_indexes")

print("Index built and saved in 'storage_indexes'")

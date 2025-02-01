import faiss
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from llama_index.vector_stores.faiss import FaissVectorStore
from llama_index.core import StorageContext, load_index_from_storage

from chain import create_chat_chain


"""
Here the chat runs, uses created indexes and chain 
"""
app = FastAPI()

templates = Jinja2Templates(directory="templates")

d = 1536
faiss_index = faiss.IndexFlatL2(d)
vector_store = FaissVectorStore(faiss_index=faiss_index)
storage_context = StorageContext.from_defaults(
    persist_dir="storage_indexes",
    vector_store=vector_store
)
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

chat_chain = create_chat_chain()


class query_request(BaseModel):
    question: str


class query_response(BaseModel):
    answer: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask", response_model=query_response)
async def ask(req: query_request):
    retrieval_response = query_engine.query(req.question)
    context_str = str(retrieval_response)

    final_answer = chat_chain.run(context=context_str, question=req.question)

    return query_response(answer=final_answer)

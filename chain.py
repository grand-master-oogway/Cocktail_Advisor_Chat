import os
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory


os.environ[
        'OPENAI_API_KEY'] = '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'


def create_chat_chain() -> LLMChain:
    """
    function that creates a chain for storing context of data and memory of conversation
    """

    llm = OpenAI(temperature=0)

    memory = ConversationBufferMemory(
        input_key="question",
        memory_key="history"
    )
    template_str = """
    You are an expert cocktail advisor. 
    Use the conversation history below plus new context from the knowledge base.

    Past conversation:
    {history}

    Relevant info:
    {context}

    Current question:
    {question}

    Provide a helpful, concise answer:
    """

    prompt = PromptTemplate(
        input_variables=["history", "context", "question"],
        template=template_str
    )

    chain = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )

    return chain

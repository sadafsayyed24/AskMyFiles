# from langchain_openai import ChatOpenAI   # use if u r using openAI key
from app.rag.vectorstore import similarity_search

from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


# ⚠️ TEMPORARY: for local testing only
# # Do NOT commit this file with a real key
# OPENAI_API_KEY = "sk-WWWWWWWWWWWWWWWWWWWWWW"


# def get_llm():
#     """
#     Lazy-load the LLM so FastAPI doesn't crash at startup
#     """
#     # use for paid API 
#     return ChatOpenAI(
#         temperature=0,
#         api_key=OPENAI_API_KEY,
#         model="gpt-3.5-turbo"  # or gpt-4o-mini if enabled
#     )
#     return HuggingFacePipeline(pipeline=pipe)


_llm = None

def get_llm():
    global _llm
    if _llm is None:
        pipe = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=256,
            temperature=0
        )
        _llm = HuggingFacePipeline(pipeline=pipe)
    return _llm


def answer_question(query: str) -> str:
    """
    Answers user question strictly from retrieved context
    """
    docs = similarity_search(query, k=3)

    if not docs:
        return "I don't have that information in the uploaded data."

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""You are a QA assistant. Answer ONLY using the context below. If the answer is not present, say: "I don't have that information in the uploaded data."

    Context:
    {context}

    Question:
    {query}
    """

    llm = get_llm()
    return llm.invoke(prompt)

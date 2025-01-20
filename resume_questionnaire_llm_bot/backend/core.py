from dotenv import load_dotenv
load_dotenv()
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain import hub

def res_docs(query: str, chat_history: list = []):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = FAISS.load_local("faiss_resume_index", embeddings, allow_dangerous_deserialization=True)

    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")
    rephrase_prompt = hub.pull("langchain-ai/chat-langchain-rephrase")
    
    llm = ChatOpenAI(temperature=0)
    
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)
    retrieval_chain = create_retrieval_chain(retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain)
    
    result = retrieval_chain.invoke(input={"input": query, "chat_history": chat_history})
    
    new_result = {
        "query": query,
        "result": result['answer'],
        "source_documents": result['context']
    }

    chat_history.append(("human", query))
    chat_history.append(("ai", result['answer']))
    
    return new_result

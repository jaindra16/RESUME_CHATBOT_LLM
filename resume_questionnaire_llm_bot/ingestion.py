from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

def ingest_docs():
    
    pdf_path = "data/Jaindrap_Resume.pdf"  
    
    loader = PyPDFLoader(pdf_path)
    raw_documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local("faiss_resume_index")

if __name__ == '__main__':
    ingest_docs()

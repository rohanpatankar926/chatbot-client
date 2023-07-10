from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
from tqdm import tqdm
import hashlib
load_dotenv()
from langchain.document_loaders import PDFMinerLoader
from utils import config_loader
from utils import tiktoken_len

class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata
    
    def __call__(self):
         return f"Document(page_content={self.page_content},metadata={self.metadata})"
    
    def get_pagecontent(self):
         return self.page_content
    
    def get_metadata(self):
         return self.get_metadata
    
def pdf_to_json_and_insert(filepath):
        documents=[]
        loader = PDFMinerLoader(filepath)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=tiktoken_len,
            separators=["\n\n", "\n", " ", ""],

        )
        m = hashlib.md5()  # this will convert URL into unique ID
        for doc in tqdm(docs):
            url = doc.metadata["source"].split("/")[-1]
            m.update(url.encode("utf-8"))
            chunks = text_splitter.split_text(doc.page_content)
            for i, chunk in enumerate(chunks):
                doc = Document(page_content=chunk, metadata={"source":url})

                documents.append(
                    doc
                )
        return documents

def openai_embedding():
    model_name = config_loader["openai_embedding_model"]
    embed = OpenAIEmbeddings(
        model=model_name,
        openai_api_key="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",
    )
    return embed

def upload_to_chroma(docs):
    persist_directory = 'db'
    embedding = openai_embedding()
    global vectordb
    vectordb = Chroma.from_documents(documents=docs, 
                                    embedding=embedding,
                                 persist_directory=persist_directory)
    vectordb.persist()
    return vectordb


def retriever_chroma(query):
    vectordb = Chroma(persist_directory="db", 
                    embedding_function=openai_embedding())
    retriever = vectordb.as_retriever(search_kwargs={"k": 10})
    docs = retriever.get_relevant_documents(query)
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key="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"), 
                                    chain_type="stuff", 
                                    retriever=retriever, 
                                    return_source_documents=True)
    return qa_chain(query)

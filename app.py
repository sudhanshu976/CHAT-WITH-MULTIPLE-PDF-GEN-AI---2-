import streamlit as st
from PyPDF2 import PdfReader
import os
import google.generativeai as genai 
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000 , chunk_overlap=1000)
    chunks = splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vector_store = FAISS.from_texts(text_chunks, embedding = embeddings)
    
    vector_store.save_local("vector_store")


def get_conversation():
    prompt_template= """
    Answer the given question in as much detail as you can from the provided context . If you are not able to give answer or you are not able to find the context just say 
    "I don't know" or "I am not able to find the context" and move to the next question.

    Context : \n {context} ? \n
    Question : \n {question} \n


    Asnwer : 
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt=PromptTemplate(template=prompt_template, input_variables=["context", "question"])

    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    new_db = FAISS.load_local("vector_store",embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversation()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True,
    )

    print(response)
    st.write("Reply : \n" , response["output_text"])

def main():
    st.set_page_config("Chat with Multiple PDFs")
    st.header("Chat with Multiple PDFs using Gemini Pro")

    user_question = st.text_input("Enter your question here : ")
    if st.button("Ask"):
        user_input(user_question)

    with st.sidebar:
        st.header("Upload PDFs")
        pdf_docs = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)
        if st.button("Upload"):
            with st.spinner("Uploading PDFs"):
                text = get_pdf_text(pdf_docs)
                chunks = get_chunks(text)
                get_vector_store(chunks)
                st.write("PDFs Uploaded Successfully")

if __name__ == "__main__":
    main()

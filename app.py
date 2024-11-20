from flask import Flask , render_template , jsonify , request
from src.helper import download_hugging_face_embeddings
from langchain.vectorstores import Pinecone as Pi
from pinecone import Pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os

app= Flask(__name__)

# Load the .env file
load_dotenv()

# Retrieve the Pinecone API key
api_key = os.getenv("PINECONE_API_KEY")

embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pc = Pinecone(api_key=api_key)
index_name = "medical-chatbot"
index = pc.Index(index_name)


# Initialize the Pinecone retriever with the embeddings
retriever = Pi.from_existing_index(index_name=index_name, embedding=embeddings )

PROMPT= PromptTemplate(template= prompt_template , input_variables=['context' , 'question'])
chain_type_kwargs={'prompt': PROMPT}

llm = CTransformers(model ="model/llama-2-7b-chat.ggmlv3.q2_K.bin" ,
                    model_type = 'llama',
                     config= {'max_new_tokens' :512 ,
                              'temperature': 0.8} )

# Create the RetrievalQA chain with the customizations
qa = RetrievalQA.from_chain_type(
    llm=llm,                      # Your LLM model (CTransformers in this case)
    retriever=retriever.as_retriever(search_kwargs={"k": 3}),  # Limit to 3 documents
    chain_type="stuff",            # Chain type, change to "stuff" or other options if necessary
    return_source_documents=True,  # Ensure source documents are returned
    chain_type_kwargs=chain_type_kwargs  # Include source document metadata
)

@app.route('/')
def index():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug=True)
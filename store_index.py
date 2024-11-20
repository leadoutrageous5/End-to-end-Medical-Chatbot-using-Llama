from src.helper import load_pdf , text_split , download_hugging_face_embeddings
from langchain.vectorstores import Pinecone as Pi
from pinecone import Pinecone
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Retrieve the Pinecone API key
api_key = os.getenv("PINECONE_API_KEY")

# print(f"Pinecone API Key: {api_key}")

extracted_data = load_pdf('data/')
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone
pc = Pinecone(api_key=api_key)
index_name = "medical-chatbot"
index = pc.Index(index_name)
print(len(text_chunks))
#Creating Embeddings for each Text Chunks and storing in vectors
vectors = [
    {
        "id": f"chunk-{i+1}",  # Unique ID
        "values": embeddings.embed_query(chunk.page_content),  # Embedding values
        "metadata": {"content": chunk.page_content}  # Store the original text
    }
    for i, chunk in enumerate(text_chunks)
]
print(len(vectors))

#Sending the vectors data to Pinecone in batch to avoid the limit
batch_size =200  # Number of vectors per batch
for i in range(0, len(vectors), batch_size):
    batch = vectors[i:i+batch_size]
    index.upsert(vectors=batch, namespace="ns1")
    print(f"Upserted batch {i // batch_size + 1}")


# # Initialize the Pinecone retriever with the embeddings
# retriever = Pi.from_existing_index(index_name=index_name, embedding=embeddings )
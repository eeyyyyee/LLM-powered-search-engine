from sentence_transformers import SentenceTransformer
from pinecone import Pinecone


#Connect to the vector database 
pc = Pinecone(api_key="<Insert api key here>", environment="gcp-starter")
pc.list_indexes()
index = pc.Index("database")


# Loading of embedding model
model = SentenceTransformer('all-MiniLM-L12-v2')


# Create a list of paragraphs
with open('output.txt', 'r') as file:
    paragraphs = file.read().split('\n\n')  


# Embed the paragraph sequentially and store it inside the vector database
counter = 1
for paragraph in paragraphs:
    embedding = model.encode(paragraph)
    embedding_list = embedding.tolist()
    index.upsert(vectors=[{"id":str(counter), "values": embedding_list,"metadata":{"text":paragraph}}])
    counter += 1



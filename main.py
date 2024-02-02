import streamlit as st
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import wordnet
from nltk.corpus import stopwords


# Connecting to database and loading of embedding models
pc = Pinecone(api_key="<Insert api key here>", environment="gcp-starter")
pc.list_indexes()
index = pc.Index("database")
model = SentenceTransformer('all-MiniLM-L12-v2')


# User query expansion by removing stopwords and finding synonyms for non-stopwords, before 
# generating a new expanded query
def synonym_mapping(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

def remove_stopwords(sentence):
    stop_words = set(stopwords.words('english'))
    words = sentence.split()
    filtered_sentence = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_sentence)

def query_expansion(query):
    expanded_query = ""
    query_without_stopwords = remove_stopwords(query)
    for word in query_without_stopwords.split():
        synonyms = synonym_mapping(word)
        expanded_query += word + " "
        for synonym in synonyms:
            expanded_query += synonym + " "
    return expanded_query



def main():
    st.title("Ask questions about the Earth")
    input_text = st.text_input("Enter your text", "")


    if st.button("Answer"):
        expanded_query = query_expansion(input_text)
        query_embedding = model.encode(expanded_query)
        query_embedding_list = query_embedding.tolist()
        results = index.query(vector=query_embedding_list, top_k=15, include_metadata=True)
        st.write(results["matches"][0]["metadata"]["text"])


if __name__ == "__main__":
    main()



# LLM-powered-search-engine

## Files description
1. data.py: Retrieval of data points from the huggingface simple dataset, and writing to a .txt file for cleaning and edits
2. output.txt: Contains the data to be stored in the vector database
3. embedding.py: Reads from the output.txt file, embeds the paragraph, and stores the embeddings and the original text into the Pinecone vector database
4. main.py: Main application where user can enter queries about the Earth, and the most relevant paragraph retrieved based on cosine similarity score will be returned. Query expansion is done on the user's query, where stopwords are removed, and synonyms of the non-stopwords are added. This in theory helps with the retrieval process, as it provides additional semantic information about the query terms, and increases the chances of the query matching relevant paragraphs.
<br>

## How it works:
1. For the dataset, I used huggingface's Wikipedia 20220301.simple dataset
2. For this exercise, I extracted the "Earth" page
3. I wrote the extracted content into a .txt file for further processing, which includes removing lines which only contains the headings, and in turn adding the headings to the relevant paragraphs
4. I created a Pinecone vector database that performs retrieval via cosine similarity
5. I embed the extracted "Earth" text paragraph by paragraph "all-MiniLM-L12-v2" and store it into the Pinecone vector database
6. When the user enters a query, the query is likewise embedded using the same "all-MiniLM-L12-v2" model
7. The Pinecone vector database is then queried, and the most relevant result retrieved via cosine similarity will be displayed to the user
<br>

## What can be improved
1. The data choosen for this task has short paragraphs which makes it easy to encode, as the paragraphs are able to fit within the context limit of many embedding models. If given a dataset with longer paragraphs exceeding the context limit, methods will have to be explored on how to break this long paragraphs into suitable sub-paragraphs for embedding.
2. The current database is small. When more data is introduced, more robust retrieval methods may be required. For example, rather than simply using cosine similarity, we can use hybrid search which involved a mix of traditional keyword search (bm25) and semantic search. Exactly how we should weigh each type of search and how we should combine them into a single metric score is something that has to be experimented with.
3. Adjustments can be made to the query expansion process. In this current implementation, the synonyms that are generated are from wordnet, which tends to be quite broad. What can be done is to generate a new list of synonyms that is more relevant to the current context.
4. Rather than just returning the top results, the current implementation can be modified to return top k results instead. Thereafter, based on which result the user picked, adjustments can be made to boost the selected result upwards.

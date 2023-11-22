## [Official Doc](https://python.langchain.com/docs/modules/data_connection/)

- We will use [This PDF](https://www.uvm.edu/vtvegandberry/Pubs/SampleFoodBusinessPlanOklahomaState.pdf) for learning
- A simple few lines of code to explain this is [here](./QnA_over_doc.py)

## Is this magic? Whats happening?

- To understand what is going under the hood, lets take a look at a few things first

### Embedding vector

- An LLM can capture/ process a few thousands of words at a time.
- To overcome this limitation, we use vector embeddings, what we do is, we try to encode the piece of text into numerical representation
- Embedding tries to capture meaning/ content of the text and represent it as a vector. Texts with similar meaning/ content will have similar embedding

### Vector Database

- When we get the document, it is broken into smaller chunks, embedded and stored in DB
- We create an index out of this DB, and it is used for further querying

### Retrieval

- Now we have a document broken down into smaller chunks of numerical representation, PERFECT!!
- User asks a question, we embed the question also, check which vector has the most similar and return

### Note

- The type of loader, embedding method, vector db, index, etc used depends on use case
- Same embedding might not be used for text and image data, and etc

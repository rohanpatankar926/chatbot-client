### Functions in `chromadb_handlers.py`

`pdf_to_json_and_insert(filepath)`
This function converts a PDF document into JSON format and inserts the document into a list of Document objects. It takes the filepath of the PDF file as input.

filepath: The path to the PDF file to be converted.

`openai_embedding()`
This function initializes and returns an instance of the OpenAIEmbeddings class from the LangChain library. It uses the OpenAI API key and the specified embedding model to create an embedding object.

`upload_to_chroma(docs)`
This function uploads a list of Document objects to the Chroma vector store. It generates embeddings for each document using the OpenAI model and persists the embeddings in the Chroma store.

docs: A list of Document objects to be uploaded to the Chroma vector store.

`retriever_chroma(query)`
This function performs retrieval-based question-answering using the Chroma vector store. It retrieves the most relevant documents from the store based on the given query and returns a question-answering chain that can be used to find answers within the retrieved documents.

query: The question to be answered

## Function in `utils.py` file

`read_yaml(config_path)`

This function reads and loads a YAML configuration file and returns the configuration data as a dictionary.

- `config_path`: The path to the YAML configuration file.

`tiktoken_len(text)`

This function calculates the length of text in terms of tokens using the Tiktoken library. It takes the text as input and returns the number of tokens.

- `text`: The input text.


### API Endpoints

#### `POST /normal_upload`

This endpoint allows you to upload PDF files and process them using the LangChain functions. It accepts a list of PDF files and performs the following steps:

1. Saves the uploaded file(s) to the local filesystem.
2. Converts the PDF files to JSON format using the `pdf_to_json_and_insert` function.
3. Uploads the converted documents to the Chroma vector store using the `upload_to_chroma` function.
4. Removes the temporary file(s) from the filesystem.

Example usage:

```http
POST /normal_upload
Content-Type: multipart/form-data

[PDF File(s)]
```

POST /predict
Content-Type: application/json

{
  "query": "your query"
}

### running the code
`uvicorn app:app`
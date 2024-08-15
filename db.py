from bs4 import BeautifulSoup as BS
import requests as req
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings

url = "https://www.businesstoday.in/latest/economy"
webpage = req.get(url)
anchor = BS(webpage.content, "html.parser")

urls_list = []
for link in anchor.find_all('a'):
    # Ensure that the link has a string and the string length is greater than 35
    if (str(type(link.string)) == "<class 'bs4.element.NavigableString'>"
            and len(link.string) > 35):
        urls_list.append(link.get('href'))  # This extracts and prints the href attribute

### loading the data 
loader = UnstructuredURLLoader(urls=urls_list)
data = loader.load()


### Splitting the data
splitter = RecursiveCharacterTextSplitter(
    separators = ["\n","\n\n", " "],
    chunk_size = 1000,
    chunk_overlap = 100
)

chunks = splitter.split_documents(data)


#### Defining Class for Embedding Functions
class SentenceTransformerEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("all-mpnet-base-v2")        
        embeddings = model.encode(input)
        return [embedding.tolist() for embedding in embeddings]

custom_embeddings=SentenceTransformerEmbeddingFunction()
client = chromadb.PersistentClient(path="C:\\Users\\Bishal\\Documents\\Langchain\\chroma")
collection = client.get_or_create_collection(name="news", embedding_function=custom_embeddings)

for i, doc in enumerate(chunks):
    # Extract page content and metadata
    page_content = doc.page_content     
    source = doc.metadata.get('source')  

    # Insert the document with associated metadata
    collection.upsert(
        ids=[str(i)],  
        documents=[page_content], 
        metadatas=[{'source': source}]
    )
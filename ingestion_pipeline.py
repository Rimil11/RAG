import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


def load_documents(docs_path):
    print("Loading documents from ", docs_path)

    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"The directory {docs_path} does not exist.")

    loader = DirectoryLoader(
        path = docs_path,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={
            "encoding": "utf-8",
            "autodetect_encoding": True
        }
    )

    documents = loader.load()

    if(len(documents)==0):
        raise FileNotFoundError(f"No .txt files found in ({docs_path}).")

    for i, doc in enumerate(documents):
        print(f"Document {i}")
        print(doc)
        
    return documents


def split_documents(documents, chunk_size = 200, chunk_overlap = 0):
    print("Splitting documents into chunks...")

    text_splitter = CharacterTextSplitter(
        chunk_overlap = chunk_overlap,
        chunk_size = chunk_size
    )

    chunks = text_splitter.split_documents(documents)

    if chunks:

        for i, chunk in enumerate(chunks[:5]):
            print(f"\n----(Chunk-{i+1})----")
            print(f"Source: {chunk.metadata['source']}")
            print(f"Length: {len(chunk.page_content)} characters")
            print(f"Content: ")
            print(chunk.page_content)

        if len(chunks) > 5:
            print(f"\n... and {len(chunks)-5} more chunks   ")
    
    return chunks



from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

def create_vector_store(chunks, persist_directory="db/chroma_db"):
    print("Creating embeddings and storing in ChromaDB...")

    embedding_model = OllamaEmbeddings(
        model="mxbai-embed-large"
    )

    # Create an empty vector store
    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
        collection_metadata={"hnsw:space": "cosine"},
    )

    batch_size = 100

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]

        print(
            f"Adding batch {i // batch_size + 1} "
            f"({len(batch)} documents)"
        )

        vectorstore.add_documents(batch)

    print("Finished creating vector store")
    print(f"Total documents stored: {vectorstore._collection.count()}")

    return vectorstore


def main():
    # Define paths
    docs_path = "docs"
    persistent_directory = "db/chroma_db"
    
    # Check if vector store already exists
    if os.path.exists(persistent_directory):
        print("Vector store already exists. No need to re-process documents.")
        
        embedding_model = OllamaEmbeddings(
            model="mxbai-embed-large"
        )

        vectorstore = Chroma(
            persist_directory=persistent_directory,
            embedding_function=embedding_model, 
            collection_metadata={"hnsw:space": "cosine"}
        )
        print(f"Loaded existing vector store with {vectorstore._collection.count()} documents")
        return vectorstore
    
    print("Persistent directory does not exist. Initializing vector store...\n")
    
    # Step 1: Load documents
    documents = load_documents(docs_path)  

    # Step 2: Split into chunks
    chunks = split_documents(documents)

    # # Step 3: Create vector store
    vectorstore = create_vector_store(chunks, persistent_directory)
    
    print("\nIngestion complete! Your documents are now ready for RAG queries.")
    return vectorstore

if __name__ == "__main__":
    main()
    
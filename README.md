# 📚 Retrieval-Augmented Generation (RAG) using LangChain, Ollama & ChromaDB

A simple Retrieval-Augmented Generation (RAG) application built with **LangChain**, **Ollama**, and **ChromaDB**. This project demonstrates how to build a local AI assistant capable of answering questions from custom documents without relying on cloud-based APIs.

---

## 🚀 Features

- 📄 Load documents from a local directory
- ✂️ Split documents into meaningful chunks
- 🧠 Generate embeddings using Ollama
- 💾 Store embeddings in ChromaDB
- 🔍 Retrieve relevant document chunks using similarity search
- 🤖 Generate context-aware responses using Llama 3.2
- 💬 Supports conversational question answering
- 🔒 Runs completely offline (after downloading the models)

---

## 🏗️ Project Structure

```
RAG/
│
├── docs/                     # Knowledge base documents
│   ├── google.txt
│   ├── microsoft.txt
│   ├── nvidia.txt
│   ├── spacex.txt
│   ├── tesla.txt
│   └── rag.txt
│
├── db/
│   └── chroma_db/            # Persistent Chroma vector database
│
├── ingestion_pipeline.py     # Creates embeddings and stores them in ChromaDB
├── retrieval_pipeline.py     # Retrieves relevant documents and generates answers
├── requirements.txt
├── README.md
└── .env
```

---

# 📋 Prerequisites

Before running this project, install the following software:

- Python **3.10 or later**
- Git
- Ollama

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rimil11/RAG.git
```

Move into the project directory:

```bash
cd RAG
```

---

# 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Install Ollama

Download and install Ollama from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

# 5️⃣ Download Required Models

This project uses:

- **Llama 3.2** (LLM)
- **mxbai-embed-large** (Embedding Model)

Download them:

```bash
ollama pull llama3.2
```

```bash
ollama pull mxbai-embed-large
```

---

# 6️⃣ Start Ollama

Make sure the Ollama service is running.

On most systems it starts automatically after installation.

Verify:

```bash
ollama list
```

Expected output:

```
NAME
llama3.2
mxbai-embed-large
```

---

# 7️⃣ Add Your Documents

Place your text documents inside the **docs/** folder.

Example:

```
docs/
    company.txt
    policy.txt
    products.txt
```

---

# 8️⃣ Generate the Vector Database

Run the ingestion pipeline:

```bash
python ingestion_pipeline.py
```

This will:

- Load all documents
- Split documents into chunks
- Generate embeddings
- Store vectors in ChromaDB

After completion, a persistent database will be created in:

```
db/chroma_db
```

---

# 9️⃣ Run the Chat Application

Start the retrieval pipeline:

```bash
python retrieval_pipeline.py
```

Example:

```
You:
What is NVIDIA famous for?

Assistant:
NVIDIA is known for designing graphics processing units (GPUs), AI hardware, and computing platforms...
```

---

# 🔄 Updating the Knowledge Base

Whenever you add, remove, or modify documents inside the **docs/** folder, regenerate the vector database.

Delete the old database:

```
db/chroma_db
```

Run:

```bash
python ingestion_pipeline.py
```

---

# 🧠 How the Project Works

```
Documents
     │
     ▼
Document Loader
     │
     ▼
Text Splitter
     │
     ▼
Embedding Model
     │
     ▼
ChromaDB
     │
     ▼
User Question
     │
     ▼
Retriever
     │
     ▼
Relevant Chunks
     │
     ▼
Llama 3.2
     │
     ▼
Final Answer
```

---

# 🛠️ Technologies Used

- Python
- LangChain
- Ollama
- Llama 3.2
- mxbai-embed-large
- ChromaDB

---

# 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

# 💡 Example Workflow

### Step 1

Add documents.

↓

### Step 2

Run:

```bash
python ingestion_pipeline.py
```

↓

### Step 3

Run:

```bash
python retrieval_pipeline.py
```

↓

### Step 4

Ask questions about your documents.

---

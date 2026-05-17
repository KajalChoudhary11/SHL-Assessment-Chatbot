#SHL Assessment
An AI-powered reccomendation system for SHL assessments built using FASTAPI, FAISS, Sentence Transformers, and Groq LLMS. 
The system uses RAG to provide relevant SHL assessment recommendations based on user hiring requirements.

#Features:- 
The system is designed as a conversational SHL assessment recommendation platform that helps users discover relevant hiring assessments based on job roles, skills, and hiring requirements. It uses semantic search powered by FAISS vector storage and Sentence Transformers to retrieve the most relevant assessments from the SHL catalog. The application follows a Retrieval-Augmented Generation (RAG) architecture, where relevant assessment information is first retrieved and then passed to a large language model to generate grounded and contextual conversational responses. The backend is developed using FastAPI and includes interactive Swagger API documentation for easy testing and integration. Additionally, the chatbot can intelligently handle vague queries by asking clarification questions, refuse unrelated or off-topic requests, and return structured JSON responses containing recommendations, URLs, and other assessment details.

TECH STACK:-
-Python
-FastAPI
-FAISS
-Sentence Transformers
-Groq API
-Pandas
-Uvicorn

#Project Architecture
```text
SHL ASSESSMENT
|
|---APP/
|   |--main.py
|   |--controllers.py      
|   |--dtos.py
|   |--models.py
|   |--services.py
|   |--settings.py
|   |--vectorstore
|       |--__pycache__
|       |--faiss_store.py
|
|---DATA/
|   |--shl_catalog.csv
|   |--shl_catalog.json
|   |--faiss_index.bin
|   |--metadata.pkl
|   |--documents.pkl
|
|---SCRIPTS/
|   |--create_embeddings.py
|   |--fetch_data.py
|   |--preprocess.py
|
|---requirements.txt
|---README.md
|---.env
|---run.py

|

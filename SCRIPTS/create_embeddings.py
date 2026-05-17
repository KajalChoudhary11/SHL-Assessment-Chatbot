import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

with open('DATA/documents.pkl','rb') as f:            #loading the preprocessed documents from the pickle file
    documents = pickle.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')        #using the sentence transformer model to create embeddings for the documents
embeddings = model.encode(documents)    #creating embeddings for the documents
embeddings = np.array(embeddings).astype('float32')    #converting the embeddings to a numpy array of type float32 for compatibility with faiss

dimension = embeddings.shape[1]    #getting the dimension of the embeddings
index = faiss.IndexFlatL2(dimension)    #creating a faiss index for the embeddings using L2 distance
index.add(embeddings)    #adding the embeddings to the faiss index

faiss.write_index(index, 'DATA/faiss_index.bin')    #saving the faiss index to a file for future use    
print("Embeddings created and faiss index saved successfully!")
print(f"Total vectors stored:{index.ntotal}")
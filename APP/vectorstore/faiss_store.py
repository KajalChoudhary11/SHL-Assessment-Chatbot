import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')


index = faiss.read_index('DATA/faiss_index.bin')

with open('DATA/metadata.pkl', 'rb') as f:
    metadata = pickle.load(f)


def search(query, top_k=5):

    # Create query embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype('float32')

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        if idx < len(metadata):

            results.append(metadata[idx])

    return results


if __name__ == "__main__":

    results = search(
        "Java backend developer assessment",
        top_k=5
    )

    for r in results:

        print("Assessment Name:", r["name"])
        print("URL:", r["link"])
        print("Duration:", r["duration"])
        print("Job Levels:", r["job_levels"])

        print("-" * 50)
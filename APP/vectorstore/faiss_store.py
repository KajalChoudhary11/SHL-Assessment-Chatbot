import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("DATA/documents.pkl", "rb") as f:
    documents = pickle.load(f)

with open("DATA/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)

def search(query, top_k=5):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    ).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []

    for idx in top_indices:

        results.append(metadata[idx])

    return results


if __name__ == "__main__":

    results = search("Java backend developer")

    for r in results:

        print(r["name"])
        print(r["link"])

        print("-" * 50)
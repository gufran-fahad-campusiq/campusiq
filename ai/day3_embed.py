from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "How much attendance is required for the exam?",
    "What is the minimum presence needed to sit in finals?",
    "When should the hostel fee be paid?",
]

embeddings = model.encode(sentences)

print("Shape:", embeddings.shape)
print("First 5 numbers of sentence 1:", embeddings[0][:5])

print()
print("Similarity (1 = same meaning, 0 = unrelated):")
print("sentence 1 vs 2:", round(float(util.cos_sim(embeddings[0], embeddings[1])), 3))
print("sentence 1 vs 3:", round(float(util.cos_sim(embeddings[0], embeddings[2])), 3))
print("sentence 2 vs 3:", round(float(util.cos_sim(embeddings[1], embeddings[2])), 3))
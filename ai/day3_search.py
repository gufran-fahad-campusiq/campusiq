import json
from sentence_transformers import SentenceTransformer, util

MIN_SCORE = 0.30

with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

chunk_texts = [c["text"] for c in chunks]
chunk_vectors = model.encode(chunk_texts)


def search(question, top_k=3):
    q_vector = model.encode(question)
    scores = util.cos_sim(q_vector, chunk_vectors)[0]
    ranked = sorted(zip(scores.tolist(), chunks), key=lambda pair: pair[0], reverse=True)
    good = [(s, c) for s, c in ranked if s >= MIN_SCORE]
    return good[:top_k]


for question in [
    "What happens if my attendance is 70 percent?",
    "How many marks do I need to pass?",
    "What time must I be back in the hostel?",
    "What is the menu in the canteen today?",
]:
    print("\nQ:", question)
    results = search(question)
    if not results:
        print("   No relevant rule found.")
    for score, c in results:
        print("  ", round(score, 3), "|", c["topic"], "|", c["text"][:60])
import json

with open("data/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

STOP_WORDS = {"a", "an", "the", "is", "are", "to", "of", "in", "for", "can", "i", "what", "when", "do", "does", "must", "be", "or", "and"}


def words(text):
    cleaned = text.lower().replace("?", "").replace(".", "").replace(",", "")
    return {w for w in cleaned.split() if w not in STOP_WORDS}


def search(question, top_k=3):
    q_words = words(question)
    scored = []
    for c in chunks:
        score = len(q_words & words(c["text"]))
        scored.append((score, c))
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:top_k]


for question in [
    "How much attendance is needed for the exam?",
    "When can visitors come to the hostel?",
    "What is the minimum presence required to sit in finals?",
]:
    print("\nQ:", question)
    for score, c in search(question):
        print("  score", score, "|", c["topic"], "|", c["text"][:60])
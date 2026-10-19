with open("data/sample_rules.txt", "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")

chunks = []
current_topic = ""

for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line.endswith("Rules"):
        current_topic = line
    else:
        chunk = {
            "id": len(chunks) + 1,
            "topic": current_topic,
            "text": line,
        }
        chunks.append(chunk)

print("Total chunks:", len(chunks))
for c in chunks:
    print(c["id"], "|", c["topic"], "|", c["text"][:50])

import json

with open("data/chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks, f, indent=2)

print("Saved", len(chunks), "chunks to data/chunks.json")
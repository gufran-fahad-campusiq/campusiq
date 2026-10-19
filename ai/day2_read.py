# Read the rules file and look at it
with open("data/sample_rules.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Total characters:", len(text))

lines = text.split("\n")
print("Total lines:", len(lines))

print("--- first 3 lines ---")
for line in lines[:3]:
    print(line)
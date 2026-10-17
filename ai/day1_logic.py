students = [
    {"name": "Ravi", "cgpa": 8.4},
    {"name": "Asha", "cgpa": 7.2},
    {"name": "Imran", "cgpa": 9.1},
    {"name": "Zoya", "cgpa": 6.8}
]

def attendance_percent(attended, total):
    return attended / total * 100

for s in students:
    if s["cgpa"] > 8:
        print(s["name"], "has CGPA above 8")
    if s["cgpa"]<7.5:
        print(s["name"], "has CGPA below 7.5")

print(round(attendance_percent(41, 60), 1))
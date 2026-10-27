students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# 1. Top scorer (no max())
top_name = ""
top_score = 0
for s in students:
    if s["score"] > top_score:
        top_score = s["score"]
        top_name = s["name"]
print("Top scorer:", top_name, f"({top_score})")

# 2. Class average
total = 0
for s in students:
    total += s["score"]
average = total / len(students)
print("Class average:", average)

# 3. Unique subjects
subjects = set()
for s in students:
    subjects.add(s["subject"])
print("Subjects offered:", subjects)

# 4. High scorers (above 75)
high_scorers = []
for s in students:
    if s["score"] > 75:
        high_scorers.append(s["name"])
print("High scorers:", high_scorers)

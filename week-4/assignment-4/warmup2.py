student = {
   "name": "Braxton",
   "grade": 12,
   "subjects": ["Python", "Math", "History"],
}

for key, value in student.items():
  print(key, ":", value)

student["graduated"] = False
print(student)

list_a = ["Python", "Java", "C++", "Ruby"]
list_b = ["Python", "JavaScript", "Ruby", "Go"]

set_a = set(list_a)
set_b = set(list_b)

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (only in first):", set_a - set_b)

# 1. Error message:
#    TypeError: can only concatenate str (not "int") to str
#
# 2. What caused it:
#    input() always returns a string, so age was text. I tried to add the
#    number 1 to it, and Python can't add a string and an integer.
#
# 3. How I fixed it:
#    I wrapped input() in int() so age is converted to an integer before the math.

age = int(input("Enter your age: "))
next_year = age + 1
print(f"Next year you will be {next_year}.")

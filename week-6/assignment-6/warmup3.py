# Part 1: a variable inside a function can't be used outside it
def make_message():
    message = "Hello from inside the function"
    print(message)


make_message()
# print(message)
# NameError: name 'message' is not defined


# Part 2: return gets the value out of the function
def get_message():
    message = "Hello from inside the function"
    return message


result = get_message()
print(result)

while True:
    text = input("Enter a positive integer: ")
    if text.isdigit() and int(text) > 0:
        print(f"Got it: {text}")
        break
    print("That's not a positive integer. Try again.")

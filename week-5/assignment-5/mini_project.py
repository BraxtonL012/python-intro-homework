numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        smallest = numbers[0]
        for n in numbers:
            if n < smallest:
                smallest = n
        print(f"Minimum: {smallest}")

    elif choice == "2":
        largest = numbers[0]
        for n in numbers:
            if n > largest:
                largest = n
        print(f"Maximum: {largest}")

    elif choice == "3":
        text = input("Enter a number to search for: ")
        if not text.lstrip("-").isdigit():
            print("Please enter a whole number.")
        else:
            target = int(text)
            found_index = -1
            for i in range(len(numbers)):
                if numbers[i] == target:
                    found_index = i
                    break
            if found_index != -1:
                print(f"Found {target} at index {found_index}.")
            else:
                print(f"{target} was not found.")

    elif choice == "4":
        while True:
            swapped = False
            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
            if not swapped:
                break
        print(f"Sorted list: {numbers}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.")

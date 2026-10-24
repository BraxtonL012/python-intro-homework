day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

valid_days = ["monday", "tuesday", "wednesday"]
valid_times = ["morning", "afternoon", "evening"]

if day not in valid_days:
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday")
elif time_of_day not in valid_times:
    print("Sorry, I don't recognize that time. Try: morning, afternoon, evening")
elif day == "monday":
    if time_of_day == "morning":
        print("Suggestion: Start the week with a workout.")
    elif time_of_day == "afternoon":
        print("Suggestion: Tackle your hardest task while you're focused.")
    else:
        print("Suggestion: Meal prep for the week.")
elif day == "tuesday":
    if time_of_day == "morning":
        print("Suggestion: Morning Python class, a great time to focus!")
    elif time_of_day == "afternoon":
        print("Suggestion: Go for a walk and clear your head.")
    else:
        print("Suggestion: Call a friend or family member.")
else:  # wednesday
    if time_of_day == "morning":
        print("Suggestion: Review your notes before work.")
    elif time_of_day == "afternoon":
        print("Suggestion: Run some errands.")
    else:
        print("Suggestion: Perfect night for a movie or trying a new recipe.")

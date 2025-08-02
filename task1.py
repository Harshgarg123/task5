
marks = {"Alice": 23, "Harsh": 56}


name = input("Enter student name: ")


if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")

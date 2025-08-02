# Step 1: Create a list from 1 to 10
a = list(range(1, 11))
print(f"Original List: {a}")


first_five = a[:5]
print(f"First five elements : {first_five} ")

first_five.reverse()

print(f"Reversed First Five Elements: {first_five}")

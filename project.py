# Step 1: Take input from the user as a string
user_input = input("Enter a number: ")

# Step 2: Clean the input to ignore negative signs (-) or decimal points (.)
# This ensures we only count the actual numeric digits
clean_number = [char for char in user_input if char.isdigit()]

# Step 3: Find the length of the filtered list
digit_count = len(clean_number)

# Step 4: Display the result
print(f"The number of digits is: {digit_count}")


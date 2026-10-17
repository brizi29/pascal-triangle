list1 = []

# Input verification loop
while True:
    try:
        user_input = input("Enter the number of rows to discover (Max 9): ")
        
        # Convert to integer (catches text and special characters)
        n = int(user_input)
        
        # Validate geometric and visual boundaries
        if n <= 0:
            print("Error: Please enter a number greater than 0.")
        elif n > 9:
            print(f"Error: The value {n} exceeds the maximum limit of 9 rows.")
            print("Beyond row 9, the visual formatting of the triangle breaks down.")
        else:
            break # Valid input, exit loop
            
    except ValueError:
        print("Error: Input contains text or special characters. Please enter a whole number only.")

# Pascal's Triangle generation
for i in range(n):
    temp_list=[]
    for j in range(i+1):
        if (j== 0 or j == i):
            temp_list.append(1)
        else:
            temp_list.append(list1[i-1][j-1] +list1[i-1][j])
    list1.append(temp_list)

# Balanced Equilateral Triangle printing block
for i in range(n):
    # Shift each row back by exactly 2 spaces relative to the previous one
    print(" " * (n - i - 1) * 2, end="")
    
    # Center each number within a 2-character block, separated by 2 spaces
    row_strings = [format(list1[i][j], "^2") for j in range(i+1)]
    print("  ".join(row_strings))


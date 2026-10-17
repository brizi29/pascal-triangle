# Pascal's Triangle Generator (Equilateral Layout)

A robust and visually optimized Python CLI application that generates and displays Pascal's Triangle in a perfectly balanced equilateral layout. Built and tested natively inside the Thonny IDE.

## Features

- **Perfect Geometric Alignment:** Uses advanced string formatting (`^2`) and structural spacing mathematical ratios to ensure that both single-digit and double-digit numbers align flawlessly into a symmetrical equilateral triangle.
- **Robust Input Validation:** Implements a strict `try-except` validation loop that rejects floating-point numbers, text strings, and special characters without crashing the program.
- **Visual Safeguard Boundary:** Includes a built-in safety constraint capped at 9 rows. This prevents the output from wrapping or breaking its geometric shape on standard monospaced terminals due to multi-digit expansion.

## Python Source Code

Copy and run this code inside your Python environment:

```python
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
```

## Requirements

- Python 3.x
- Any standard monospaced terminal environment or IDE (optimized for Thonny).

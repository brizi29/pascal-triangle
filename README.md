# Pascal's Triangle Generator (Equilateral Layout)

A robust and visually optimized Python CLI application that generates and displays Pascal's Triangle in a perfectly balanced equilateral layout. Built and tested natively inside the Thonny IDE.

## Features

- **Perfect Geometric Alignment:** Uses advanced string formatting (`^2`) and structural spacing mathematical ratios to ensure that both single-digit and double-digit numbers align flawlessly into a symmetrical equilateral triangle.
- **Robust Input Validation:** Implements a strict `try-except` validation loop that rejects floating-point numbers, text strings, and special characters without crashing the program.
- **Visual Safeguard Boundary:** Includes a built-in safety constraint capped at 9 rows. This prevents the output from wrapping or breaking its geometric shape on standard monospaced terminals due to multi-digit expansion.

## How It Works

1. The program continuously prompts the user for a valid number of rows (integer from 1 to 9).
2. It dynamically builds the triangle matrix using a nested list structure.
3. A tailored printing block dynamically injects proportional indentation and element-centering spacing to preserve the visual symmetry.

## Requirements

- Python 3.x
- Any standard monospaced terminal environment or IDE (optimized for Thonny).

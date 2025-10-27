"""
Task 1 – Simple Function with Arithmetic
---------------------------------------
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = π × radius²
Use the math module for π.
Ask user for radius and print result with 2 decimals.
"""

# Use math.pi for π
import math


def circle_area(radius):
    """Return the area of a circle given its radius.

    Args:
        radius (float): radius of the circle

    Returns:
        float: area of the circle
    """
    return math.pi * (radius**2)


if __name__ == "__main__":
    # Ask user for radius, convert to float, compute and print formatted result
    try:
        user_input = input("Enter radius: ")
        radius = float(user_input)
    except ValueError:
        print("Invalid radius. Please enter a numeric value.")
    else:
        area = circle_area(radius)
        print(f"Area: {area:.2f}")

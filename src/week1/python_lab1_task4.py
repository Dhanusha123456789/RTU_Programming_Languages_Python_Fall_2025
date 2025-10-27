"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    """Count non-space characters in a string."""
    # Count characters that are not whitespace
    return sum(1 for ch in text if not ch.isspace())


def count_words(text):
    """Count number of words in a string."""
    # Split on any whitespace
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    import re

    # Find integers (including negative numbers)
    matches = re.findall(r"-?\d+", text)
    return [int(m) for m in matches]


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    non_space_chars = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else None
    return non_space_chars, word_count, numbers, total, average


if __name__ == "__main__":
    # Read a line of text from the user, analyze it, and print a formatted summary
    text = input("Enter text: ")
    non_space_chars, word_count, numbers, total, average = analyze_text(text)

    print(f"Non-space characters: {non_space_chars}")
    print(f"Word count: {word_count}")
    if numbers:
        print(f"Numbers found: {numbers}")
        print(f"Sum of numbers: {total}")
        # average is a float; format to 2 decimals
        print(f"Average of numbers: {average:.2f}")
    else:
        print("Numbers found: None")
        print("Sum of numbers: 0")
        print("Average of numbers: N/A")

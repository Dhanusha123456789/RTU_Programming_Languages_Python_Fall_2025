"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # Total number of characters
    total_chars = len(text)
    # Word count (split on whitespace)
    words = text.split()
    word_count = len(words)
    # Case-insensitive check for the word 'python'
    contains_python = "python" in text.lower()
    return total_chars, word_count, contains_python


if __name__ == "__main__":
    # Read sentence from input, call function, and print results
    sentence = input("Enter a sentence: ")
    total_chars, word_count, contains_python = analyze_sentence(sentence)
    print(f"Total characters: {total_chars}")
    print(f"Word count: {word_count}")
    print(f"Contains 'Python': {contains_python}")

"""
Description: A simple Password Character Counter

Name: Kaung Sithu
"""


def main():
    """Print the number of character input as asterisks."""
    text = input("Enter a string: ")
    print(count_character(text))


def count_character(txt):
    return len(txt) * "*"


main()

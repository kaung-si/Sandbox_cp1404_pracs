"""
Description: A simple Password Character Counter

Name: Kaung Sithu
"""


def main():
    """Start Program"""
    text = input("Enter a string: ")
    print(count_character(text))
    print("Does it comply with the rule? {}".format(check_char(text)))


def count_character(txt):
    """Return the length of string as asterisks."""
    return len(txt) * "*"


def check_char(txt):
    """Check whether the input text comply the rule."""
    return 8 <= len(txt) <= 20 and '#' in txt


main()

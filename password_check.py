"""
Description: A simple Password Character Counter

Name: Kaung Sithu
"""


def main():
    """Start Program"""
    password = get_password()
    print(display_asterisks(password))
    print("Does it comply with the rule? {}".format(check_char(password)))


def get_password():
    """Prevent blank input"""
    psw = input("Enter a string: ")
    while psw == "":
        psw = input("Enter a string: ")
    return psw


def display_asterisks(password):
    """Return the length of string as asterisks."""
    return len(password) * "*"


def check_char(txt):
    """Check whether the input text comply the rule."""
    return 8 <= len(txt) <= 20 and '#' in txt


main()

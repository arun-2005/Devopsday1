import re
import sys


def is_palindrome(s: str) -> bool:
    s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return s == s[::-1]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
    else:
        text = input("Enter text: ")

    print(
        "Palindrome"
        if is_palindrome(text)
        else "Not a palindrome"
    )
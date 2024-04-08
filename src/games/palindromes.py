import re

sayings = [
    "A man, a plan, a canal, Panama",
    "Gold is where you find it",
    "If I had a hi-fi",
    "Fortune favors the prepared mind",
    "Rats live on no evil star",
    "There is no abstract living",
    "Some men interpret nine memos",
]


def sanitise(candidate):
    return re.sub(r"\W+", "", candidate.lower())


def reverse(cleaned):
    """

    >>> reverse("abcde")
    'edcba'

    """
    return cleaned[::-1]


def is_palindrome(candidate):
    cleaned = sanitise(candidate)
    return cleaned == reverse(cleaned)


def check_for_palindrome(phrase):
    def may_or_may_not_be(candidate):
        return "IS" if is_palindrome(candidate) else "IS NOT"

    print(f"{phrase} {may_or_may_not_be(phrase)} a palindrome")


def play_palindromes():
    for phrase in sayings:
        check_for_palindrome(phrase)

# string_utils.py

def count_vowels(text: str) -> int:
    if text is None:
        raise TypeError("Input cannot be None")

    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def reverse_string(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")

    return text[::-1]


def is_palindrome(text: str) -> bool:
    if text is None:
        raise TypeError("Input cannot be None")

    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(text: str) -> int:
    if text is None:
        raise TypeError("Input cannot be None")

    words = text.split()
    return len(words)


def capitalise_words(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")

    return text.title()


def remove_duplicates(text: str) -> str:
    if text is None:
        raise TypeError("Input cannot be None")

    if text == "":
        return ""

    result = text[0]

    for char in text[1:]:
        if char != result[-1]:
            result += char

    return result
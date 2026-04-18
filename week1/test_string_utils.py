# test_string_utils.py

from string_utils import (
    count_vowels,
    reverse_string,
    is_palindrome,
    word_count,
    capitalise_words,
    remove_duplicates
)


# count_vowels tests

def test_count_vowels_normal():
    assert count_vowels("Hello") == 2


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_count_vowels_case_sensitive():
    assert count_vowels("AEIOU") == 5


# reverse_string tests

def test_reverse_string_normal():
    assert reverse_string("abc") == "cba"


def test_reverse_string_single_character():
    assert reverse_string("a") == "a"


def test_reverse_string_empty():
    assert reverse_string("") == ""


# is_palindrome tests

def test_is_palindrome_true():
    assert is_palindrome("racecar") is True


def test_is_palindrome_ignore_case_and_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False


# word_count tests

def test_word_count_normal():
    assert word_count("Hello World") == 2


def test_word_count_only_spaces():
    assert word_count("   ") == 0


def test_word_count_extra_spaces():
    assert word_count("  hello   world  ") == 2


# capitalise_words tests

def test_capitalise_words_normal():
    assert capitalise_words("hello world") == "Hello World"


def test_capitalise_words_mixed_case():
    assert capitalise_words("hELLo woRLD") == "Hello World"


def test_capitalise_words_empty():
    assert capitalise_words("") == ""


# remove_duplicates tests

def test_remove_duplicates_normal():
    assert remove_duplicates("aaabbbcc") == "abc"


def test_remove_duplicates_single_character():
    assert remove_duplicates("a") == "a"


def test_remove_duplicates_long_duplicates():
    assert remove_duplicates("aaaaabbbbbcccc") == "abc"


# exception handling test

def test_count_vowels_none_input():
    import pytest
    with pytest.raises(TypeError):
        count_vowels(None)
import pytest
from main import count_vowels

def test_all_vowels():
    assert count_vowels("aeiouAEIOU") == 10

def test_no_vowels():
    assert count_vowels("bcdfg BCDFG") == 0

def test_mixed_string():
    assert count_vowels("Hello World!") == 3
    assert count_vowels("PyThOn ProGRaMmiNg") == 4
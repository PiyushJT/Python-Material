def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_words(s):
    return len(s.split())

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def capitalize_words(s):
    return s.title()

def remove_spaces(s):
    return s.replace(' ', '')

def is_palindrome(s):
    s = s.replace(' ', '').lower()
    return s == s[::-1]

"""

Write a python program to make a module which contain all
the basic functions related to string 
and import that module in another file and use that
functions with string given by user.

"""

from modules import string_methods

str = "The courageous fallen! The anguished fallen! Their lives have meaning because we the living refuse to forget them! And as we ride to certain death, we trust our successors to do the same for us! Because my soldiers do not buckle or yield when faced with the cruelty of this world! My soldiers push forward! My soldiers scream out! My soldiers RAAAAAGE!"

print(string_methods.capitalize_words(str))

print(string_methods.count_vowels(str))

print(string_methods.count_words(str))

print(string_methods.is_palindrome(str))

print(string_methods.remove_spaces(str))

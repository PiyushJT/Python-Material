"""

Write a class called WordPlay. It should have a constructor
that holds a list of words. The user of the class should pass the
list of words through constructor, which user wants to use
for the class. The class should have following methods:
words_with_length(length) — returns a list of all the
words of length length
starts_with(char1) — returns a list of all the words
that start with char1
ends_with(char2) — returns a list of all the words
that end with char2
palindromes() — returns a list of all the palindromes
in the list
only(str1) — returns a list of the words that contain
only those leters in str1
avoids(str2) — returns a list of the words that contain
none of the leters in str2
Make Required object for WordPlay class and test all the methods.
For Example:

"""


class WordPlay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        lst = []
        for w in self.words:
            if len(w) == length:
                lst.append(w)
        return lst

    def starts_with(self, char1):
        lst = []
        for w in self.words:
            if w.startswith(char1):
                lst.append(w)
        return lst

    def ends_with(self, char2):
        lst = []
        for w in self.words:
            if w.endswith(char2):
                lst.append(w)
        return lst


    def palindromes(self):
        lst = []
        for w in self.words:
            if w == w[::-1]:
                lst.append(w)
        return lst

    def only(self, chars):
        lst = []
        for word in self.words:
            for letter in word:
                if letter not in chars:
                    break
            else:
                lst.append(word)
                
        return lst

    def avoids(self, chars):
        lst = []
        for word in self.words:
            for letter in word:
                if letter in chars:
                    break
            else:
                lst.append(word)
                
        return lst

sample = [
    "apple",
    "banana",
    "find",
    "dictionary",
    "set",
    "tuple",
    "list",
    "malayalam",
    "nayan",
    "grind",
    "apricot",
]
wp = WordPlay(sample)

print("words_with_length(5):", wp.words_with_length(5))
print("starts_with('a'):", wp.starts_with("a"))
print("ends_with('d'):", wp.ends_with("d"))
print("palindromes():", wp.palindromes())
print("only('bna'):", wp.only("bna"))
print("avoids('amkd'):", wp.avoids("amkd"))

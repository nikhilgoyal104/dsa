# T=n,S=1
def main(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    n, letterToWord, wordToLetter = len(pattern), {}, {}
    for i in range(n):
        letter, word = pattern[i], words[i]
        if letter in letterToWord and letterToWord[letter] != word:
            return False
        letterToWord[letter] = word
    for i in range(n):
        letter, word = pattern[i], words[i]
        if word in wordToLetter and wordToLetter[word] != letter:
            return False
        wordToLetter[word] = letter
    return True


for pattern, s in [
    ('abba', 'dog cat cat dog'),
    ('abba', 'dog cat cat fish'),
    ('aaaa', 'dog cat cat dog'),
    ('abba', 'dog dog dog dog')
]:
    print(main(pattern, s))

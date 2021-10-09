from collections import Counter


# https://www.geeksforgeeks.org/removing-string-that-is-an-anagram-of-an-earlier-string/
def main(text):
    res, vis = [], set()
    for i in range(len(text)):
        word = ''.join(sorted(text[i]))
        if word not in vis:
            res.append(text[i])
            vis.add(word)
    res.sort()
    return res


for text in [
    ['code', 'doce', 'ecod', 'framer', 'frame'],
    ['code', 'aaagmnrs', 'anagrams', 'doce'],
    ['poke', 'pkoe', 'okpe', 'ekop']
]:
    print(main(text))

# https://github.com/AnoshaRehan/Coding-Challenges/blob/main/damDesign.py

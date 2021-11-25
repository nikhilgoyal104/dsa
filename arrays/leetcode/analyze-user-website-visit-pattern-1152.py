from itertools import combinations
from collections import defaultdict, Counter

inputs = [
    (
        ['joe', 'joe', 'joe', 'james', 'james', 'james', 'james', 'mary', 'mary', 'mary'],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ['home', 'about', 'career', 'home', 'cart', 'maps', 'home', 'home', 'about', 'career']
    ),
    (
        ['ua', 'ua', 'ua', 'ub', 'ub', 'ub'],
        [1, 2, 3, 4, 5, 6],
        ['a', 'b', 'a', 'a', 'b', 'c']
    )
]


def main(username, timestamp, website):
    packedTuple = zip(timestamp, username, website)
    userToSites = defaultdict(list)
    for time, user, site in sorted(packedTuple):
        userToSites[user].append(site)
    patternCount = Counter()
    for websiteList in userToSites.values():
        patterns = set(combinations(websiteList, 3))
        for pattern in patterns:
            patternCount[pattern] += 1
    return min(patternCount, key=lambda x: (-patternCount[x], x))


for username, timestamp, website in inputs:
    print(main(username, timestamp, website))

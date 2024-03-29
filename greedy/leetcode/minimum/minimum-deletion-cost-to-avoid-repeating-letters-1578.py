# T=n,S=1
def main(s, cost):
    res = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            res += min(cost[i], cost[i - 1])
            cost[i] = max(cost[i], cost[i - 1])
    return res


for s, cost in [
    ('abaac', [1, 2, 3, 4, 5]),
    ('abc', [1, 2, 3]),
    ('aabaa', [1, 2, 3, 4, 1])
]:
    print(main(s, cost))

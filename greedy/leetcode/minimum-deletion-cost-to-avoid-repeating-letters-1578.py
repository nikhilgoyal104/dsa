# T=n,S=1
def main(s, cost):
    res, n = 0, len(s)
    for i in range(1, n):
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

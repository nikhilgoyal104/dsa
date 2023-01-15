def main(s):
    res = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) == len(set(substring)):
                res += 1
    return res


print(main('abcd'))

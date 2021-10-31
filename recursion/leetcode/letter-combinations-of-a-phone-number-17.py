keypad = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

inputs = [
    '', '2', '23',
]


# T=4ⁿn,S=n²
def main(nums):
    def dfs(i):
        if i == len(nums):
            return ['']
        res = []
        for letter in keypad[nums[i]]:
            for path in dfs(i + 1):
                res.append(letter + path)
        return res

    return dfs(0)


for nums in inputs:
    print(main(nums))


# T=4ⁿn,S=n
def main(nums):
    def dfs(i, path):
        if len(path) == len(nums):
            print(''.join(path), end=' ')
            return
        for letter in keypad[nums[i]]:
            path.append(letter)
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])


for nums in inputs:
    main(nums)
    print()

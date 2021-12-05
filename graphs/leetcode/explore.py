def main():
    s = 'nik'
    for i in range(len(s)):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            print(s[:i] + char + s[i + 1:], end='|')
        print()


main()

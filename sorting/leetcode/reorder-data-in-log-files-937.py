# T=mnlogn,S=mn
def main(logs):
    def sort(log):
        if log[-1].isnumeric():
            return 1,
        identifier, content = log.split(' ', maxsplit=1)
        return 0, content, identifier

    return sorted(logs, key=sort)


for logs in [
    ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'],
    ['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo'],
    ['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo', 'a2 act car'],
    ['27 85717 7', '2 y xyr fc', '52 314 99', 'd 046099 0', 'm azv x f', '7e apw c y', '8 hyyq z p', '6 3272401',
     'c otdk cl', '8 ksif m u']
]:
    print(main(logs))

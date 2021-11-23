def apply(operator, num2, num1):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return int(num1 / num2)


# T=n,S=n
def main(s):
    stack = []
    for char in s:
        if char not in '+-*/':
            stack.append(int(char))
        else:
            stack.append(apply(char, stack.pop(), stack.pop()))
    return stack.pop()


for s in [
    ['2', '1', '+', '3', '*'],
    ['4', '13', '5', '/', '+'],
    ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']
]:
    print(main(s))

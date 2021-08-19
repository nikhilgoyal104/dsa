print(min('c', 'b', 'a', 'Y', 'Z'))
print(min('c', 'b', 'a', 'Y', 'Z', key=str.lower))
print(min('java', 'python', 'z++'))
print(min('java', 'python', 'z++', key=len))

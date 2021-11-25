# T=n,S=1
def main(instructions):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    i = x = y = 0
    for instruction in instructions:
        if instruction == 'L':
            i = (i + 3) % 4
        elif instruction == 'R':
            i = (i + 1) % 4
        else:
            x += directions[i][0]
            y += directions[i][1]
    return (x, y) == (0, 0) or i != 0


for instructions in [
    'GGLLGG',
    'GG'
]:
    print(main(instructions))

from heapq import *


# T=nlogn,S=n
def main(sticks):
    res = 0
    heapify(sticks)
    while len(sticks) > 1:
        cost = heappop(sticks) + heappop(sticks)
        res += cost
        heappush(sticks, cost)
    return res


for sticks in [
    [5],
    [2, 4, 3],
    [1, 8, 3, 5],
    [1, 2, 3, 4, 5],
    [3, 7, 1, 10, 8],
    [1175, 8967, 1382, 8748, 8612, 7067, 5979, 8237, 9691, 389, 5801, 7387, 8620, 6674, 1610, 7444, 6969, 970, 9463,
     7727, 5044, 1834, 3426, 3192, 9473, 2300, 3647, 6492, 3166, 3486, 454, 6077, 670, 4929, 1266, 8288, 8554, 8432,
     4724, 8553, 2442, 1776, 2704, 1276, 2933, 3376, 8259, 8548, 1563, 3884]
]:
    print(main(sticks))

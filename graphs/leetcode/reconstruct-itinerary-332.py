from collections import defaultdict
from heapq import *


def main(edges):
    res, graph = [], defaultdict(list)
    for src, dest in edges:
        heappush(graph[src], dest)

    def dfs(src):
        while graph[src]:
            dfs(heappop(graph[src]))
        res.append(src)

    dfs('JFK')
    return res[::-1]


for edges in [
    [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']],
    [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']],
    [['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]
]:
    print(main(edges))

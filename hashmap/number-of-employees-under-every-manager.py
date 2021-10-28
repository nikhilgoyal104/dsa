from pprint import pprint


def construct(mapping):
    graph, src = {person: [] for person in mapping.keys()}, None
    for employee, manager in mapping.items():
        if employee != manager:
            graph[manager].append(employee)
        else:
            src = employee
    return graph, src


def x(mapping):
    graph, src = construct(mapping)
    res = {}

    def dfs(src):
        res[src] = 1
        for nbr in graph[src]:
            res[src] += dfs(nbr)
        return res[src]

    dfs(src)
    return res


def y(mapping):
    graph, src = construct(mapping)
    res = {}

    def dfs(src):
        res[src] = []
        for nbr in graph[src]:
            res[src] += [nbr] + dfs(nbr)
        return res[src]

    dfs(src)
    return res


for mapping in [
    {
        'A': 'C',
        'B': 'C',
        'C': 'F',
        'D': 'E',
        'E': 'F',
        'F': 'F'
    },
    {
        'A': 'A',
        'B': 'A',
        'C': 'B',
        'D': 'B',
        'E': 'D',
        'F': 'E'
    }
]:
    pprint(x(mapping), width=1)
    pprint(y(mapping), width=50)

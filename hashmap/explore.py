def x(mapping):
    graph = {person: [] for person in mapping.keys()}
    edges, src = mapping.items(), ''
    for employee, manager in edges:
        if employee == manager:
            src = employee
            continue
        graph[manager].append(employee)

    res = {}

    def dfs(src):
        count = 0
        for nbr in graph[src]:
            count += 1 + dfs(nbr)
        res[src] = count
        return count

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
    print(x(mapping))

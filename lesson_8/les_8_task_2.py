""" 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    ways = []
    cons_vert = start

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    print('*' * 50)
    print(f'Кратчайшие пути до каждой вершины из стартовой {cons_vert}:')
    for i in range(length):
        ways.append([])
        if i == cons_vert:
            ways[i].append('Это стартовая вершина')
        elif cost[i] == float('inf'):
            ways[i].append('До этой вершины из стартовой не добраться')
        else:
            j = i
            ways[i].append(j)
            while j != cons_vert:
                j = parent[j]
                ways[i].append(j)
            ways[i].reverse()
        print(f'до {i}-й: {ways[i]}')
    print('*' * 50)

    return cost


grf = [
    [0, 2, 1, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
    [3, 0, 0, 3, 0, 2, 0, 9, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 6, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0, 0]
]
n = int(input('От какой вершины находим пути: '))
print(dijkstra(grf, n), '- расстояния кратчайших путей до каждой вершины')

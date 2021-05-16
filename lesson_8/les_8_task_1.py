""" 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было? Примечание. Решите задачу при помощи построения графа.
"""

n = int(input('Enter friends amount: '))
# Составим матрицу смежности, где 0 - рукопожатия не было (сам себе руку не пожимал)
#                                 1 - рукопожатие было (с другом)
graph = [[(0 if i == j else 1) for i in range(n)] for j in range(n)]
for i in range(n):
    print(graph[i])

# Посчитаем количество единиц в матрице(рукопожатий друзей) и поделим на 2, учитывая повторные рукопожатия.
hands = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            hands += 1
hands /= 2

print(f'{int(hands)} handshakes between {n} friends occurred.')

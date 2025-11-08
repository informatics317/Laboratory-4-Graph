class Graf:
    def __init__(self):
        self.graf = {}

    def svuzy(self, u, v):
        if u not in self.graf:
            self.graf[u] = []
        if v not in self.graf:
            self.graf[v] = []

        self.graf[u].append(v)
        self.graf[v].append(u)


    def dfs(self, start):
        visit = set()
        stack = [start]
        while stack:
            vershina = stack.pop()
            if vershina not in visit:
                print(vershina, end = ' ')
                visit.add(vershina)
                for neighbor in reversed(self.graf[vershina]):
                    if neighbor not in visit:
                        stack.append(neighbor)

        print()

    def bfs(self, start):
        visit = set()
        queue = [start]
        visit.add(start)
        while queue:
            vershina = queue.pop(0)
            print(vershina, end = ' ')
            for neighbor in self.graf[vershina]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)

g = Graf()

g.svuzy(0, 1)
g.svuzy(0, 2)
g.svuzy(1, 3)
g.svuzy(1, 4)
g.svuzy(2, 5)
g.svuzy(2, 6)
g.svuzy(3, 7)
g.svuzy(4, 8)
g.svuzy(5, 9)
g.svuzy(6, 10)
g.svuzy(7, 8)
g.svuzy(8, 9)
g.svuzy(9, 10)
g.svuzy(10, 11)


print('Обход в глубину (DFS):')
g.dfs(0)

print('Обход в ширину (BFS):')
g.bfs(0)



















































class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def delete_node(self, node):
        if node in self.adj:
            del self.adj[node]
            for n in self.adj:
                self.adj[n] = [(nbr, c) for nbr, c in self.adj[n] if nbr != node]

    def add_edge(self, n1, n2, cost):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1].append((n2, cost))
            self.adj[n2].append((n1, cost))
        else:
            print("One or both nodes not found!")

    def delete_edge(self, n1, n2):
        if n1 in self.adj and n2 in self.adj:
            self.adj[n1] = [(nbr, c) for nbr, c in self.adj[n1] if nbr != n2]
            self.adj[n2] = [(nbr, c) for nbr, c in self.adj[n2] if nbr != n1]

    def display(self):
        for node in self.adj:
            print(node, "->", self.adj[node])


def a_star_search(graph, start, goal, heuristic):
    open_list = [start]
    closed_list = []

    g = {start: 0}
    f = {start: heuristic[start]}
    parent = {start: None}

    step = 1

    while open_list:
        print("\nStep", step)
        print("OPEN:", open_list)
        print("CLOSED:", closed_list)

        # Select node with minimum f value
        current = min(open_list, key=lambda x: f[x])

        print("Selected:", current,
              "g:", g[current],
              "h:", heuristic[current],
              "f:", f[current])

        # Goal check
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()

            print("Path:", " -> ".join(path))
            print("Total Cost:", g[goal])
            return

        open_list.remove(current)
        closed_list.append(current)

        for neighbor, cost in graph.adj[current]:

            if neighbor in closed_list:
                continue

            tentative_g = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)

            elif tentative_g >= g.get(neighbor, float('inf')):
                continue

            parent[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + heuristic[neighbor]

        step += 1

    print("No path found!")


# ---------------- MAIN PROGRAM ---------------- #

graph = Graph()

n = int(input("Enter number of nodes: "))
for _ in range(n):
    graph.add_node(input("Enter node: "))

e = int(input("Enter number of edges: "))
for _ in range(e):
    n1 = input("Enter node 1: ")
    n2 = input("Enter node 2: ")
    cost = int(input("Enter cost: "))
    graph.add_edge(n1, n2, cost)

while True:
    print("\n1.Add Edge")
    print("2.Delete Edge")
    print("3.Add Node")
    print("4.Delete Node")
    print("5.A* Search")
    print("6.Display Graph")
    print("7.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        n1 = input("Enter node 1: ")
        n2 = input("Enter node 2: ")
        cost = int(input("Enter cost: "))
        graph.add_edge(n1, n2, cost)

    elif choice == 2:
        n1 = input("Enter node 1: ")
        n2 = input("Enter node 2: ")
        graph.delete_edge(n1, n2)

    elif choice == 3:
        node = input("Enter node: ")
        graph.add_node(node)

    elif choice == 4:
        node = input("Enter node: ")
        graph.delete_node(node)

    elif choice == 5:
        heuristic = {}
        print("Enter heuristic values:")
        for node in graph.adj:
            heuristic[node] = int(input(f"h({node}) = "))

        start = input("Enter start node: ")
        goal = input("Enter goal node: ")

        if start not in graph.adj or goal not in graph.adj:
            print("Invalid start or goal node!")
        else:
            a_star_search(graph, start, goal, heuristic)

    elif choice == 6:
        graph.display()

    elif choice == 7:
        break
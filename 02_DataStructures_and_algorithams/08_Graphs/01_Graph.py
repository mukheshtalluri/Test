class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(f"{vertex} : {self.adjacency_list[vertex]}")

    def breath_first_search(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end = ' ')
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    visited.add(adjacency_vertex)
                    queue.append(adjacency_vertex)


    def depth_first_search(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    stack.append(adjacency_vertex)

    def topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)
        for other_vertex in self.adjacency_list[vertex]:
            if other_vertex not in visited:
                self.topological_sort_util(other_vertex, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []
        for vertex in list(self.adjacency_list):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)
        print(stack)

            

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_vertex('H')
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('E', 'G')
graph.add_edge('G', 'H')
graph.add_edge('F', 'H')
graph.topological_sort()







#? Adjacency Matrices
    #? a table where each row and column represents a location, and the entries indicate whether there's a direct road (edge) between those locations.
    #? If there's an edge connecting the locations, the entry is 1; otherwise, it's 0

#? Example:
adj_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

#! Adjacency Lists
    #! A more compact representation of a graph.
    #! Lists each vertex and its neighboring vertices
    #! Useful for sparse graphs where there are fewer connections

#! Example:
adj_list = {
    1: [1, 3],
    2: [0, 2, 3],
    3: [2, 4],
    4: [1, 4]
}

#* Degrees - the number of edges leading to or from a vertex
#? Paths - a sequence of locations where each adjacent pair is connected by a road (edge)
#! Cycles - a path that starts and ends at the same location
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1][vertex2] = weight
            self.vertices[vertex2][vertex1] = weight

    def dijkstra(self, start):
        distances = {vertex: float("inf") for vertex in self.vertices}
        distances[start] = 0
        pq = [(0, start)] #Priority queue of (distance, vertex)

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.vertices[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    # def display(self):
    #     for vertex in self.vertices:
    #         print(vertex, "->", " -> ".join(map(str, self.vertices[vertex])))
    #
    # def has_path(self, start, end, visited=None):
    #     if visited is None:
    #         visited = set()
    #     visited.add(start)
    #     if start == end:
    #         return True
    #     for neighbor in self.vertices[start]:
    #         if neighbor not in visited:
    #             if self.has_path(neighbor, end, visited):
    #                 return True
    #     return False

graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1, 2, 2)
graph.add_edge(2, 3, 5)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 1, 2)
# graph.display()
# print("Path exists between 1 and 3:", graph.has_path(1, 3))

distances = graph.dijkstra(3)
print("Shortest distances from vertex 1:", distances)





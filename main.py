import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge(self, source, destination, weight):
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

    def dijkstra(self, start):
        distances = {vertex: float("inf") for vertex in self.vertices}
        distances[start] = 0

        previous_vertices = {vertex: None for vertex in self.vertices}

        # Priority queue (min-heap) to process vertices
        priority_queue = [(0, start)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.get_neighbors(current_vertex).items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances, previous_vertices



graph1 = Graph()
graph1.add_vertex(1)
graph1.add_vertex(2)
graph1.add_vertex(3)
graph1.add_edge(1, 2, 5)
graph1.add_edge(2, 3, 3)

print(graph1.vertices)

distances1, previous_vertices1 = graph1.dijkstra(1)
print("Distances: ", distances1)
print("Previous vertices: ", previous_vertices1)

graph2 = Graph()
graph2.add_vertex(4)
graph2.add_vertex(5)
graph2.add_vertex(6)
graph2.add_edge(4, 5, 10)
graph2.add_edge(5, 6, 20)

print(graph2.vertices)

distances2, previous_vertices2 = graph2.dijkstra(5)
print("Distances: ", distances2)
print("Previous vertices: ", previous_vertices2)


#! Time Complexity: O((V + E) logV); V = # of vertices; E = # of edges
#! Space Complexity: O(V + E); V = # of vertices; E = # of edges
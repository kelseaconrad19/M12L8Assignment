import heapq

class NavigationSystem:
    def __init__(self):
        self.intersections = {}

    def add_intersection(self, intersection_id):
        if intersection_id not in self.intersections:
            self.intersections[intersection_id] = {}

    def add_road(self, intersection1, intersection2, distance):
        if intersection1 in self.intersections and intersection2 in self.intersections:
            self.intersections[intersection1][intersection2] = distance
            self.intersections[intersection2][intersection1] = distance

    def shortest_route(self, start, end):
        distances = {intersection: float('inf') for intersection in self.intersections}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_intersection = heapq.heappop(pq)
            if current_distance > distances[current_intersection]:
                continue
            for neighbor, distance in self.intersections[current_intersection].items():
                total_distance = current_distance + distance
                if total_distance < distances[neighbor]:
                    distances[neighbor] = total_distance
                    heapq.heappush(pq, (total_distance, neighbor))

        return distances[end]

navigation = NavigationSystem()
navigation.add_intersection(1)
navigation.add_intersection(2)
navigation.add_intersection(3)
navigation.add_intersection(4)

navigation.add_road(1, 2, 5)
navigation.add_road(2, 3, 3)
navigation.add_road(3, 4, 4)
navigation.add_road(4, 1, 6)

shortest_distance = navigation.shortest_route(1, 3)
print("Shortest distance between intersections 1 and 3: ", shortest_distance)
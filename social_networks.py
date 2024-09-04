import heapq

class SocialNetwork:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id):
        if user_id not in self.users:
            self.users[user_id] = []

    def add_friendship(self, user1, user2):
        if user1 in self.users and user2 in self.users:
            self.users[user1].append(user2)
            self.users[user2].append(user1)

    def find_shortest_path(self, start, end):
        distances = {user: float('inf') for user in self.users}
        distances[start] = 0
        pq = [(0, start)]

        while pq:
            current_distance, current_user = heapq.heappop(pq)
            if current_distance > distances[current_user]:
                continue
            for friend in self.users[current_user]:
                distance = current_distance + 1
                if distance < distances[friend]:
                    distances[friend] = distance
                    heapq.heappush(pq, (distance, friend))

        shortest_path = []
        current_user = end
        while current_user != start:
            shortest_path.append(current_user)
            for friend in self.users[current_user]:
                if distances[friend] == distances[current_user] - 1:
                    current_user = friend
                    break
        shortest_path.append(start)
        return shortest_path[::-1]

network = SocialNetwork()
network.add_user(1)
network.add_user(2)
network.add_user(3)
network.add_user(4)
network.add_friendship(1, 2)
network.add_friendship(2, 3)
network.add_friendship(3, 4)
network.add_friendship(4, 1)

shortest_path = network.find_shortest_path(1, 3)
print(
    "Shortest path from user 1 to user 3: ", shortest_path)
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in range(self.V)}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for weight, neighbor in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

    def bfs(self, start):
        visited = [False] * self.V
        queue = [start]
        visited[start] = True
        result = []

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for weight, neighbor in self.graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = [False] * self.V
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)
            for weight, neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start)
        return result
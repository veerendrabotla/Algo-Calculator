import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store graph edges

    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))  # Add edge with weight

    def kruskal(self):
        """Kruskal's algorithm to find the Minimum Spanning Tree (MST)."""
        self.graph.sort()  # Sort edges based on weight
        parent = {}
        rank = {}

        def find(v):
            if parent[v] != v:
                parent[v] = find(parent[v])
            return parent[v]

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                elif rank[root_u] < rank[root_v]:
                    parent[root_u] = root_v
                else:
                    parent[root_v] = root_u
                    rank[root_u] += 1

        for vertex in range(self.V):
            parent[vertex] = vertex
            rank[vertex] = 0

        mst = []
        for weight, u, v in self.graph:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))

        return mst


def prims(graph, start):
    """Prim's algorithm to find the Minimum Spanning Tree (MST)."""
    mst = []
    visited = [False] * graph.V
    min_heap = [(0, start, -1)]  # (weight, current_vertex, parent_vertex)

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        if parent != -1:
            mst.append((parent, u, weight))

        for v, w in graph.graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return mst


def huffman_coding(frequencies):
    """Huffman coding algorithm to create a binary tree for encoding characters."""
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
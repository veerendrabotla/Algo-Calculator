import heapq


def dijkstra(graph, start):
    """Dijkstra's algorithm to find the shortest path from start to all other vertices."""
    distances = {vertex: float('infinity') for vertex in range(graph.V)}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


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


def activity_selection(activities):
    """Activity Selection Problem: Select the maximum number of activities that don't overlap."""
    # Sort activities based on their finish time
    activities.sort(key=lambda x: x[1])
    selected_activities = [activities[0]]  # Select the first activity

    last_finish_time = activities[0][1]
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish_time:  # If the start time is greater than or equal to the last finish time
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities
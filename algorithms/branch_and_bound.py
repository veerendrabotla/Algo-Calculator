def traveling_salesman_brute_force(graph):
    """Solves the Traveling Salesman Problem using brute force."""
    from itertools import permutations

    n = len(graph)
    min_path = float('inf')
    best_route = []

    for perm in permutations(range(n)):
        current_cost = 0
        for i in range(n):
            current_cost += graph[perm[i]][perm[(i + 1) % n]]
        if current_cost < min_path:
            min_path = current_cost
            best_route = perm

    return min_path, best_route
# algo_calculator/metrics_calculator/complexity.py
def analyze_complexity(algo_name, n):
    complexities = {
        "merge_sort": f"Time Complexity: O(n log n), Space Complexity: O(n)",
        "quick_sort": f"Time Complexity: O(n log n) (average), Space Complexity: O(log n)"
    }
    print(f"Complexity Analysis for {algo_name}: {complexities.get(algo_name, 'Unknown')}")

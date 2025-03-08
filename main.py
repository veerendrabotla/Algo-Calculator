import tkinter as tk
from tkinter import ttk, messagebox
import time
from algorithms.divide_conquer import merge_sort, quick_sort, binary_search
from algorithms.dynamic_programming import fibonacci, knapsack, longest_common_subsequence, matrix_chain_multiplication, coin_change
from algorithms.greedy_algorithms import huffman_coding
from algorithms.backtracking import n_queens, sudoku_solver
from algorithms.graph_algorithms import Graph

from algorithms.branch_and_bound import traveling_salesman_brute_force
from algorithms.randomized_algorithms import randomized_quick_sort, random_sampling
from algorithms.string_algorithms import kmp_search, longest_common_subsequence as lcs
from metrics_calculator.complexity import analyze_complexity
from help_content import help_instructions  # Import help content

# Global Variables
selected_algorithm = None

# Algorithm Categories and Types
algorithm_categories = {
    "Divide and Conquer": ["Merge Sort", "Quick Sort", "Binary Search", "Strassen's Matrix Multiplication"],
    "Dynamic Programming": ["Fibonacci Sequence", "Knapsack Problem", "Longest Common Subsequence", "Matrix Chain Multiplication", "Coin Change Problem"],
    "Greedy Algorithms": ["Prim's Algorithm", "Kruskal's Algorithm", "Dijkstra's Algorithm", "Huffman Coding", "Activity Selection Problem"],
    "Backtracking": ["N-Queens Problem", "Sudoku Solver"],
    "Graph Algorithms": ["Depth-First Search", "Breadth-First Search"],
    "Branch and Bound": ["Traveling Salesman Problem"],
    "Randomized Algorithms": ["Randomized Quick Sort", "Random Sampling"],
    "String Algorithms": ["Knuth-Morris-Pratt", "Rabin-Karp", "Longest Common Substring"],
}

# Algorithm Execution Function
def execute_algorithm():
    input_data = entry_var.get().strip()
    
    if not selected_algorithm:
        messagebox.showerror("Error", "Please select an algorithm!")
        return

    try:
        if selected_algorithm == "Merge Sort":
            arr = list(map(int, input_data.split()))
            result = merge_sort(arr)
        elif selected_algorithm == "Quick Sort":
            arr = list(map(int, input_data.split()))
            result = quick_sort(arr)
        elif selected_algorithm == "Binary Search":
            arr, target = input_data.split(';')
            arr = list(map(int, arr.split()))
            target = int(target)
            result = binary_search(arr, target)
        elif selected_algorithm == "Fibonacci Sequence":
            n = int(input_data)
            result = fibonacci(n)
        elif selected_algorithm == "Knapsack Problem":
            items = [tuple(map(int, item.split(','))) for item in input_data.split()]
            weights, values = zip(*items)
            result = knapsack(weights, values, capacity=10)  # Example capacity
        elif selected_algorithm == "Longest Common Subsequence":
            seq1, seq2 = input_data.split(';')
            result = longest_common_subsequence(seq1, seq2)
        elif selected_algorithm == "Matrix Chain Multiplication":
            dimensions = list(map(int, input_data.split(',')))
            result = matrix_chain_multiplication(dimensions)
        elif selected_algorithm == "Coin Change Problem":
            coins, amount = input_data.split(';')
            coins = list(map(int, coins.split(',')))
            amount = int(amount)
            result = coin_change(coins, amount)
        elif selected_algorithm == "Prim's Algorithm":
            # Example input: "0,1,2;1,2,3;2,3,4"
            edges = [tuple(map(int, edge.split(','))) for edge in input_data.split(';')]
            graph = Graph(len(edges))
            for u, v, w in edges:
                graph.add_edge(u, v, w)
            result = graph.prims(0)  # Starting from vertex 0
        elif selected_algorithm == "Kruskal's Algorithm":
            edges = [tuple(map(int, edge.split(','))) for edge in input_data.split(';')]
            graph = Graph(len(edges))
            for u, v, w in edges:
                graph.add_edge(u, v, w)
            result = graph.kruskal()
        elif selected_algorithm == "Dijkstra's Algorithm":
            edges = [tuple(map(int, edge.split(',' ))) for edge in input_data.split(';')]
            graph = Graph(len(edges))
            for u, v, w in edges:
                graph.add_edge(u, v, w)
            result = graph.dijkstra(0)  # Starting from vertex 0
        elif selected_algorithm == "Huffman Coding":
            frequencies = eval(input_data)  # Expecting a dictionary input
            result = huffman_coding(frequencies)
        elif selected_algorithm == "N-Queens Problem":
            n = int(input_data)
            result = n_queens(n)
        elif selected_algorithm == "Sudoku Solver":
            board = [list(map(int, row.split())) for row in input_data.split(';')]
            result = sudoku_solver(board)
        elif selected_algorithm == "Traveling Salesman Problem":
            distances = [list(map(int, row.split(','))) for row in input_data.split(';')]
            result = traveling_salesman_brute_force(distances)
        elif selected_algorithm == "Randomized Quick Sort":
            arr = list(map(int, input_data.split()))
            result = randomized_quick_sort(arr)
        elif selected_algorithm == "Knuth-Morris-Pratt":
            pattern, text = input_data.split(';')
            result = kmp_search(pattern, text)
        elif selected_algorithm == "Rabin-Karp":
            pattern, text = input_data.split(';')
            result = rabin_karp(pattern, text)
        elif selected_algorithm == "Longest Common Substring":
            seq1, seq2 = input_data.split(';')
            result = lcs(seq1, seq2)

        output_var.set(f"Result: {result}")
        analyze_complexity(selected_algorithm.lower().replace(" ", "_"), len(arr) if selected_algorithm in ["Merge Sort", "Quick Sort", "Binary Search"] else n)

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid input based on the selected algorithm!")

# Algorithm Category Selection
def on_category_select(event):
    selected_category = category_dropdown.get()
    algo_dropdown['values'] = algorithm_categories[selected_category]
    algo_dropdown.set("")  # Clear the algorithm dropdown
    output_var.set(f"Selected Category: {selected_category}")
    clear_entry()  # Clear previous input and output when category changes
    help_label.config(text="")  # Clear help text

# Algorithm Selection
def on_algorithm_select(event):
    global selected_algorithm
    selected_algorithm = algo_dropdown.get()
    output_var.set(f"Selected Algorithm: {selected_algorithm}")
    entry_var.set("")  # Clear input field
    help_label.config(text=help_instructions.get(selected_algorithm, "No help available."))  # Update help text
    update_input_ui()  # Update input UI based on selected algorithm

# Update Input UI Dynamically
def update_input_ui():
    if selected_algorithm in ["Merge Sort", "Quick Sort", "Randomized Quick Sort", "Binary Search"]:
        entry_label.config(text="Enter numbers separated by spaces:")
        entry_var.set("")
    elif selected_algorithm in ["Fibonacci Sequence", "N-Queens Problem"]:
        entry_label.config(text="Enter a single integer:")
        entry_var.set("")
    elif selected_algorithm == "Knapsack Problem":
        entry_label.config(text="Enter weight,value pairs separated by spaces (e.g., '2,3 3,4'):")
        entry_var.set("")
    elif selected_algorithm in ["Longest Common Subsequence", "Knuth-Morris-Pratt", "Rabin-Karp", "Longest Common Substring"]:
        entry_label.config(text="Enter two sequences separated by a semicolon (e.g., 'ABC;AC'):")
        entry_var.set("")
    elif selected_algorithm in ["Matrix Chain Multiplication", "Coin Change Problem", "Traveling Salesman Problem"]:
        entry_label.config(text="Enter comma-separated values or matrix rows separated by semicolons:")
        entry_var.set("")
    elif selected_algorithm in ["Prim's Algorithm", "Kruskal's Algorithm", "Dijkstra's Algorithm"]:
        entry_label.config(text="Enter edges as 'u,v,w' separated by semicolons (e.g., '0,1,2;1,2,3'):")
        entry_var.set("")
    elif selected_algorithm == "Huffman Coding":
        entry_label.config(text="Enter frequencies as a dictionary (e.g., '{'A': 5, 'B': 9}'):")
        entry_var.set("")
    elif selected_algorithm == "Sudoku Solver":
        entry_label.config(text="Enter Sudoku board rows separated by semicolons (e.g., '5 3 0;6 0 0;0 9 8'):")
        entry_var.set("")
    else:
        entry_label.config(text="Enter input:")


# Button Click Handler
def on_button_click(value):
    entry_var.set(entry_var.get() + str(value) + " ")
# Clear Input
def clear_entry():
    entry_var.set("")
    output_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Algorithm Calculator")
root.geometry("420x600")
root.configure(bg="#f0f0f0")

entry_var = tk.StringVar()
output_var = tk.StringVar()

# Header
header_label = tk.Label(root, text="Algorithm Calculator", font=("Arial", 18, "bold"), bg="#4A90E2", fg="white", padx=10, pady=5)
header_label.pack(fill="x")

# Algorithm Category Selection
category_frame = tk.Frame(root, bg="#f0f0f0")
category_frame.pack(pady=10)

tk.Label(category_frame, text="Select Category:", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=5)
category_dropdown = ttk.Combobox(category_frame, values=list(algorithm_categories.keys()), state="readonly", width=20, font=("Arial", 12))
category_dropdown.pack(side="left", padx=5)
category_dropdown.bind("<<ComboboxSelected>>", on_category_select)

# Algorithm Selection
algo_frame = tk.Frame(root, bg="#f0f0f0")
algo_frame.pack(pady=10)

tk.Label(algo_frame, text="Select Algorithm:", font=("Arial", 14), bg="#f0f0f0").pack(side="left", padx=5)
algo_dropdown = ttk.Combobox(algo_frame, state="readonly", width=20, font=("Arial", 12))
algo_dropdown.pack(side="left", padx=5)
algo_dropdown.bind("<<ComboboxSelected>>", on_algorithm_select)

# Input Field
entry_label = tk.Label(root, text="Enter input:", font=("Arial", 12), bg="#f0f0f0")
entry_label.pack(pady=5)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 16), width=25, bd=2, relief="solid")
entry.pack(pady=5)

# Output Display
output_label = tk.Label(root, textvariable=output_var, font=("Arial", 14, "bold"), fg="blue", bg="#f0f0f0")
output_label.pack(pady=5)

# Button Grid
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

buttons = [str(i) for i in range(1, 10)] + ["0", "Clear", "Run"]
row, col = 0, 0

for btn in buttons:
    action = lambda x=btn: on_button_click(x) if x not in ["Clear", "Run"] else clear_entry() if x == "Clear" else execute_algorithm()
    color = "#e0e0e0" if btn.isdigit() else "#FF4C4C" if btn == "Clear" else "#4CAF50"
    tk.Button(button_frame, text=btn, width =7, height=2, font=("Arial", 14), command=action, bg=color, fg="white").grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Help Section
help_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0", fg="gray", justify="left")
help_label.pack(pady=10)

root.mainloop()
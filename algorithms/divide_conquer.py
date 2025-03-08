def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


def quick_sort(arr):
    """Sorts an array using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choosing the middle element as pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        return quick_sort(left) + middle + quick_sort(right)


def binary_search(arr, target):
    """Performs binary search on a sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found


def strassen_matrix_multiplication(A, B):
    """Multiplies two matrices using Strassen's algorithm."""
    def add_matrices(A, B):
        return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def subtract_matrices(A, B):
        return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    def split_matrix(M):
        mid = len(M) // 2
        return ( [row[:mid] for row in M[:mid]], [row[mid:] for row in M[:mid]],
                  [row[:mid] for row in M[mid:]], [row[mid:] for row in M[mid:]] )

    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen_matrix_multiplication(add_matrices(A11, A22), add_matrices(B11, B22))
    M2 = strassen_matrix_multiplication(add_matrices(A21, A22), B11)
    M3 = strassen_matrix_multiplication(A11, subtract_matrices(B12, B22))
    M4 = strassen_matrix_multiplication(A22, subtract_matrices(B21, B11))
    M5 = strassen_matrix_multiplication(add_matrices(A11, A12), B22)
    M6 = strassen_matrix_multiplication(subtract_matrices(A21, A11), add_matrices(B11, B12))
    M7 = strassen_matrix_multiplication(subtract_matrices(A12, A22), add_matrices(B21, B22))

    C11 = add_matrices(subtract_matrices(add_matrices(M1, M4), M5), M7)
    C12 = add_matrices(M3, M5)
    C21 = add_matrices(M2, M4)
    C22 = add_matrices(subtract_matrices(add_matrices(M1 , M3), M2), M6)

    # Combine the four quadrants into a single matrix
    new_matrix = []
    for i in range(len(C11)):
        new_matrix.append(C11[i] + C12[i])
    for i in range(len(C21)):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix
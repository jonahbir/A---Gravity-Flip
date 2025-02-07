def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half
    
    return merge(left_half, right_half)  # Merge sorted halves

def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):  # Merge two halves
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])  # Add remaining elements from left
    sorted_list.extend(right[j:])  # Add remaining elements from right
    return sorted_list

# Read input
n = int(input())  # Number of columns
cubes = list(map(int, input().split()))  # Read cube counts

# Sort using Merge Sort
sorted_cubes = merge_sort(cubes)

# Print the result
print(*sorted_cubes)

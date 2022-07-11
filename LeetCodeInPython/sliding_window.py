"""
    Sliding window is an optimization approach
    Problem Statement
        Given an array of integers of size N, find maximum sum of K consecutive elements
"""
def max_sum(arr, window_size):
    """Returns the max sum of given k consecutive numbers"""
    array_size = len(arr)
    if array_size <= window_size:
        print(f"Invalid Opertion. windo size {window_size} must be less than array size")
        return -1

    window_sum = sum([arr[index] for index in range(k)])
    max_sum = window_sum

    for i in range(array_size-window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(window_sum, max_sum)
    return max_sum


arr = [80, -50, 90, 100, 120]
k = 2
answer = max_sum(arr, k)
print(answer)
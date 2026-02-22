#Max sum of subarray of size k

def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sum([2,4,6,1,3], 3))
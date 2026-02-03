arr = [1,12,-5,-6,50,3]
k = 4

window_sum = sum(arr[:k])
max_avg = window_sum / k

for i in range(k, len(arr)):
    window_sum += arr[i]       # add new element
    window_sum -= arr[i-k]     # remove old element

    curr_avg = window_sum / k
    max_avg = max(max_avg, curr_avg)

print(max_avg)




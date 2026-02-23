'''Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15

Input: nums = [4,4,4], k = 3
Output: 0'''

nums = [1,5,4,2,9,9,9]
k = 3

seen = set()
window_sum = 0
max_sum = 0
left = 0

for right in range(len(nums)):

    # duplicate aaye to window shrink
    while nums[right] in seen:
        seen.remove(nums[left])
        window_sum -= nums[left]
        left += 1

    # new element add
    seen.add(nums[right])
    window_sum += nums[right]

    # window size k ho gayi
    if right - left + 1 == k:
        max_sum = max(max_sum, window_sum)

        # window slide
        seen.remove(nums[left])
        window_sum -= nums[left]
        left += 1

print(max_sum)
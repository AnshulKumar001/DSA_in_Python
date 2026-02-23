'''Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15

Input: nums = [4,4,4], k = 3
Output: 0'''

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen = set()
        win_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            
            # agar duplicate aaye to window shrink karo
            while nums[right] in seen:
                seen.remove(nums[left])
                win_sum -= nums[left]
                left += 1

            # add new element
            seen.add(nums[right])
            win_sum += nums[right]

            # window size k ho jaye
            if right - left + 1 == k:
                max_sum = max(max_sum, win_sum)

                # slide window forward
                seen.remove(nums[left])
                win_sum -= nums[left]
                left += 1

        return max_sum
   
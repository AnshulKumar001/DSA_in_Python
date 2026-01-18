#(1480) Running Sum of 1d Array

'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]'''

def runningSum(nums):
    n=len(nums)
    ans=[]
    ans.append(nums[0])
    for i in range (1,n):
        x=ans[i-1]+nums[i]
        ans.append(x)
    return ans
print(runningSum([1,2,3,4]))      #output: [1,3,6,10]    
       
 
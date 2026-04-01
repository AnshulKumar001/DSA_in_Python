class Solution:
    def merge(self, nums1,nums2,n,m):
        #nums1[m:]=nums2[:n]
        #nums1.sort()
        p1=n-1
        p2=m-1
        p=n+m-1
sol=Solution()
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
sol.merge(nums1,nums2,3,3)
print(nums1)





        
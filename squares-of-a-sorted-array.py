'''
https://leetcode.com/problems/squares-of-a-sorted-array/
'''

# 2/2/23
# time: 289s, 38.61%
# space: 16.2mb, 43.95%
# O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        i = len(nums)-1
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[r]**2 > nums[l]**2:
                ans[i] = nums[r]**2
                r -= 1
            else:
                ans[i] = nums[l]**2
                l += 1
            i -= 1

        return ans
        

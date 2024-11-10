# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        res = 0
        count = 0

        while r < len(nums):
            if nums[r] == 0:
                count += 1
            
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1 

        return res

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0
        
        total = 0
        res = float('inf')
        
        while r < len(nums):
            num = nums[r]
            total += num
            r += 1
            
            while total >= target:
                res = min(res, r - l)
                out = nums[l]
                total -= out
                l += 1
                
        if res == float('inf'):
            return 0 
        else:
            return res
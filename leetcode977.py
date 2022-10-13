class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        
        res = []
        l = 0 
        r = len(nums) - 1
        while l <= r :
            if nums[l] ** 2 < nums[r] ** 2:
                res.append(nums[r] ** 2)
                r -= 1
            else:
                res.append(nums[l] ** 2)
                l += 1
                
        return res[::-1]
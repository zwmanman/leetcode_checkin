# 27. Remove Element


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        #1221
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
            
        return l
                
            

# 704 Binary search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        l = 0
        r = len(nums) - 1
        
        while l + 1 < r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid
            else:
                r = mid
                
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
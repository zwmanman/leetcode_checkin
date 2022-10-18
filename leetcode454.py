class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hashmap = {}
        for n1 in nums1:
            for n2 in nums2:
                key = n1 + n2
                if key in hashmap:
                    hashmap[key] += 1
                else:
                    hashmap[key] = 1
                
        count = 0
        
        for n3 in nums3:
            for n4 in nums4:
                key = -n3 - n4
                if key in hashmap:
                    count += hashmap[key]
                    
        return count
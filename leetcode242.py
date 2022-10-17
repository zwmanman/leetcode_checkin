class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s or not t:
            return False
        
        mapS = collections.Counter(s)
        
        for word in t:
            if word not in mapS:
                return False
            mapS[word] -= 1
            
            if mapS[word] == 0:
                del mapS[word]
                
        return len(mapS) == 0
            
        
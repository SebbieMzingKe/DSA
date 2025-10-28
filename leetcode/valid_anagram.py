class Solution(object):
    def isAnagra(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        map_s = {}
        map_t = {}

        for i in s:
            map_s[i] = map_s.get(i, 0) + 1
        for i in t:
            map_t[i] = map_t.get(i, 0) + 1
        
        for key in map_s:
            if map_s[key] != map_t.get(key, 0):
                return False
        return True
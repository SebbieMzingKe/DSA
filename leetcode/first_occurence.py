class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for i in range(len(haystack) +1 - len(needle)):
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
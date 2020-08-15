# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
#
# Example 2:
#
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
#
#  
# Constraints:
#
#
# 	haystack and needle consist only of lowercase English characters.
#
#


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 双指针 暴力匹配 在某些情况下表现的很蠢,比如 haystack = aaabaaac needle = aaac
        # lh = len(haystack)
        # ln = len(needle)
        # for i in range(lh-ln+1):
        #     match = 0
        #     for j in range(ln):
        #         if needle[j] == haystack[i+j]:
        #             match += 1
        #         else:
        #             break
        #     if match == ln:
        #         return i
        # return -1

        # kmp 算法
        return self.kmp(haystack, needle)

    def kmp(self, text, p):
        """
        kmp 算法
        j处匹配不上时,p串跳转到[0~j-1]的最长前后缀公共子串长度
        """
        i, j = 0, 0
        lenText = len(text)
        lenP = len(p)
        np = self.getNext(p)

        while i < lenText and j < lenP:
            if text[i] == p[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = np[j-1]
        
        if j == lenP:
            return i - j
        else:
            return -1

    def getNext(self, p):
        """
        不使用一些文章中提到的next数组, 
        使用pmt数组更容易让人理解,
        用法也与next数组基本相同
        """
        lenP = len(p)
        np = [0]*lenP
        i, j = 1, 0

        while i < lenP:
            if p[i] == p[j]:
                j += 1
                np[i] = j
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = np[j-1]
        return np


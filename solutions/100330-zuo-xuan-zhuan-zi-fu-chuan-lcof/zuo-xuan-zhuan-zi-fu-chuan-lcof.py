# English description is not available for the problem. Please switch to Chinese.
#


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

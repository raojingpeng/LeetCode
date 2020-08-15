# English description is not available for the problem. Please switch to Chinese.
#


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 约瑟夫问题
        i, a = 0, list(range(n))
        while len(a)>1:
            i = (i+m-1)%len(a)
            del a[i]
        return a[0]

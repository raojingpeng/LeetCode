# English description is not available for the problem. Please switch to Chinese.
#


class Solution:
    def __init__(self):
        self.total = 0

    def sumNums(self, n: int) -> int:
        # 方法1 
        # n > 1 and self.sumNums(n-1)
        # self.total += n
        # return self.total

        # 方法二 妙啊！
        return n and n + self.sumNums(n-1)

# 暂无


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum([math.ceil(i/2) for i in coins])

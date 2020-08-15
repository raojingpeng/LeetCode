# English description is not available for the problem. Please switch to Chinese.
#


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 暴力法
        # result = []
        # for i in range(1, target//2+1):
        #     total = i
        #     for j in range(i+1, target//2+2):
        #         if total + j < target:
        #             total += j
        #             j += 1
        #         else:
        #             if total + j == target:
        #                 result.append([e for e in range(i, j+1)])
        #             break
        # return result
        
        # 滑动窗口
        # i, j, sum_, result = 1, 1, 0, []
        # while i <= target//2:
        #     if sum_ < target:
        #         sum_ += j
        #         j += 1
        #     elif sum_ > target:
        #         sum_ -= i
        #         i += 1
        #     else:
        #         result.append(list(range(i, j)))
        #         sum_ -= i
        #         i += 1
        # return result

        # 等差数列 + 求根
        result = []
        y = 2
        while y <= target//2+1:
            x = (1/4+y**2+y-2*target)**(1/2)+0.5
            if type(x) != complex and x == int(x):
                result.append(list(range(int(x), y+1)))
            y += 1
        return result

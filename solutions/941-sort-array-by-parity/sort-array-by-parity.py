# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#  
#
#
# Example 1:
#
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
#
#
#  
#
# Note:
#
#
# 	1 <= A.length <= 5000
# 	0 <= A[i] <= 5000
#
#
#


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # 1 逻辑思路 O(n) O(n)
        # ans = []
        # for i in A:
        #     if i % 2 == 0:
        #         ans.insert(0, i)
        #     else:
        #         ans.append(i)
        # return ans

        # 2 自带排序 O(nlogn) O(n)
        # A.sort(key=lambda x: x % 2)
        # return A

        # 3 双指针 原地排序 O(n) O(1)
        # i = 0
        # j = len(A)-1
        # while i < j:
        #     # 我的写法
        #     if A[i] % 2 == 1 and A[j] % 2 == 0:
        #         A[i], A[j] = A[j], A[i]
        #         i += 1
        #         j -= 1
        #     elif A[i] % 2 == 1:
        #         j -= 1
        #     else:
        #         i += 1
            
        #     # 官方答案写法
        #     if A[i] % 2 > A[j] % 2:
        #         A[i], A[j] = A[j], A[i]
        #     if A[i] % 2 == 0:
        #         i += 1
        #     if A[j] % 2 == 1:
        #         j -= 1
        # return A

        # 4 扫描两次 O(n)省略常数 O(n)
        return [x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1]

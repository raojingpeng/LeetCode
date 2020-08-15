# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
#
# Initially the number of elements in A and B are m and n respectively.
#
# Example:
#
#
# Input:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        # 快排
        def quick_search(array):
            if len(array) < 2:
                return array
            provice = array[0]
            left, right = [], []

            for i in array[1:]:
                if i < provice:
                    left.append(i)
                else:
                    right.append(i)
            return quick_search(left) + [provice] + quick_search(right)
        
        A[:] = quick_search(A[:m]+B)
        # 自带排序
        # A[m:] = B
        # A.sort()
        
        # 双指针
        # result = []
        # pa , pb = 0, 0
        # while pa < m and pb < n:
        #     if A[pa] <= B[pb]:
        #         result.append(A[pa])
        #         pa += 1
        #     if A[pa] > B[pb]:
        #         result.append(B[pb])
        #         pb += 1
        
        # if pa == m:
        #     result += B[pb:n]
        # if pb == n:
        #     result += A[pa:m]
        # A[:] = result






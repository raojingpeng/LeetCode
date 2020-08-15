# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
#
# Return the number of negative numbers in grid.
#
#  
# Example 1:
#
#
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
#
#
# Example 2:
#
#
# Input: grid = [[3,2],[1,0]]
# Output: 0
#
#
# Example 3:
#
#
# Input: grid = [[1,-1],[-1,-1]]
# Output: 3
#
#
# Example 4:
#
#
# Input: grid = [[-1]]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	m == grid.length
# 	n == grid[i].length
# 	1 <= m, n <= 100
# 	-100 <= grid[i][j] <= 100
#


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # 暴力法 时间复杂度 O(n)
        # ans = 0
        # for i in grid:
        #     for j in i:
        #         if j < 0:
        #             ans += 1
        # return ans

        # 二分法
        # ans = 0
        # n = len(grid[0])
        # for i in grid:
        #     l = 0
        #     r = n - 1
        #     pos = -1
        #     while l <= r:
        #         mid = (l+r)//2
        #         if i[mid] >= 0:
        #             l = mid + 1
        #             pos = mid
        #         else:
        #             r = mid - 1
        #     ans += n-1-pos if pos != -1 else n
        # return ans

        # 下楼梯
        ans = 0
        i = 0
        j = len(grid[0])-1
        while i < len(grid) and j >= 0:
            if grid[i][j] >= 0:
                i += 1
            else:
                ans += len(grid) - i
                j -= 1
        return ans





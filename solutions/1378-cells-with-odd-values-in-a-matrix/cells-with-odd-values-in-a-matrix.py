# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
#
# Return the number of cells with odd values in the matrix after applying the increment to all indices.
#
#  
# Example 1:
#
#
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
#
#
# Example 2:
#
#
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 50
# 	1 <= m <= 50
# 	1 <= indices.length <= 100
# 	0 <= indices[i][0] < n
# 	0 <= indices[i][1] < m
#
#


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # 模拟 暴力法
        # matrix = [[0 for j in range(m)] for i in range(n)]
        # for x, y in indices:
        #     for i in range(m):
        #         matrix[x][i] += 1
        #     for j in range(n):
        #         matrix[j][y] += 1
        # return sum([j%2==1 for i in matrix for j in i])

        # 记录行列增加的次数， 最后汇总（妙啊！）
        # row = [0]*n
        # col = [0]*m
        # for x, y in indices:
        #     row[x] += 1
        #     col[y] += 1
        # return sum(((i+j)%2 == 1 for i in row for j in col))

        # 在方法二的基础上再次优化， 依据是奇+奇=偶， 奇+偶=奇， 偶+偶=偶
        row = [0]*n
        col = [0]*m
        for x, y in indices:
            row[x] += 1
            col[y] += 1
        odd_row = sum((i%2==1 for i in row))
        odd_col = sum((i%2==1 for i in col))
        return odd_row*(m-odd_col)+odd_col*(n-odd_row)

 

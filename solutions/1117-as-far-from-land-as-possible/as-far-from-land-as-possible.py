# Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
# If no land or water exists in the grid, return -1.
#
#  
#
# Example 1:
#
#
#
#
# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
#
#
# Example 2:
#
#
#
#
# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
#
#
#  
#
# Note:
#
#
# 	1 <= grid.length == grid[0].length <= 100
# 	grid[i][j] is 0 or 1
#
#


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # 广度优先搜索 Breadth-First Search
        from collections import deque
        l = len(grid)
        d = deque([[i, j] for i in range(l) for j in range(l) if grid[i][j]==1])  # 将所有陆地放入队列
        step = -1  # while 循环时会多走 1 步, 所以 step 从 -1 开始
        if len(d) == 0 or len(d) == l**2:  # 如果队列长度为 0 (没有陆地), 或长度与 grid 相同(没有海洋), 直接返回 -1
            return step

        while len(d) > 0:  # 判断此时队列长度
            for _ in range(len(d)):  # 循环完毕后, 队列的元素都被弹出了
                x, y = d.popleft()
                for x1, y1 in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    # 判断坐标是否在取值范围内, 是否为海洋
                    if x1 >= 0 and x1 < l and y1 >= 0 and y1 < l and grid[x1][y1] == 0:
                        d.append([x1, y1])
                        grid[x1][y1] = 1  # 将坐标对应值修改为陆地(一定不要忘记加上,否则会无限循环)
            step += 1

        return step

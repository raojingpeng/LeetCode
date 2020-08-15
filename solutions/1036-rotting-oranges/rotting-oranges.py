# In a given grid, each cell can have one of three values:
#
#
# 	the value 0 representing an empty cell;
# 	the value 1 representing a fresh orange;
# 	the value 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
#  
#
#
# Example 1:
#
#
#
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
#
# Example 2:
#
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
#
#
# Example 3:
#
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
#
#  
#
# Note:
#
#
# 	1 <= grid.length <= 10
# 	1 <= grid[0].length <= 10
# 	grid[i][j] is only 0, 1, or 2.
#
#
#
#
#


from collections import deque
class Solution:
    def orangesRotting(self, grid):
        L = len(grid)
        W = len(grid[0])
        chan = deque()

        for x, row in enumerate(grid):
            for y, val in enumerate(row):
                if val == 2:
                    chan.append((x, y, 0))

        def neighbor(x, y):
            for nx, ny in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
                if 0 <= nx < L and 0 <= ny < W:
                    yield nx, ny

        minute = 0
        while chan:
            x, y, c = chan.popleft()
            for nx, ny in neighbor(x, y):
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    chan.append((nx, ny, c+1))

            if minute < c:
                minute = c

        if any(1 in row for row in grid):
            return -1
        return minute

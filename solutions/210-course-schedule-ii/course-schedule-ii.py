# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.
#
# Example 1:
#
#
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
#              course 0. So the correct course order is [0,1] .
#
# Example 2:
#
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
#
# Note:
#
#
# 	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# 	You may assume that there are no duplicate edges in the input prerequisites.
#
#


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 拓扑排序 DFS
        # adjacency = [[] for _ in range(numCourses)]
        # handle = [0] * numCourses
        # res = []

        # for pre, cur in prerequisites: 
        #     adjacency[cur].append(pre)
        
        # def dfs(i):
        #     if handle[i] == 1: return False
        #     elif handle[i] == -1: return True
        #     handle[i] = 1
        #     for item in adjacency[i]:
        #         if not dfs(item): return False
        #     handle[i] = -1
        #     res.append(i)
        #     return True

        # for i in range(numCourses):
        #     if not dfs(i):
        #         return []
        # return res[::-1]

        # BFS
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        res = []

        for pre, cur in prerequisites:
            indegrees[pre] += 1
            adjacency[cur].append(pre)

        queue = [i for i in range(numCourses) if indegrees[i] == 0]
        while queue:
            pre = queue.pop(0)
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0: queue.append(cur)
            res.append(pre)

        return res if len(res) == numCourses else []


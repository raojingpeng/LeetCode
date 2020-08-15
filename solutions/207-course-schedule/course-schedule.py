# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#  
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#
#
#  
# Constraints:
#
#
# 	The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# 	You may assume that there are no duplicate edges in the input prerequisites.
# 	1 <= numCourses <= 10^5
#
#


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """拓扑排序"""
        # bfs
        # indegrees = [0] * numCourses  # 入度表
        # adjacency = [[] for _ in range(numCourses)]  # 邻接表

        # for cur, pre in prerequisites:
        #     indegrees[cur] += 1
        #     adjacency[pre].append(cur)
        
        # queue = [i for i in range(len(indegrees)) if indegrees[i] == 0]
        # while queue:
        #     pre = queue.pop(0)
        #     numCourses -= 1
        #     for cur in adjacency[pre]:
        #         indegrees[cur] -= 1
        #         if indegrees[cur] == 0: queue.append(cur)

        # return numCourses == 0

        # dfs
        handle = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)

        def dfs(i):
            """
            当 flag[i] == -1，说明当前访问节点已被其他节点启动的 DFS 访问，无需再重复搜索，
            直接返回 True。
            当 flag[i] == 1，说明在本轮 DFS 搜索中节点 i 被第 2 次访问，即 课程安排图有环 ，
            直接返回 False
            """
            if handle[i] == 1: return False
            if handle[i] == -1: return True
            handle[i] = 1
            for j in adjacency[i]:
                if not dfs(j): return False
            handle[i] = -1
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

        

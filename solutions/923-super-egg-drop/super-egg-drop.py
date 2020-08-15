# You are given K eggs, and you have access to a building with N floors from 1 to N. 
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?
#
#  
#
#
#
#
#
# Example 1:
#
#
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
#
#
#
# Example 2:
#
#
# Input: K = 2, N = 6
# Output: 3
#
#
#
# Example 3:
#
#
# Input: K = 3, N = 14
# Output: 4
#
#
#  
#
# Note:
#
#
# 	1 <= K <= 100
# 	1 <= N <= 10000
#
#
#
#
#


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dynamic programming + 二分法
        # dp(K, N) = min(max(dp(K-1, X-1), dp(K, N-X)))
        mem = {}

        def dp(K, N):
            if (K, N) not in mem:
                if K == 0:
                    return 0
                if K == 1:
                    return N
                if N == 0:
                    return 0

                lo, hi = 1, N
                while lo+1 < hi:  # lo, hi 这两点是最接近中间点的, 两者距离为1
                    mid = (lo + hi) // 2
                    v1 = dp(K - 1, mid - 1)
                    v2 = dp(K, N - mid)
                    if v1 < v2:
                        lo = mid
                    elif v1 > v2:
                        hi = mid
                    else:
                        lo = hi = mid
                mem[K, N] = min(max(dp(K - 1, x - 1), dp(K, N - x)) for x in [lo, hi]) + 1

            ans = mem[K, N]
            return ans

        return dp(K, N)
            

# Alice and Bob take turns playing a game, with Alice starting first.
#
# Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
#
#
# 	Choosing any x with 0 < x < N and N % x == 0.
# 	Replacing the number N on the chalkboard with N - x.
#
#
# Also, if a player cannot make a move, they lose the game.
#
# Return True if and only if Alice wins the game, assuming both players play optimally.
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
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#
#
#
# Example 2:
#
#
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#
#
#  
#
# Note:
#
#
# 	1 <= N <= 1000
#
#
#


class Solution:
    def divisorGame(self, N: int) -> bool:
        # 归纳法
        # 拿到2 赢 拿到1 输
        # 奇数的约数只能是奇数或者 1，因此下一个(奇数减约数)一定是偶数
        # 偶数减1一定是奇数
        # 因此 奇数赢 偶数输
        # return N % 2 == 0
        
        # 动态规划
        if N < 2:
            return False
        
        target= [0 for i in range(N+1)]
        target[2] = 1
        for i in range(3, N+1):
            for j in range(1, i//2):
                if i % j == 0 and target[i-j] == 0:
                    target[i] = 1
                    break
        return target[N] == 1

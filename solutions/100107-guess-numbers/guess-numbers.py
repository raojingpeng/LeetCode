# English description is not available for the problem. Please switch to Chinese.
#  


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return sum([guess[i]==answer[i] for i in range(len(guess))])

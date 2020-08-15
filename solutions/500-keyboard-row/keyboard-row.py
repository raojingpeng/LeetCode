# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
#  
#
#
#  
#
# Example:
#
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#  
#
# Note:
#
#
# 	You may use one character in the keyboard more than once.
# 	You may assume the input string will only contain letters of alphabet.
#
#


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        mapping1 = set('qwertyuiop')
        mapping2 = set('asdfghjkl')
        mapping3 = set('zxcvbnm')
        ans = []

        for word in words:
            w = set(word.lower())
            if w.issubset(mapping1) or w.issubset(mapping2) or w.issubset(mapping3):
                ans.append(word)
        return ans     

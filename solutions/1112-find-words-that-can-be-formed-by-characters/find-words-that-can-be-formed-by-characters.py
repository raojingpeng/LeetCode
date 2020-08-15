# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#  
#
# Example 1:
#
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
#
#
# Example 2:
#
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
#
#
#  
#
# Note:
#
#
# 	1 <= words.length <= 1000
# 	1 <= words[i].length, chars.length <= 100
# 	All strings contain lowercase English letters only.
#


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # 自己想的
        # ans = 0
        # mapping = {}
        # for c in chars:
        #     mapping[c] = mapping.get(c, 0) + 1

        # for w in words:
        #     w_mapping = {}
        #     for i in w:
        #         w_mapping[i] = w_mapping.get(i, 0) + 1
        #     if all(w_mapping[i] <= mapping.get(i, 0) for i in w_mapping):
        #         ans += len(w)
        # return ans

        # 官方解答复刻版 跟我的思路差不多 for else 这个还是学到了
        ans = 0
        chars_cnt = collections.Counter(chars)
        for w in words:
            w_cnt = collections.Counter(w)
            for key in w_cnt:
                if w_cnt[key] > chars_cnt[key]:
                    break
            else:
                ans += len(w)
        return ans


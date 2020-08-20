# Write a function to swap a number in place (that is, without temporary vari­ ables).
#
# Example: 
#
#
# Input: numbers = [1,2]
# Output: [2,1]
#
#
# Note: 
#
#
# 	numbers.length == 2
#
#


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        # python 语法糖
        # numbers[0], numbers[1] = numbers[1], numbers[0]
        # return numbers

        # 异或运算满足交换律 结合律 a^b=a+b a^b^b = a 0^a=a a^a=0
        # numbers[0] ^= numbers[1] # numbers[0] = numbers[0] + numbers[1]
        # numbers[1] ^= numbers[0] # numbers[1] = numbers[0] + numbers[1] + numbers[1] = numbers[0]
        # numbers[0] ^= numbers[1] # numbers[0] = numbers[0] + numbers[0] + numbers[1] = numbers[1]
        # return numbers

        # 加减法 其他语言可能存在溢出问题
        numbers[0] = numbers[0] + numbers[1]
        numbers[1] = numbers[0] - numbers[1]
        numbers[0] = numbers[0] - numbers[1]
        return numbers

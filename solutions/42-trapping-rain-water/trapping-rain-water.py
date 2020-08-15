# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution:
    def trap(self, height: List[int]) -> int:
        # 按列求 时间复杂度 O(n的平方)
        # _sum = 0

        # for i in range(1, len(height)-1):
        #     max_left = 0
        #     for j in range(0, i):
        #         if height[j] > max_left:
        #             max_left = height[j]

        #     max_right = 0
        #     for j in range(i+1, len(height)):
        #         if height[j] > max_right:
        #             max_right = height[j]
            
        #     min_value = min(max_left, max_right)
        #     if height[i] < min_value:
        #         _sum += min_value - height[i]

        # return _sum

        # 动态规划 + 双指针
        """
        对于位置left而言，它左边最大值一定是left_max，右边最大值“大于等于”right_max，这时候，如果left_max<right_max成立，         那么它就知道自己能存多少水了。无论右边将来会不会出现更大的right_max，都不影响这个结果。 所以当left_max<right_max时，        我们就希望去处理left下标，反之，我们希望去处理right下标。
        信任!
        """
        # max_left = max_right = _sum = 0
        # left = 1
        # right = len(height) - 2
        # while left <= right:
        #     max_left = max(max_left, height[left-1])
        #     max_right = max(max_right, height[right+1])
        #     if max_left < max_right:
        #         if height[left] < max_left:
        #             _sum += max_left-height[left]
        #         else:
        #             max_left = height[left]
        #         left += 1
            
        #     else:
        #         if height[right] < max_right:
        #             _sum += max_right-height[right]
        #         else:
        #             max_right = height[right]
        #         right -= 1
        # return _sum

        # 栈
        cur = 0
        _sum = 0
        stack = []
        while cur < len(height):
            while stack and height[cur] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                # 想了半天才明白为什么要有这个距离
                # 可以理解成 算完top接的水后 top的高度等同于stack[-1]的高度(相当于补齐了)
                # pop出新的元素后 原来top少算的 通过乘以距离补齐
                distance = cur - stack[-1] - 1
                _sum += (min(height[cur], height[stack[-1]])-height[top])*distance
            stack.append(cur)
            cur += 1
        return _sum


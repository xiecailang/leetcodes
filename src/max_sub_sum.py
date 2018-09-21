'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = ending = nums[0]
        for x in nums[1:]:
            ending = max(x, ending + x)
            ans = max(ending, ans)
        return ans
nums = [int(i) for i in input().split()]
so = Solution()
print(so.maxSubArray(nums))
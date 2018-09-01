class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2:
            return 0
        if len(height) == 2:
            return min(height[0], height[1])
        max_area = 0
        p_start = 0
        p_end = len(height) - 1

        while p_start < p_end:         
            area = (p_end - p_start) * min(height[p_end], height[p_start])
            max_area = max(max_area, area)

            if height[p_start] < height[p_end]:
                p_start += 1
            else:
                p_end -= 1
        return max_area
           

solution = Solution()
print(solution.maxArea([2,3,4,5,18,17,6]))
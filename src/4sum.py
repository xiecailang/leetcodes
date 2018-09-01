class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 4 and sum(nums) == target:
            return [nums]
        nums.sort()
        two_sum = {}       
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                if temp not in two_sum:
                    two_sum[temp] = [[i, j]]
                else:  
                    two_sum[temp].append([i, j])
                        
        ans = []
        #pre_ans = []
        for key in two_sum.keys():
            s_target = target - key
            #if s_target == key:
                #continue
            if s_target in two_sum:
                for i in two_sum[key]:
                    for j in two_sum[s_target]: 
                        #有相同元素
                        if i[0] == j[0] or i[1] == j[0] or i[0] == j[1] or i[1] == j[1]:
                           continue                     
                        sub_ans = [nums[i[0]], nums[i[1]], nums[j[0]], nums[j[1]]]
                        sub_ans.sort()
                        if sub_ans not in ans:
                            ans.append(sub_ans)
                        
        return ans
                

nums = [int(i) for i in input().split()]
target = int(input())       
solution = Solution()
print(solution.fourSum(nums, target))

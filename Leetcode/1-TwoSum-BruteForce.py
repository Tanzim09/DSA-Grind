# Problem Link : https://leetcode.com/problems/two-sum/description/
# Time Complexity: O(n^2)
# Remark: Accepted. 


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums),1):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
          
            


solution = Solution()
test_case1 = [2,7,11,15]
target1 = 9
print(solution.twoSum(test_case1,target1)) # [0,1]
test_case2 = [3,2,4]
target2 = 6
print(solution.twoSum(test_case2,target2)) # [1,2]           
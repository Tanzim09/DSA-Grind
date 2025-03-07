# Problem Link : https://leetcode.com/problems/missing-number/description/
# Time Complexity: O(n^2)
# Remark: Did not sumbit. 


class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            flag = False
            for j in range(len(nums)):
                if i == nums[j]:
                    flag = True
                    break;
            if not flag:
                return i
            

solution = Solution()
test_case1 = [3,0,1]
print(solution.missingNumber(test_case1)) # 2
test_case2 = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(test_case2)) # 8
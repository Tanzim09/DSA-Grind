# Problem Link : https://leetcode.com/problems/missing-number/description/
# Time Complexity: O(n) --> O(1) + O(n) = O(n)
# Remark: Was accepted. 


class Solution(object):
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

            

solution = Solution()
test_case1 = [3,0,1]
print(solution.missingNumber(test_case1)) # 2
test_case2 = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(test_case2)) # 8
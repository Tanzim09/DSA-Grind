# Problem Link : https://leetcode.com/problems/contains-duplicate/
# Time Complexity: O(n)
# Remark: Accepted


class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) == len(nums):
            return False
        else:
            return True



solution = Solution()
test_case1 = [1, 2, 3, 4, 8]
print(solution.containsDuplicate(test_case1)) # False
test_case2 = [1, 2, 3, 4, 2]
print(solution.containsDuplicate(test_case2)) # True
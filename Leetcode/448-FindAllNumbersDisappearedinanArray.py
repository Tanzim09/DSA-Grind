# Problem Link : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Time Complexity: O(n)
# Remark: Accepted. 

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set = set(nums)
        output = []
        for i in range(1,(len(nums)+1)): # 2 --> 1..2
            if i not in num_set: # Lookup using set is O(1) as it uses hash tables
                output.append(i)
        
        return output
            
solution = Solution()
test_case1 = [4,3,2,7,8,2,3,1]
print(solution.findDisappearedNumbers(test_case1)) # [5,6]
test_case2 = [1,1]
print(solution.findDisappearedNumbers(test_case2)) # [2]
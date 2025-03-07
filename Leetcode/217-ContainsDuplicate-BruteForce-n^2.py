class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
                else :
                    continue
        
        return False


solution = Solution()
test_case1 = [1, 2, 3, 4, 8]
print(solution.containsDuplicate(test_case1)) # False
test_case2 = [1, 2, 3, 4, 2]
print(solution.containsDuplicate(test_case2)) # True
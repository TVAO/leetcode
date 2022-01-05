
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# We can reduce lookup time from O(n) to O(1) by using hash table with O(n) space, giving O(n) time

from typing import List

class Solution:
    # O(n^2) time and O(1) space as space does not depend on size of input 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
    # O(n) time and space 
    def twoSumFast(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

assert(Solution().twoSum(nums = [2, 7, 11, 15], target = 9) == [0, 1])
assert(Solution().twoSum(nums = [3, 2, 4], target = 6) == [1, 2])
assert(Solution().twoSum(nums = [3, 3], target = 6) == [0, 1])
print("All tests passed")
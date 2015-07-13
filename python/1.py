# Given an array of integers, find two numsbers such that they add up to a specific target numsber.
# The function twoSum should return indices of the two numsbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numsbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
  # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
      d = dict()
      d[nums[0]] = 0
      for i in range(1, len(nums)):
        aim = target - nums[i]
        if aim in d:
          return [d[aim]+1, i+1]
        d[nums[i]] = i
      return

nums = [3, 2, 4]
target = 6
a = Solution()
print a.twoSum(nums, target)

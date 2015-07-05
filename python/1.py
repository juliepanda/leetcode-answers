# didn't pass yet, O(n^2) is too slow to pass

# Given an array of integers, find two numsbers such that they add up to a specific target numsber.

# The function twoSum should return indices of the two numsbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numsbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# @param {integer[]} nums
# @param {integer} target
# @return {integer[]}
def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(len(nums)-1, i, -1):
            if nums[i] + nums[j] == target:
                return [i+1, j+1]
    return
testNums = [0, 1, 4, 12, 5]
testTarget = 9
print twoSum(testNums, testTarget)







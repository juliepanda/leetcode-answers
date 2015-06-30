# NOT EFFICIENT YET, USE DYNAMIC PROGRAMMING

# Given an array of integers, find two numsbers such that they add up to a specific target numsber.

# The function twoSum should return indices of the two numsbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numsbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# @param {integer[]} nums
# @param {integer} target
# @return {integer[]}
def twoSum(nums, target):
    forward_ind = 0
    while forward_ind < len(nums):
        backward_ind = len(nums) - 1
        while backward_ind > forward_ind:
            if nums[forward_ind] + nums[backward_ind] == target:
                return [forward_ind + 1, backward_ind + 1]
            backward_ind = backward_ind - 1
        forward_ind = forward_ind + 1
    return

testNums = [4, 1, 7, 6, 12, 673, 23, 1, 6]
testTarget = 7
print twoSum(testNums, testTarget)







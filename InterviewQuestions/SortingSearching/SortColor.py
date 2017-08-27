"""
Given an array with n objects colored red, white or blue, sort them so that objects of the
 same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    # index = 0
    # print (len(nums))
    # while index < len(nums):
    #     if nums[index] == 0:
    #         nums.insert(0, nums.pop(index))
    #     if nums[index]  == 2:
    #         nums.append(nums.pop(index))
    #         if nums[index:] != [ 2 ]  * (len(nums) - index):
    #             index = index - 1
    #     index = index + 1

    map = {0: [], 1: [], 2: [] }
    for value in nums:
        map[value].append(value)
    vals = map[0] + map[1] + map[2]
    del(nums[:])
    for val in vals:
        nums.append(val)

nums = [1,2,0,2,1, 2, 1, 2, 1, 0]
sortColors(nums)
print(nums)


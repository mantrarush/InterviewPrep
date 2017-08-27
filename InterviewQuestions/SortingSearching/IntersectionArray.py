"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you
cannot load all elements into the memory at once?

"""

def intersection(nums1: [int], nums2: [int]) -> [int]:
    # Keys are integers from nums1 and values are the frequency of that integer
    nums = {}
    intersection = []
    for num in nums1:
        if num in nums:
            nums[num] = nums[num] + 1
        else:
            nums[num] = 1
    for num in nums2:
        if num in nums and nums[num] > 0:
            nums[num] = nums[num] - 1
            intersection.append(num)

    return intersection
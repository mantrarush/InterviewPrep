# Find the *k*th largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# Note:
# You may assume k is always valid, 1 ? k ? array's length.

#https://leetcode.com/problems/kth-largest-element-in-an-array/description/
[1,2,3,4,5,6]

def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    sortedArr  = sorted(nums)
    return 0 if len(sortedArr) == 0 else sortedArr[-k]

print(findKthLargest([2,3,1], 2))

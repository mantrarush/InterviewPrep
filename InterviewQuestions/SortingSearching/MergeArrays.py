# https://leetcode.com/problems/merge-sorted-array/description/
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
#  The number of elements initialized in nums1 and nums2 are m and n respectively.

# def merge(nums1: [int], nums2: [int], nums1Size: int, nums2Size: int) -> [int]:
#     nums1 = nums1[:nums1Size]
#     nums2 = nums2[:nums2Size]
#     mergedArr = []
#     index = 0
#     for num in nums1:
#         while index < len(nums2) and nums2[index] < num:
#             mergedArr.append (nums2[index])
#             index = index + 1
#         mergedArr.append(num)
#     remainingElems = []
#     if index < len(nums2):
#         remainingElems = nums2[index:]
#     return mergedArr + remainingElems


def merge(nums1: [int], nums2: [int], nums1Size: int, nums2Size: int) -> [int]:
    nums1_copy = nums1[:nums1Size]
    nums2_copy = nums2[:nums2Size]
    # nums1.clear()
    del(nums1[:])
    index = 0
    for num in nums1_copy:
        while index < len(nums2_copy) and nums2_copy[index] < num:
            nums1.append (nums2_copy[index])
            index = index + 1
        nums1.append(num)
    for remaininingIndex in range(index, len(nums2_copy)):
        nums1.append(nums2_copy[remaininingIndex])


nums1 = [0, 1, 3, 5]
nums2 = [2, 7, 11, 15, 21]
m = 4
n = 5
merge(nums1=nums1, nums2 = nums2, nums1Size = m, nums2Size = n)
print(nums1)
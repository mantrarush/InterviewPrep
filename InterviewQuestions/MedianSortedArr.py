"""
There are two sorted arrays nums1
 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

    #Step 1: Merge sorted arrays
    #Step 2; Depending on the size, return n/2 or avg of two
        sol_arr = self.mergeSortedArrays(nums1, nums2)
        print(sol_arr)
        return self.findMedian(sol_arr)

    def mergeSortedArrays(self, nums1: [int], nums2: [int]) -> [int]:
        # &sol_arr => 3129
        sol_arr = []
        if len(nums1) == 0 and len(nums2) == 0:
            return [0]
        arr1 = nums1 if len(nums1) <= len(nums2) else nums2
        arr2 = nums1 if len(nums2) < len(nums1) else nums2
        arr1_counter = 0
        arr1_len = len(arr1)
        for index in range(len(arr2)):
            while arr1_counter < arr1_len and arr1[arr1_counter] <= arr2[index]:
                sol_arr.append(arr1[arr1_counter])
                arr1_counter = arr1_counter + 1
            sol_arr.append(arr2[index])

        if arr1_counter < arr1_len:
            sol_arr = sol_arr + arr1[arr1_counter:]
        return sol_arr

    def findMedian(self, arr):
        return float(arr[int(len(arr)/2)]) if len(arr) % 2 == 1 else float(arr[int(len(arr)/2 - 1)] + arr[int(len(arr)/2)])*0.5

a = Solution()
print(a.findMedianSortedArrays([100001],[100000]))
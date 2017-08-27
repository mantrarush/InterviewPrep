# https://leetcode.com/problems/maximum-distance-in-arrays/description/
# Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
#
# Example 1:
# Input:
# [[1,2,3],
#  [4,5],
#  [1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
# Note:
# Each given array will have at least 1 number. There will be at least two non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].
#
def maxDistance(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    # Key is
    mins = [ (arrays[i][0], i) for i in range(len(arrays))]
    maxs = [ (arrays[i][-1], i) for i in range(len(arrays))]
    mins.sort(key=lambda l: l[0])
    maxs.sort(key=lambda l: l[0])
    maxs.reverse()
    return getMaxDistance(sortedMaxs= maxs, sortedMins=mins)


def getMaxDistance(sortedMaxs: [(int, int)], sortedMins: [(int, int)], previousMax: int = None) -> int:
    if sortedMaxs[0][1] != sortedMins[0][1]:
        firstDistance = abs(sortedMaxs[0][0] - sortedMins[0][0])
        secondDistance = firstDistance - 1
        if previousMax != None and len(sortedMins) > 1:
            secondDistance = abs(sortedMins[1][0] - previousMax)
        return max(firstDistance, secondDistance)
    if len(sortedMaxs) < 2:
        return None
    return getMaxDistance(sortedMaxs=sortedMaxs[1:], sortedMins = sortedMins, previousMax = sortedMaxs[0][0] )

print(maxDistance([[1,2,3], [4,5], [1,2,3]]))

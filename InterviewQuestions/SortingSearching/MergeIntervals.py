#https://leetcode.com/problems/merge-intervals/description/
#Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],

class Interval:
    def __init__(self, s = 0, e = 0):
        self.start, self.end = s, e

    def __str__(self):
        print(self.start, self.end)

    def includes(self, interval2):
        # [1, 10] and [8, 9]
        return interval2.start <= self.end and interval2.end <= self.end and self.start <= interval2.start

    #[5,90], [5,6]  -> [4,6]
    #[5,7], [3,6]  -> [3,7]
    #[5, 7] [2, 3] -> None
    #[1, 10], [1, 9] ->
    def join(self, interval2):
        if interval2.end >= self.start and interval2.start <= self.start:
            return Interval(interval2.start, self.end)
        return None

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    mergedIntervals  = sorted(intervals, key=lambda interval: interval.end)
    mergedIntervals.reverse()
    index = 0
    while index < len(mergedIntervals) - 1:
        joinable = mergedIntervals[index].join(mergedIntervals[index + 1])
        if joinable != None:
            mergedIntervals[index] = joinable
            mergedIntervals.pop(index + 1)
            index = index - 1
        elif mergedIntervals[index].includes(mergedIntervals[index + 1]):
            mergedIntervals.pop(index + 1)
            index = index - 1

        index = index + 1
    return mergedIntervals[::-1]

def printIntervals(intervals: [Interval]):
    print([ (interval.start, interval.end) for interval in intervals ])

# arr = []
# arr.append(Interval(2,6))
# arr.append(Interval(15,18))
# arr.append(Interval(1,3))
# arr.append(Interval(8,10))
# arr = merge(arr)
# for index in arr:
#     print (index.start, index.end)
#
# [15,18] [9,10] [2,8] [1,8]
# start0 >= start1 and start0<=end1
# start1, end0
values = [ [15,18], [9,10], [2,8], [1,8] ]
arr = [ Interval(x[0], x[1]) for x in values ]
printIntervals(merge(arr))
values = [[2,3],[4,5],[6,7],[8,9],[1,10]]
arr = [ Interval(x[0], x[1]) for x in values ]
printIntervals(merge(arr))


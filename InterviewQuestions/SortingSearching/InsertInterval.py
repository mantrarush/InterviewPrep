"""
https://leetcode.com/problems/insert-interval/description/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [1,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

#[1,2],[3,5],[6,7],[8,10],[12,16]

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        return self.findElements(intervals, newInterval)



    def findElements(self, intervals: [Interval], newInterval: Interval):
        """
               :type intervals: List[Interval]
               :type newInterval: Interval
               :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        indices = [-1,-1]
        for index in range(len(intervals)):
            self.element_includes(indices, intervals[index], newInterval, index)
        if indices == [-1, -1]:
            return self.insert_interval(intervals, newInterval)
        return self.merge_interval(indices, intervals, newInterval)



        # [-1, x] case


    def element_includes(self,indices, interval, new_interval, index):
        if interval.start <= new_interval.start <= interval.end:
            indices[0] = index
        if interval.start <= new_interval.end <= interval.end:
            indices[1] = index

    def is_exclusive(self, indices):
        return indices[0] == -1 or indices[1] == -1

    # [1, 5], [6. 8]; [0, 9]
    def insert_interval(self, intervals, newInterval):
        # [0, 5], [9, 12], [13, 18], [20, 23] ; [7, 19] => [0, 5], [7, 16]
        startVal = None
        startIndex = None
        for intervalIndex in range(len(intervals)):
            curInterval = intervals[intervalIndex]
            if startVal == None:
                if curInterval.start > newInterval.start:
                    startIndex = intervalIndex
                    startVal = newInterval.start
            else:
                if curInterval.start > newInterval.end:
                    prefix = intervals[:startIndex]
                    midFix = [Interval(s=startVal, e=newInterval.end)]
                    suffix = [] if intervalIndex > len(intervals) - 1 else intervals[intervalIndex:]
                    return prefix + midFix + suffix
        # [0, 5], [9, 12], [13, 18], [20, 23] ; [7, 25] => [0, 5], [7, 16]
        if startVal != None:
            prefix = intervals[:startIndex]
            midFix = [Interval(s=startVal, e=newInterval.end)]

            if intervals[-1].end > newInterval.end:
                return prefix + midFix + intervals[startIndex:]
            # [1, 5]; [-2. 0]
            if intervals[0].start > newInterval.end:
                return prefix + midFix + [intervals[0]]
            return prefix + midFix

        # [9, 11]: [0, 13]
        if newInterval.start < intervals[0].start and newInterval.end > intervals[0].end:
            return [newInterval]
        return intervals + [newInterval]

        # [9, 11]; [0, 13]
        # if newInterval.start <= intervals[0].start and newInterval.end >= intervals[-1].end:
        #     return [newInterval]
        # [9, 11]; [15, 20]
        # return intervals + [newInterval]


    def merge_interval(self, indices, intervals, newInterval):
        # [x, -1] case
        # [2,5], [9, 11], [15, 21] -> [,28]
        # indices = [1, -1]
        if indices[0] != -1 and indices[1] == -1:
            prefix = intervals[:indices[0]] + [Interval(s=intervals[indices[0]].start,
                                                  e=newInterval.end)]
            suffix = [] if indices[0] + 1 > len(intervals) - 1 else intervals[indices[0] + 1:]
            return prefix + suffix
        elif indices[0] == -1 and indices[1] != - 1:
            midFix = [Interval( s=newInterval.start,
                                e= intervals[indices[1]].end)
                      ] + intervals[indices[1] + 1:]
            suffix = [] if indices[1] + 1 > len(intervals) - 1 else intervals[indices[1] + 1:]
            return intervals[:indices[1]] + midFix + suffix

        prefix = intervals[:indices[0]] + [ Interval(intervals[indices[0]].start, intervals[indices[1]].end) ]
        suffix = [] if indices[1] + 1 > len(intervals) - 1 else intervals[indices[1]+1:]
        return  prefix + suffix

    def internal_helper(self, intervals: [int], newInterval: [int]):
        array = self.insert([Interval(s=value[0], e=value[1]) for value in intervals], Interval(newInterval[0], newInterval[1]))
        return [ [arr.start, arr.end] for arr in array]

import unittest


class TestMergeInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # [x, -1]
    def testMerge(self):
        intervals = [[1,3],[6,9]]
        actualAnswer = self.solution.internal_helper(intervals=intervals, newInterval=[2, 5])
        self.assertEqual(actualAnswer, [[1, 5], [6, 9]])

    # [-1, -1] at the end
    def testMergeSingleEnd(self):
        actualAnswer = self.solution.internal_helper(intervals=[[1, 5]], newInterval=[6, 8])
        self.assertEqual(actualAnswer, [[1, 5], [6, 8]])


    # [-1, -1] at the begining
    def testMergeSingleBeg(self):
        actualAnswer = self.solution.internal_helper(intervals=[[1, 5]], newInterval=[-2, 0])
        self.assertEqual(actualAnswer, [[-2, 0], [1, 5]])


    # [-1, -1] at the begining
    def testMergeSingleBetween(self):
        actualAnswer = self.solution.internal_helper(intervals=[[1,3], [6,9]], newInterval=[4, 5])
        self.assertEqual(actualAnswer, [[1,3], [4, 5], [6,9]])


    def testMergeReplace(self):
        actualAnswer = self.solution.internal_helper(intervals=[[1,5]], newInterval=[0, 6])
        self.assertEqual(actualAnswer, [[0, 6]])

    def testMergeInsert(self):
        actualAnswer = self.solution.internal_helper(intervals=[[0,5],[9,12]], newInterval=[7,16])
        self.assertEqual(actualAnswer, [[0,5],[7,16]])

    def testMergeInsertV2(self):
        actualAnswer = self.solution.internal_helper(intervals=[[1, 5], [6, 8]], newInterval=[0, 9])
        self.assertEqual(actualAnswer, [[0,9]])

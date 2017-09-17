"""
https://leetcode.com/problems/insert-interval/description/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [1,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [23,32] in as [1,2],[3,10],[12,16].
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,,13] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List


# Definition for an interval.
class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

class Solution(object):
    def insert(self, intervals, newInterval):
        return self.insert_into(intervals, newInterval)

    def insert_into(self, intervals, interval):
        intervals_before = []
        index = 0

        while index < len(intervals) and intervals[index].end < interval.start:
            intervals_before.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index].start <= interval.end:
            interval = Interval(start=min(interval.start, intervals[index].start),
                                end=max(interval.end, intervals[index].end))
            index += 1

        return intervals_before + [interval] + intervals[index:]

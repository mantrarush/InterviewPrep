# HackerRank: https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
#
# Complete the function provided in the editor below. It has one parameter: a pointer to a Node object named  that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle in the list. If there is a cycle, return true; otherwise, return false.
#
# Note: If the list is empty,  will be null.
#
# Input Format
#
# Our hidden code checker passes the appropriate argument to your function. You are not responsible for reading any input from stdin.
#
# Constraints
#
#
# Output Format
#
# If the list contains a cycle, your function must return true. If the list does not contain a cycle, it must return false. The binary integer corresponding to the boolean value returned by your function is printed to stdout by our hidden code checker.
#
# Sample Input
#
# The following linked lists are passed as arguments to your function:


"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycles(head):
    traversed_nodes = {head: True}

    while head:
        if traversed_nodes[head.next]:
            return True
        traversed_nodes[head.next] = True
        head = head.next
    return False

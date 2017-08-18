"""
Have a stack of n boxes, with widths w, heights h and depths d
Boxes can't be rotated and can be stacked on top of one another if each box in stack strictly larger than the box above
it in w, d, h
Compute height of the tallest possible stack
"""
from functools import reduce

class Box:
    def __init__(self, width: float, height: float, depth: float):
        self.w = width
        self.h = height
        self.d = depth
        
    def __gt__(self, other):
        return self.w > other.w and self.h > other.h and self.d > other.d


def waysToStack(remainingBoxes: [Box], moves: [Box], answers: [[Box]]):
    if len(remainingBoxes) == 0 and moves not in answers:
        answers.append(moves)
        return
    for box in remainingBoxes:
        if isStackable(moves, box):
            waysToStack(remainingBoxes = getBoxesWithout(remainingBoxes, box), moves= moves + [box], answers=answers)


def isStackable(stack: [Box], boxToAdd: Box) -> bool:
    if len(stack) == 0:
        return True
    return stack[-1] > boxToAdd


def getBoxesWithout(boxes: [Box], boxToRemove: Box) -> [Box]:
    if boxToRemove not in boxes:
        return []
    if boxes.index(boxToRemove) == len(boxes) - 1:
        return boxes[:-1]
    return boxes[: boxes.index(boxToRemove)] + boxes[boxes.index(boxToRemove)+1: ]



def getTallestStack(boxes: [Box]) -> [[Box]]:
    answers = [[]]
    waysToStack(remainingBoxes = boxes, moves = [], answers = answers)
    if len(answers) == 0:
        return 0
    maxVal = 0
    for moves in answers:
        maxVal = max(reduce(lambda x, y: x.h + y.h, moves), maxVal)
    return maxVal

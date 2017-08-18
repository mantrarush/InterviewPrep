'''
Given an array that has been rotated, fid the index w.r.t to the unrotated array for a given value.
'''
def indexRotated(list: [int], element: int) -> int:
    rotatedIndex = -1
    rotationCounter = 0
    for index in range(len(list) - 1):
        if list[index] == element:
            rotatedIndex = rotationCounter
        if list[index] > list[index + 1]:
            if rotatedIndex != -1:
                return len(list[index + 1: ]) + rotatedIndex
            rotationCounter = -1
        rotationCounter = rotationCounter + 1
    return rotatedIndex

print(indexRotated([4, 7, 9, 1, 2, 3], 7))
print(indexRotated([4, 7, 9, 1, 2, 3], 2))
print(indexRotated([4, 7, 9, 1, 2, 3], 1))
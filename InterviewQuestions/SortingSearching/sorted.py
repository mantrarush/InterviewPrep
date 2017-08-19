def searchInRotated(rotatedArr: [int], searchElem: int) -> int:
    if len(rotatedArr) is 0:
        return -1
    indexArr = [0, 0]
    search(rotatedArr, searchElem, indexArr)
    if indexArr[0] > indexArr[1]:
        return len(rotatedArr[indexArr[0]:]) + indexArr[1]
    else:
        return indexArr[1] - indexArr[0] if indexArr != [0,0] else -1

def search(arr: [int], findElem: int, indices: [int]):
    arrLen = len(arr)
    for index in range(arrLen):
        if index < arrLen-1 and arr[index] > arr[index+1]:
            indices[0] = index + 1
        if findElem == arr[index]:
            indices[1] = index





print(searchInRotated([1, 2, 3, 4, 7, 9], 11))

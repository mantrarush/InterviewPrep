# Child running up staircase with n steps either 1,2,3 steps at a time. Find the moves to get to that step.

def canReach(stepsLeft: int, moves: [int], answers: [int]):
    if stepsLeft == 0 and moves not in answers:
        answers.append(moves)
        return
    if stepsLeft < 0:
        return
    canReach(stepsLeft - 1, moves=moves + [1], answers=answers)
    canReach(stepsLeft - 2, moves=moves + [2], answers=answers)
    canReach(stepsLeft - 3, moves=moves + [3], answers=answers)

def canReachMain(toStep: int) -> [str]:
    answers = []
    canReach(stepsLeft=toStep - 1, moves=[1], answers=answers)
    canReach(stepsLeft=toStep - 2, moves=[2], answers=answers)
    canReach(stepsLeft=toStep - 3, moves=[3], answers=answers)
    return answers

moves = canReachMain(10)
print(moves)
print(len(moves))

'''
canReachMain(4)
    canReach(3, [1], [])
        canReach(2, [1, 1], [])
            canReach(1, [1, 1, 1], [])
                canReach(0, [1, 1, 1, 1], [])
                    APPEND [1, 1, 1, 1]
                    END
                canReach(-1, ....)
                    END
                canReach(-2, ....)
                    END

        canReach(0, [1, 1, 2], [ [1, 1, 1, 1]] )
            APPEND [1, 1, 2]
            END
        canReach(-1, ...)
            END
        canReach(-1, ...)
            END
    canReach(2, [2], [ [1, 1, 1, 1], [1, 1, 2] ])
        canReach(1, [2, 1], [ [1, 1, 1, 1], [1, 1, 2] ])
            canReach(0, [2, 1, 1], [ [1, 1, 1, 1], [1, 1, 2] ])
                APPEND [2, 1, 1]
                END
            canReach(-1, ....)
                END
            canReach(-1, ...)
                END
        canReach(0, [2, 2], [ [1, 1, 1, 1], [1, 1, 2], [2, 1, 1] ])
            APPEND [2, 2]
            END
        canReach(-1, ...)
            END
    canReach(1, [3], [ [1, 1, 1, 1], [1, 1, 2], [2, 1, 1], [2, 2 ])
        canreach(0, [3, 1],  [ [1, 1, 1, 1], [1, 1, 2], [2, 1, 1], [2, 2 ])
            APPEND [3, 1]
            END
        canReach(-1, ....)
            END
        canReach(-2. ...)
            END
'''
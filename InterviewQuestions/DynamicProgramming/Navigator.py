# For a given position of a robot x, y. Find the unique move(s) to get to a target position x, y
# given that the robot can only move down and right. Assume top left is 0, 0.
# A position may or may not be valid
# The canvas is columns x rows large.

ROWS = 3
COLUMNS = 3

class Position:
    def __init__(self, x: int, y: int, validity: bool = True):
        self.x = x
        self.y = y
        self.isValid = validity

def getMoves(cur_pos: Position, target: Position, moves: [Position], answers: [Position]):
    pass


def getMovesMain(cur_pos: Position, target: Position) -> [Position]:
    return []

initPos = Position(x=0, y=0)
targetPos = Position(x=COLUMNS, y=ROWS)
print(getMovesMain(initPos, targetPos))
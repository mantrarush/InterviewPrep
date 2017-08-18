from copy import copy

def paint_fill(scene: [[int]], current_pixel: [int], initial_color: int, final_color: int):
    if len(scene) < current_pixel[0] or current_pixel[0] < 0 or current_pixel[1] < 0 or len(scene[0]) < current_pixel[1]:
        return

    if initial_color == final_color:
        return

    current_color = scene[current_pixel[0]][current_pixel[1]]
    if current_color == initial_color:
        scene[current_pixel[0]][current_pixel[1]] = final_color
        return

    paint_fill(scene, [current_pixel[0] + 1, current_pixel[1]], initial_color, final_color)
    paint_fill(scene, [current_pixel[0] - 1, current_pixel[1]], initial_color, final_color)
    paint_fill(scene, [current_pixel[0], current_pixel[1] + 1], initial_color, final_color)
    paint_fill(scene, [current_pixel[0], current_pixel[1] - 1], initial_color, final_color)

def paint_filler(scene: [[int]], starting_point: [int], new_color: int):
    paint_fill(scene, starting_point, scene[starting_point[0]][starting_point[1]], new_color)



class Color:
    def __init__(self, r: float, g: float, b: float):
        self.red = r
        self.green = g
        self.blue = b

class Pixel:
    def __init__(self, x: int, y: int, color: Color = None):
        self.color = color
        self.x = x
        self.y = y


class Scene:
    def __init__(self, rows: int, cols: int):
        self.data = []
        for i in range(rows):
            self.data.append([Pixel(x=col, y=i) for col in range(cols)])
        self.rows = rows
        self.cols = cols

    def __getitem__(self, item: Pixel):
         return self.data[item.x][item.y]

    def __setitem__(self, key: Pixel, value: Color):
        self.data[key.x][key.y] = value


def paint_fill2(scene: Scene, current_pixel: Pixel, initial_color: Color, final_color: Color):
    if scene.cols < current_pixel.x or current_pixel.x < 0 or current_pixel.y < 0 or scene.rows < current_pixel.y or initial_color == final_color:
        return

    current_color = scene[current_pixel]
    if current_color == initial_color:
        scene[current_pixel] = final_color
        return
    paint_fill2(scene, Pixel(x=current_pixel.x + 1, y = current_pixel.y), initial_color, final_color)
    paint_fill2(scene, Pixel(x=current_pixel.x - 1, y = current_pixel.y), initial_color, final_color)
    paint_fill2(scene, Pixel(x=current_pixel.x, y = current_pixel.y + 1), initial_color, final_color)
    paint_fill2(scene, Pixel(x=current_pixel.x, y = current_pixel.y - 1), initial_color, final_color)


def paint_filler2(scene: Scene, starting_point: Pixel, new_color: Color):
    paint_fill2(scene, starting_point, scene[starting_point], new_color)

#scene = Scene(10, 12)
#print("lel")


class Board:
    def __init__(self, rows: int, cols: int):
        self.canvas = [[False]*cols for i in range(rows)]

def boardPrinter(board: [[bool]]):
    buffer = ""
    for row in range(8):
        for col in range(8):
            if board[row][col] == False:
                buffer = buffer + "0\t"
            else:
                buffer = buffer + "1\t"
        buffer = buffer + "\n"
    print(buffer+"\n\n\n")


# Diagnols
def fillBoard(pieces: int, board: [[bool]], memoRows: [], memoCols: [], memoDiags: {int: [int]}):
    possibleRows = set([i for i in range(8)]).difference(set(memoRows))
    possibleCols = set([i for i in range(8)]).difference(memoCols)
    if pieces == 0:
        boardPrinter(board)
        return

    if len(possibleRows) == 0 or len(possibleCols) == 0:
        return
    for row in possibleRows:
        for col in possibleCols:
            if row in memoDiags and col in memoDiags[row]:
                pass
            boardCopy = copy(board)
            boardCopy[row][col] = True
            memoDiags[row] = []
            fillBoard(pieces = pieces - 1, board = boardCopy, memoRows = memoRows + [row], memoCols = memoCols + [col])


brd = Board(8, 8)
fillBoard(8, brd.canvas, memoRows=[], memoCols=[])
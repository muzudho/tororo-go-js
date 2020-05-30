pure_board_map = []
for y in range(2, 15):
    for x in range(2, 15):
        pure_board_map.append((x, y))
# print(f'pure_board_map=len:{len(pure_board_map)} {pure_board_map}')

window_5x5 = []
for y in range(-2, 3):
    for x in range(-2, 3):
        window_5x5.append((x, y))
# print(f'window_5x5=len:{len(window_5x5)} {window_5x5}')

"""
-2 . . x
-1 . x x
 0 @ x x
 1 . x x
 2 . . x
   0 1 2
"""
eastward = [(2, -2), (1, -1), (2, -1), (1, 0),
            (2, 0), (1, 1), (2, 1), (2, 2)]

"""
-2 x x x
-1 x x x
 0 @ x x
 1 . . .
 2 . . .
   0 1 2
"""
north_eastward = [(0, -2), (1, -2), (2, -2), (0, -1),
                  (1, -1), (2, -1), (1, 0), (2, 0)]

"""
-2  x  x  x  x  x
-1  x  x  x  x  x
 0  x  x  @  x  x
 1  x  x  x  x  x
 2  x  x  x  x  x
   -2 -1  0  1  2
"""
neighbor24_map = [(-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
                  (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
                  (-2, 0), (-1, 0), (1, 0), (2, 0),
                  (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1),
                  (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2)]


def stone_density_node(stone_board):
    """盤サイズは 太さ2と3の枠が付いた 計18x18 にしてください。"""
    num_board = [0] * (18*18)

    def count_up(stone_board, p, pp):
        nonlocal num_board
        if stone_board[to_addr18x18(pp)] != '.':
            num_board[to_addr18x18(p)] += 1

    scan_pure_board(lambda p: scan_window_5x5(
        lambda pp: count_up(stone_board, p, pp), p))
    return num_board


'''
def scan_neighbor8(f, p):
    for pp in neighbor24_map:
        f((pp[0] + p[0], pp[1]+p[1]))
    pass
'''


def scan_pure_board(f):
    """枠を除いた、盤上を１マスずつイテレートして座標を返します。Y座標は行番号です。"""
    for p in pure_board_map:
        f(p)


def scan_window_5x5(f, p):
    """中心を p とする 5x5 のウィンドウの各マスをイテレートして座標を返します。"""
    for pp in window_5x5:
        f((p[0]+pp[0], p[1]+pp[1]))


'''
def match_color(stone_board, p, color):
    if stone_board[to_addr18x18(p)] == color:
        return 1

    return 0
'''


def stone_density_sq():
    pass


def directed_stone_density_node():
    pass


def directed_stone_density_sq():
    pass


def ccw90(p):
    """反時計回りに90°回転"""
    return (-p[1], p[0])


def ccw180(p):
    """反時計回りに180°回転"""
    p = ccw90((-p[1], p[0]))
    return (-p[1], p[0])


def ccw270(p):
    """反時計回りに270°回転"""
    p = ccw180((-p[1], p[0]))
    return (-p[1], p[0])


def to_addr18x18(p):
    """18x18盤の番地に変換"""
    return 18*p[1]+p[0]


'''
for p in pure_board_map:
    # print(p)
    print(to_addr18x18(p))
'''

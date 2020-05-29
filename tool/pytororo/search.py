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


def stone_density_node(stone_board, color):
    """盤サイズは 太さ2の枠が付いた 計17x17 にしてください。"""
    num_board = [0] * (17*17)

    def count_up(stone_board, p, color):
        nonlocal num_board
        num_board[to_addr17x17(p)] += match_color(stone_board, p, color)

    scan_board(lambda p: scan_neighbor8(
        lambda pp: count_up(stone_board, pp, color), p))
    return num_board


def scan_neighbor8(f, p):
    for pp in neighbor24_map:
        f((pp[0] + p[0], pp[1]+p[1]))
    pass


def scan_board(f):
    """枠を除いた、盤上を１マスずつイテレートします。"""
    for x in range(2, 15):
        for y in range(2, 15):
            f((x, y))


def match_color(stone_board, p, color):
    if stone_board[to_addr17x17(p)] == color:
        return 1

    return 0


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


def to_addr17x17(p):
    """17x17盤の番地に変換"""
    return 17*p[1]+p[0]

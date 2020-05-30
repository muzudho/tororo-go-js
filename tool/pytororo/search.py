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

# 右側、下側に１つ多め。
window_6x6 = []
for y in range(-2, 4):
    for x in range(-2, 4):
        window_6x6.append((x, y))
# print(f'window_6x6=len:{len(window_6x6)} {window_6x6}')


def ccw90(p):
    """反時計回りに90°回転"""
    return (-p[1], p[0])


dir_node_map = []

"""
西向きを手動で作ります。
-2 . . x
-1 . x x
 0 @ x x
 1 . x x
 2 . . x
   0 1 2
"""
dir_node_map.append([(2, -2), (1, -1), (2, -1), (1, 0),
                     (2, 0), (1, 1), (2, 1), (2, 2)])
"""
北西を手動で作ります。
-2 x x x
-1 x x x
 0 @ x x
 1 . . .
 2 . . .
   0 1 2
"""
dir_node_map.append([(0, -2), (1, -2), (2, -2), (0, -1),
                     (1, -1), (2, -1), (1, 0), (2, 0)])

# あとは90°回転で作るぜ☆（＾～＾）
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[0])))
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[1])))
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[2])))
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[3])))
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[4])))
dir_node_map.append(list(map(lambda p: ccw90(p), dir_node_map[5])))
# print(f'dir_node_map=len:{len(dir_node_map)} {dir_node_map}')


def drop_shadow(p):
    """右下に影が落ちるような座標"""
    return p, (p[0]+1, p[1]), (p[0], p[1]+1), (p[0]+1, p[1]+1)


def flat(m):
    """重複とネストを解消します。順はばらばらになります。"""
    s = set()
    for items in m:
        # items は ((),(),(),()) みたいに丸かっこがネストしている。
        for item in items:
            s.add(item)
    return list(s)


dir_sq_map = []
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[0])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[1])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[2])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[3])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[4])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[5])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[6])))
dir_sq_map.append(flat(map(lambda p: drop_shadow(p), dir_node_map[7])))
# print(f'dir_sq_map=len:{len(dir_sq_map)} {dir_sq_map}')


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


def stone_density_sq(stone_board):
    """盤サイズは 太さ2と3の枠が付いた 計18x18 にしてください。"""
    num_board = [0] * (18*18)

    def count_up(stone_board, p, pp):
        nonlocal num_board
        if stone_board[to_addr18x18(pp)] != '.':
            num_board[to_addr18x18(p)] += 0.25
            num_board[to_addr18x18((p[0]+1, p[1]))] += 0.25
            num_board[to_addr18x18((p[0], p[1]+1))] += 0.25
            num_board[to_addr18x18((p[0]+1, p[1]+1))] += 0.25

    scan_pure_board(lambda p: scan_window_6x6(
        lambda pp: count_up(stone_board, p, pp), p))
    return num_board


def directed_stone_density_node(stone_board, ccw45: int):
    """
    Parameters
    ----------
    ccw45:
        0 - 東
        1 - 北東
        2 - 北
        3 - 北西
        4 - 西
        5 - 南西
        6 - 南
        7 - 南東
    """
    num_board = [0] * (18*18)

    def count_up(stone_board, p, pp):
        nonlocal num_board
        if stone_board[to_addr18x18(pp)] != '.':
            num_board[to_addr18x18(p)] += 1

    scan_pure_board(lambda p: scan_window_dir_node(
        lambda pp: count_up(stone_board, p, pp), ccw45, p))
    return num_board


def directed_stone_density_sq(stone_board, ccw45: int):
    """
    Parameters
    ----------
    ccw45:
        0 - 東
        1 - 北東
        2 - 北
        3 - 北西
        4 - 西
        5 - 南西
        6 - 南
        7 - 南東
    """
    num_board = [0] * (18*18)

    def count_up(stone_board, p, pp):
        nonlocal num_board
        if stone_board[to_addr18x18(pp)] != '.':
            num_board[to_addr18x18(p)] += 0.25
            num_board[to_addr18x18((p[0]+1, p[1]))] += 0.25
            num_board[to_addr18x18((p[0], p[1]+1))] += 0.25
            num_board[to_addr18x18((p[0]+1, p[1]+1))] += 0.25

    scan_pure_board(lambda p: scan_window_dir_sq(
        lambda pp: count_up(stone_board, p, pp), ccw45, p))
    return num_board


def scan_pure_board(f):
    """枠を除いた、盤上を１マスずつイテレートして座標を返します。Y座標は行番号です。"""
    for p in pure_board_map:
        f(p)


def scan_window_5x5(f, p):
    """中心を p とする 5x5 のウィンドウの各マスをイテレートして座標を返します。"""
    for pp in window_5x5:
        f((p[0]+pp[0], p[1]+pp[1]))


def scan_window_6x6(f, p):
    """中心を p とする 6x6 のウィンドウの各マスをイテレートして座標を返します。"""
    for pp in window_6x6:
        f((p[0]+pp[0], p[1]+pp[1]))


def scan_window_dir_node(f, ccw45, p):
    """起点を p とする方向性のあるウィンドウの各マスをイテレートして座標を返します。"""
    for pp in dir_node_map[ccw45]:
        f((p[0]+pp[0], p[1]+pp[1]))


def scan_window_dir_sq(f, ccw45, p):
    """起点を p とする方向性のあるウィンドウの各マスをイテレートして座標を返します。"""
    for pp in dir_sq_map[ccw45]:
        f((p[0]+pp[0], p[1]+pp[1]))


def to_addr18x18(p):
    """18x18盤の番地に変換"""
    return 18*p[1]+p[0]


'''
for p in pure_board_map:
    # print(p)
    print(to_addr18x18(p))
'''

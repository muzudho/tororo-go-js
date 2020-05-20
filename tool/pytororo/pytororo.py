def stone_board(board):
    return board.replace(' ', '').replace('\n', '').replace('/', '')


def black_stone(stone_board):
    return stone_board.replace('o', '.')


def white_stone(stone_board):
    return stone_board.replace('x', '.')


def print_stone_board(stone_board):
    for stone in stone_board:
        if stone == '.':
            print('<img src="img/s.png">', end='')
        elif stone == "x":
            print('<img src="img/b.png">', end='')
        elif stone == "o":
            print('<img src="img/w.png">', end='')
        elif stone == "/":
            print('<br>')
        elif stone == " " or stone == "\n":
            pass
        else:
            print(f"[{stone}]?", end='')

    print()  # New line.


def print_cake_board(cake_board):
    """餅の色情報は持てません。
    """
    for i, cake in enumerate(cake_board):
        if cake == 0:
            print('<img src="img/s.png">', end='')
        else:
            # print(f'i={i} cake={cake:02X} {cake//0x10:02X}')
            under_p = coordinate_under(cake)
            print(
                f'<img src="img/gray-stone.png" style="object-fit: none; object-position:{under_p[0]}px {under_p[1]}px; width:40px; height:40px;">', end='')

        if i % 13 == 12:
            print('<br>')

    print('')  # New line.


def coordinate_under(cake):
    arr = [
        [0, 0],  # 0
        [-40, 0],  # 1
        [0, -120],  # 2
        [-40, -120],  # 3
        [-120, 0],  # 4
        [-80, 0],  # 5
        [-120, -120],  # 6
        [-80, -120],  # 7
        [0, -40],  # 8
        [-40, -40],  # 9
        [0, -80],  # A
        [-40, -80],  # B
        [-120, -40],  # C
        [-80, -40],  # D
        [-120, -80],  # E
        [-80, -80]]  # F
    return arr[cake//0x10]


def sticky_rice_cake_board(stone_board):
    """餅盤を作ります。"""
    result = []

    for i, stone in enumerate(stone_board):
        under, cover = sticky_rice_cake(stone_board, i, stone)
        # print(
        #    f'i={i} stone={stone} sticky_rice_cake={under+cover:02X} under={under} cover={cover}')
        result.append(under+cover)

    return result


def sticky_rice_cake(board: str, index, stone):
    """餅数を求めます。

    Parameters
    ----------
    board:
        /、空白、改行記号は取り除いておいてください。
    """
    under = 0
    cover = 0

    if stone == '.':
        return (under, cover)

    col = index % 13
    row = index // 13

    # 北西
    if 0 <= index-14 and board[index-14] == stone and col != 0 and row != 0:
        cover += 0x02

    # 北
    if 0 <= index-13 and board[index-13] == stone and row != 0:
        under += 0x20

    # 北東
    if 0 <= index-12 < 12 and board[index-12] == stone and col != 12 and row != 0:
        cover += 0x01

    # 西
    if 0 <= index-1 and board[index-1] == stone and col != 0:
        under += 0x40

    # 東
    if index + 1 < len(board) and board[index+1] == stone and col != 12:
        under += 0x10

    # 南西
    if index + 12 < len(board) and board[index+12] == stone and col != 0 and row != 12:
        cover += 0x04

    # 南
    if index + 13 < len(board) and board[index+13] == stone and row != 12:
        under += 0x80

    # 南東
    if index + 14 < len(board) and board[index+14] == stone and col != 12 and row != 12:
        cover += 0x8

    return (under, cover)

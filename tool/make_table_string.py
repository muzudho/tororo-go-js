def go():
    print('Trace   | Start.')

    # 1st layer.
    for row in range(0, 5):
        for col in range(0, 5):
            pass

    # 2nd layer.
    for row in range(0, 5):
        for col in range(0, 4):
            pass

    # 3rd layer.
    for row in range(0, 5):
        for col in range(0, 4):
            pass

    # 4th layer.
    for row in range(0, 4):
        for col in range(0, 5):
            pass

    # 5th layer.
    for row in range(0, 4):
        for col in range(0, 4):
            pass

    # 6th layer.
    for row in range(0, 4):
        for col in range(0, 4):
            pass

    # 7th layer.
    for row in range(0, 4):
        for col in range(0, 5):
            pass

    # 8th layer.
    for row in range(0, 4):
        for col in range(0, 4):
            pass

    # 9th layer.
    for row in range(0, 4):
        for col in range(0, 4):
            pass

    print('Trace   | Finish.')


def neighbor8(board: str, index, stone):
    """紐付きパターンを求めます。

    Parameters
    ----------
    board:
        /、空白、改行記号は取り除いておいてください。
    """
    num = 0

    if stone != '.':
        return 0

    col = index % 13
    row = index // 13

    # 北西
    if 0 <= index-14 and board[index-14] == stone and col != 0 and row != 0:
        num += 0b00001000

    # 北
    if 0 <= index-13 and board[index-13] == stone and row != 0:
        num += 0b00000100

    # 北東
    if 0 <= index-12 and board[index-12] == stone and col != 12 and row != 0:
        num += 0b00000010

    # 西
    if 0 <= index-1 and board[index-1] == stone and col != 0:
        num += 0b00010000

    # 東
    if index + 1 < len(board) and board[index+1] == stone and col != 12:
        num += 0b00000001

    # 南西
    if index + 12 < len(board) and board[index+12] == stone and col != 0 and row != 12:
        num += 0b00100000

    # 南
    if index + 13 < len(board) and board[index+13] == stone and row != 12:
        num += 0b01000000

    # 南東
    if index + 14 < len(board) and board[index+14] == stone and col != 12 and row != 12:
        num += 0b10000000

    return num


def image_num():
    """TODO 画像番号。"""
    pass


def coordinate_string(num):
    # 31パターンのヒモ。
    if num == 47:
        return (0, 0)
    elif num == 57:
        return (1*-40, 0)
    elif num == 58:
        return (2*-40, 0)
    elif num == 16:
        return (4*-40, 0)
    elif num == 35:
        return (5*-40, 0)
    elif num == 36:
        return (6*-40, 0)
    elif num == 38:
        return (0, 1*-40)
    elif num == 13:
        return (1*-40, 1*-40)
    elif num == 14:
        return (2*-40, 1*-40)
    elif num == 15:
        return (3*-40, 1*-40)
    elif num == 25:
        return (4*-40, 1*-40)
    elif num == 17:
        return (5*-40, 1*-40)
    elif num == 27:
        return (6*-40, 1*-40)
    elif num == 37:
        return (7*-40, 1*-40)
    elif num == 1357:
        return (0, 2*-40)
    elif num == 1571:
        return (1*-40, 2*-40)
    elif num == 7135:
        return (2*-40, 2*-40)
    elif num == 3583:
        return (4*-40, 2*-40)
    elif num == 274:
        return (5*-40, 2*-40)
    elif num == 1361:
        return (6*-40, 2*-40)
    elif num == 1371:
        return (0, 3*-40)
    elif num == 15037:
        return (1*-40, 3*-40)
    elif num == 3573:
        return (2*-40, 3*-40)
    elif num == 416:
        return (4*-40, 3*-40)
    elif num == 258:
        return (6*-40, 3*-40)
    elif num == 1753:
        return (0, 4*-40)
    elif num == 1351:
        return (1*-40, 4*-40)
    elif num == 3175:
        return (2*-40, 4*-40)
    elif num == 2572:
        return (4*-40, 4*-40)
    elif num == 638:
        return (5*-40, 4*-40)
    elif num == 1471:
        return (6*-40, 4*-40)
    else:
        raise f'Invalid num={num}'


go()

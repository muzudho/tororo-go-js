def go():
    print('Trace   | Start.')

    board = """\
.x...o......./
ooxxxxoo...../
.oox..x..o.../
o.oox..x...../
oooox....o.../
xxxx..x.o..../
............./
.......x.o.o./
.x........ox./
ox.x...x.oxx./
.ox....xooxxo/
oox....xxxoo./
.o.........../
    """

    board_array = board.replace(' ', '').replace('\n', '').replace('/', '')

    for i, stone in enumerate(board_array):
        under, cover = number(board_array, i, stone)
        under_p = coordinate_under(under)
        # print(
        #    f'i={i} under=0x{under:02X} cover=0x{cover:02X} under_p0={under_p[0]} under_p1={under_p[1]}')
        if stone == '.':
            print('<img src="img/s.png">', end='')
        elif stone == "x":
            print(
                f'<img src="img/black-stone.png" style="object-fit: none; object-position:{under_p[0]}px {under_p[1]}px; width:40px; height:40px;">', end='')
        elif stone == "o":
            print(
                f'<img src="img/white-stone.png" style="object-fit: none; object-position:{under_p[0]}px {under_p[1]}px; width:40px; height:40px;">', end='')
        elif stone == "/":
            print('<br>')
        elif stone == " " or stone == "\n":
            pass
        else:
            print(f"[{stone}]?", end='')

    print('')  # New line.
    print('Trace   | Finished.')


def coordinate_under(num):
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
    return arr[num//0x10]


def number(board: str, index, stone):
    """
    Parameters
    ----------
    board:
        /、空白、改行記号は取り除いておいてください。
    """
    under = 0
    cover = 0

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


go()

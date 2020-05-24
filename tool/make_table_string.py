from pytororo.pytororo import stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board


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

    stone_board1 = stone_board(board)
    white_stone_board = white_stone(stone_board1)

    img_num_dict = create_image_num_dict()
    # print(f'Debug   | img_num_dict={img_num_dict}')
    coord_string_dict = create_coordinate_string_dict()
    # print(f'Debug   | coord_string_dict={coord_string_dict}')

    def print_layer(cols, rows, dx, dy):
        for row in range(0, rows):
            for col in range(0, cols):
                addr = 3*(row+dy)*cols + 3*col+dx
                bit = neighbor8(white_stone_board, addr, 'o')
                """
                if bit is not None:
                    print(
                        f'Debug   | addr={addr:>3} bit={bit:>3} exists={bit in img_num_dict}')
                else:
                    print(
                        f'Debug   | addr={addr} None')
                """
                """
                # Grid
                print(
                    f'<img src="img/rect-m.png" style="width:120px; height:120px;">', end='')
                """

                if bit in img_num_dict:
                    img_num = img_num_dict[bit]
                    coord = coord_string_dict[img_num]
                    print(
                        f'<img src="img/white-string.png" style="object-fit: none; object-position:{coord[0]}px {coord[1]}px; width:120px; height:120px;">', end='')
                else:
                    print(
                        f'<img src="img/_.png" style="width:120px; height:120px;">', end='')

        print('')  # New line.

    # 1st layer.
    print('\nTrace   | 1st layer.\n')
    print_layer(5, 5, 0, 0)

    # 2nd layer.
    print('\nTrace   | 2nd layer.\n')
    print_layer(4, 5, 1, 0)

    # 3rd layer.
    print('\nTrace   | 3rd layer.\n')
    print_layer(4, 5, 2, 0)

    # 4th layer.
    print('\nTrace   | 4th layer.\n')
    print_layer(4, 5, 0, 1)

    # 5th layer.
    print('\nTrace   | 5th layer.\n')
    print_layer(4, 4, 1, 1)

    # 6th layer.
    print('\nTrace   | 6th layer.\n')
    print_layer(4, 4, 2, 1)

    # 7th layer.
    print('\nTrace   | 7th layer.\n')
    print_layer(5, 4, 0, 2)

    # 8th layer.
    print('\nTrace   | 8th layer.\n')
    print_layer(4, 4, 1, 2)

    # 9th layer.
    print('\nTrace   | 9th layer.\n')
    print_layer(4, 4, 2, 2)

    print('Trace   | Finish.')


def neighbor8(board: str, index, stone):
    """紐付きパターンを求めます。

    Parameters
    ----------
    board:
        /、空白、改行記号は取り除いておいてください。
    """
    num = 0

    if board[index] != '.':
        return

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


def create_image_num_dict():
    """TODO 画像番号連想配列。"""

    dic = {}

    for i in [72, 104, 143, 200, 232]:
        dic[i] = 47

    for i in [132, 134, 140, 142, 188]:
        dic[i] = 38

    for i in [80, 88, 92, 94, 208, 209, 211, 215, 216, 217, 219, 220, 221, 222]:
        dic[i] = 57

    for i in [5, 13, 29, 61, 125, 133, 141, 157, 189, 197, 205, 229, 237]:
        dic[i] = 13

    for i in [144, 152, 156, 158, 176, 184, 190]:
        dic[i] = 58

    for i in [9, 11, 137, 139, 201, 233, 235]:
        dic[i] = 14

    for i in [17, 19, 25, 27, 49, 51, 57, 59, 145, 147, 153, 155, 177, 179, 185]:
        dic[i] = 15

    for i in [33, 35, 47, 161, 163]:
        dic[i] = 16

    for i in [18, 26, 50, 58, 242]:
        dic[i] = 25

    for i in [20, 22, 23, 52, 54, 55, 116, 118, 135, 183, 244, 245, 246]:
        dic[i] = 35

    for i in [65, 67, 71, 79, 95, 97, 99, 103, 111, 113, 115, 119, 121, 123]:
        dic[i] = 17

    for i in [36, 38, 39, 44, 46, 167, 175]:
        dic[i] = 36

    for i in [66, 98, 114, 122, 194, 226, 250]:
        dic[i] = 27

    for i in [68, 70, 76, 78, 100, 102, 108, 110, 196, 198, 204, 206, 228, 230, 236]:
        dic[i] = 37

    for i in [85]:
        dic[i] = 15037

    for i in [84, 86, 212, 214]:
        dic[i] = 3573

    for i in [117]:
        dic[i] = 7135

    for i in [81, 83, 89, 91]:
        dic[i] = 1571

    for i in [213]:
        dic[i] = 1357

    for i in [69, 77, 101, 109]:
        dic[i] = 1371

    for i in [87]:
        dic[i] = 1753

    for i in [21, 53, 149, 181]:
        dic[i] = 1351

    for i in [93]:
        dic[i] = 3175

    for i in [146, 154, 178, 186]:
        dic[i] = 258

    for i in [37, 45, 165, 173]:
        dic[i] = 1361

    for i in [74, 106, 202, 234]:
        dic[i] = 274

    for i in [148, 150, 180, 182]:
        dic[i] = 3583

    for i in [41, 43, 169, 171]:
        dic[i] = 416

    for i in [82, 90, 210, 218]:
        dic[i] = 2572

    for i in [164, 166, 172, 174]:
        dic[i] = 638

    for i in [73, 75, 105, 107]:
        dic[i] = 1471

    return dic


def create_coordinate_string_dict():
    """31パターンのヒモ。"""
    w = 60
    h = 60
    return {
        47: (0, 0),
        57: (1*-w, 0),
        58: (2*-w, 0),
        16: (4*-w, 0),
        35: (5*-w, 0),
        36: (6*-w, 0),
        38: (0, 1*-h),
        13: (1*-w, 1*-h),
        14: (2*-w, 1*-h),
        15: (3*-w, 1*-h),
        25: (4*-w, 1*-h),
        17: (5*-w, 1*-h),
        27: (6*-w, 1*-h),
        37: (7*-w, 1*-h),
        1357: (0, 2*-h),
        1571: (1*-w, 2*-h),
        7135: (2*-w, 2*-h),
        3583: (4*-w, 2*-h),
        274: (5*-w, 2*-h),
        1361: (6*-w, 2*-h),
        1371: (0, 3*-h),
        15037: (1*-w, 3*-h),
        3573: (2*-w, 3*-h),
        416: (4*-w, 3*-h),
        258: (6*-w, 3*-h),
        1753: (0, 4*-h),
        1351: (1*-w, 4*-h),
        3175: (2*-w, 4*-h),
        2572: (4*-w, 4*-h),
        638: (5*-w, 4*-h),
        1471: (6*-w, 4*-h),
    }


go()

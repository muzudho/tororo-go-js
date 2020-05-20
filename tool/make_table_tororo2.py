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
    black_stone_board = black_stone(stone_board1)
    print(f'black_stone_board = {black_stone_board}')
    print_stone_board(black_stone_board)

    white_stone_board = white_stone(stone_board1)
    print(f'white_stone_board = {white_stone_board}')
    print_stone_board(white_stone_board)

    black_cake_board = sticky_rice_cake_board(black_stone_board)
    print(f'black_cake_board = {black_cake_board}')
    print_cake_board(black_stone_board, black_cake_board)

    white_cake_board = sticky_rice_cake_board(white_stone_board)
    print(f'white_cake_board = {white_cake_board}')
    print_cake_board(white_stone_board, white_cake_board)

    def print_cake_cover(corners_board, color):
        for i, corners in enumerate(corners_board):
            if corners == 4:
                under_p = coordinate_cover()
                if color == 'black':
                    print(
                        f'<img src="img/black-stone.png" style="object-fit: none; object-position:{under_p[0]}px {under_p[1]}px; width:40px; height:40px;">', end='')
                elif color == 'white':
                    print(
                        f'<img src="img/white-stone.png" style="object-fit: none; object-position:{under_p[0]}px {under_p[1]}px; width:40px; height:40px;">', end='')
                else:
                    raise f'Invalid color={color}'
            else:
                print('<img src="img/_.png">', end='')

            if i % 12 == 11:
                print('<br>')

        print('')  # New line.

    print('Trace   | Black cake cover.')
    corners_board = convolute(black_cake_board)
    print_cake_cover(corners_board, 'black')

    print('Trace   | White cake cover.')
    corners_board = convolute(white_cake_board)
    print_cake_cover(corners_board, 'white')

    print('Trace   | Finished.')


def coordinate_cover():
    return (-180, -20)


def convolute(cake_board):
    print(f'len(cake_board): {len(cake_board)}')
    print(f'cake_board: {cake_board}')
    #corner_table = corner_number_table()
    #print(f'corner_table: {corner_table}')
    #print(f'len(corner_table): {len(corner_table)}')

    result = []

    rows = 12
    cols = 12
    for row in range(0, rows):
        for col in range(0, cols):
            adr = address(row, col)
            sum = 0
            # +------+
            # |      |
            # |    08|
            # +------+
            # 左上タイルの右下コーナー
            if cake_board[adr] & 0x08:
                sum += 1
            # +------+
            # |      |
            # |04    |
            # +------+
            # 右上タイルの左下コーナー
            if cake_board[adr+1] & 0x04:
                sum += 1
            # +------+
            # |    01|
            # |      |
            # +------+
            # 左下タイルの右上コーナー
            if cake_board[adr+13] & 0x01:
                sum += 1
            # +------+
            # |02    |
            # |      |
            # +------+
            # 右下タイルの左上コーナー
            if cake_board[adr+14] & 0x02:
                sum += 1
            result.append(sum)

    return result


def address(row, col):
    return row * 13 + col


def corner_number_table():
    def corners_number(num):
        s = f'{num:04b}'
        #print(f'bit {num} : {s}')
        sum = 0
        for i in range(len(s)-1):
            if s[i] == '1' and s[i+1] == '1':
                sum += 1
        if s[len(s)-1] == '1' and s[0] == '1':
            sum += 1
        return sum

    table = []
    for num in range(16):
        table.append(corners_number(num))

    return table


go()

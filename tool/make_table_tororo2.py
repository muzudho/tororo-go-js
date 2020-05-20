from pytororo.pytororo import sticky_rice_cake, sticky_rice_cake_board


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
    n_board = sticky_rice_cake_board(board_array)
    print(f'n_board: {n_board}')
    conv_board = convolute(n_board)

    for i, corners in enumerate(conv_board):
        #print(f'i={i} corners={corners}')
        if 1 < corners:
            print('<img src="img/b.png">', end='')
        else:
            print('<img src="img/s.png">', end='')

        if i % 12 == 11:
            print('<br>')

    print('')  # New line.
    print('Trace   | Finished.')


def coordinate_cover():
    return (-180, -20)


def convolute(sticky_rice_cake_board):
    #print(f'len(sticky_rice_cake_board): {len(sticky_rice_cake_board)}')
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
            # 左上タイルの右下コーナー
            # print(f'num a: {adr} {sticky_rice_cake_board[adr]:02X} {sticky_rice_cake_board[adr]//0x10}')
            if sticky_rice_cake_board[adr] & 0x01:
                sum += 1
            # print(
            #    f'num b: {adr+1} {sticky_rice_cake_board[adr+1]:02X} {sticky_rice_cake_board[adr+1]//0x10}')
            if sticky_rice_cake_board[adr+1] & 0x02:
                sum += 1
            # print(
            #    f'num c: {adr+13} {sticky_rice_cake_board[adr+13]:02X} {sticky_rice_cake_board[adr+13]//0x10}')
            if sticky_rice_cake_board[adr+13] & 0x04:
                sum += 1
            # print(
            #    f'num d: {adr+14} {sticky_rice_cake_board[adr+14]:02X} {sticky_rice_cake_board[adr+14]//0x10}')
            if sticky_rice_cake_board[adr+14] & 0x08:
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

from pytororo.pytororo import stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, print_cake_cover, convolute


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

    print('Trace   | Black cake cover.')
    corners_board = convolute(black_cake_board)
    print_cake_cover(corners_board, 'black')

    print('Trace   | White cake cover.')
    corners_board = convolute(white_cake_board)
    print_cake_cover(corners_board, 'white')

    print('Trace   | Finished.')


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

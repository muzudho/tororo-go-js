from pytororo.pytororo import resize13to18str, line_to_table_str, line_to_table, stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, print_cake_cover, convolute
from pytororo.search import stone_density_node


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
    # 18x18=324
    stone_board324 = resize13to18str(stone_board1, '.')
    stone_board18x18 = line_to_table_str(stone_board324, 18)
    print(stone_board18x18)

    num_board324 = stone_density_node(stone_board324)
    # print(num_board324)
    num_board18x18 = line_to_table(num_board324, 18)
    # print(num_board18x18)

    row_format = "{:>3}" * 18
    for row in num_board18x18:
        print(row_format.format(*row))

    print('Trace   | Finished.')


go()

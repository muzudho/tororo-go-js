from pytororo.pytororo import resize13to18str, line_to_table_str, line_to_table, stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, print_cake_cover, convolute
from pytororo.search import stone_density_node, stone_density_sq


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

    density_node_board324 = stone_density_node(stone_board324)
    # print(density_node_board324)
    density_node_board18x18 = line_to_table(density_node_board324, 18)
    # print(density_node_board18x18)

    row_format = "{:>6}" * 18
    for row in density_node_board18x18:
        print(row_format.format(*row))

    density_sq_board324 = stone_density_sq(stone_board324)
    density_sq_board18x18 = line_to_table(density_sq_board324, 18)

    row_format = "{:>6.02f}" * 18
    for row in density_sq_board18x18:
        print(row_format.format(*row))

    print('Trace   | Finished.')


go()

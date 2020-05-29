from pytororo.pytororo import stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, print_cake_cover, convolute
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

    num_board17x17 = stone_density_node(stone_board1, 'x')

    print('Trace   | Finished.')


go()

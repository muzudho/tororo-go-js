from pytororo.pytororo import resize13to18str, stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, print_cake_cover, convolute
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
    board18 = resize13to18str(stone_board1, '.')
    # print(board18)
    # board18_text = ''.join(board18)
    # rows = [''.join(board18[i: i+18]) for i in range(0, len(board18), 18)]
    rows = [board18[i: i+18] for i in range(0, len(board18), 18)]
    # print(rows)
    board18_text = '\n'.join(rows)
    print(board18_text)

    """
    num_board17x17 = stone_density_node(stone_board1, 'x')
    """

    print('Trace   | Finished.')


go()

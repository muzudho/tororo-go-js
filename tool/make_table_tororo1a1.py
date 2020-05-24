from pytororo.pytororo import sticky_rice_cake, coordinate_under
from pytororo.pytororo import stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board


def go():
    print('Trace   | Start.')

    board = """\
........ooooo/
........ooooo/
o....xx...ooo/
.o....xx..ooo/
......xx..ooo/
.....xx..oooo/
xxxxxxxx.oooo/
xxxxxxxx...../
...xxxxx...../
...x.xxx...../
....xxxx...../
....xxxx...../
....xxxxxx.../
    """

    stone_board1 = stone_board(board)
    black_stone_board = black_stone(stone_board1)
    white_stone_board = white_stone(stone_board1)
    black_cake_board = sticky_rice_cake_board(black_stone_board)
    white_cake_board = sticky_rice_cake_board(white_stone_board)

    print('Trace   | Black-floor.')
    print_cake_board(black_stone_board, black_cake_board,
                     img_src='img/black-floor.png')

    print('Trace   | White-floor.')
    print_cake_board(white_stone_board, white_cake_board,
                     img_src='img/white-floor.png')

    print('Trace   | Finished.')


go()

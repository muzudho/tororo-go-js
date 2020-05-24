from pytororo.pytororo import stone_board, black_stone, white_stone, sticky_rice_cake, sticky_rice_cake_board, print_stone_board, print_cake_board, convolute, print_cake_cover


def go():
    print('Trace   | Start.')

    board = """\
........ooooo/
........ooooo/
o...xx....ooo/
.o...xx...ooo/
.....xx...ooo/
....xx...oooo/
xxxxxxx..oooo/
xxxxxxx....../
..xxxxx....../
..x.xxx....../
...xxxx....../
...xxxx....../
...xxxxxx..../
    """

    stone_board1 = stone_board(board)
    black_stone_board = black_stone(stone_board1)
    white_stone_board = white_stone(stone_board1)
    black_cake_board = sticky_rice_cake_board(black_stone_board)
    white_cake_board = sticky_rice_cake_board(white_stone_board)

    print('\nTrace   | Black-floor.\n')
    print_cake_board(black_stone_board, black_cake_board,
                     img_src='img/black-floor.png')

    print('\nTrace   | White-floor.\n')
    print_cake_board(white_stone_board, white_cake_board,
                     img_src='img/white-floor.png')

    print('\nTrace   | Black cake cover.\n')
    corners_board = convolute(black_cake_board)
    print_cake_cover(corners_board, 'black',
                     black_img_src='img/black-floor.png')

    print('\nTrace   | White cake cover.\n')
    corners_board = convolute(white_cake_board)
    print_cake_cover(corners_board, 'white',
                     white_img_src='img/white-floor.png')

    print('\nTrace   | Finished.\n')


go()

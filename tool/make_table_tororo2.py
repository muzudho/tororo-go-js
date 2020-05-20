from pytororo.pytororo import number


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

    for i, stone in enumerate(board_array):
        _, cover = number(board_array, i, stone)
        cover_p = coordinate_cover()
        # print(
        #    f'i={i} under=0x{under:02X} cover=0x{cover:02X} under_p0={under_p[0]} under_p1={under_p[1]}')
        if stone == '.':
            print('<img src="img/s.png">', end='')
        elif stone == "x":
            print(
                f'<img src="img/black-stone.png" style="object-fit: none; object-position:{cover_p[0]}px {cover_p[1]}px; width:40px; height:40px;">', end='')
        elif stone == "o":
            print(
                f'<img src="img/white-stone.png" style="object-fit: none; object-position:{cover_p[0]}px {cover_p[1]}px; width:40px; height:40px;">', end='')
        elif stone == "/":
            print('<br>')
        elif stone == " " or stone == "\n":
            pass
        else:
            print(f"[{stone}]?", end='')

    print('')  # New line.
    print('Trace   | Finished.')


def coordinate_cover():
    return (-180, -20)


go()

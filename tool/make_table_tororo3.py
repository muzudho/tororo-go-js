from pytororo.pytororo import resize13to18str, line_to_table_str, line_to_table, stone_board
from pytororo.search import stone_density_node, stone_density_sq, directed_stone_density_node, directed_stone_density_sq


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

    print('Trace   | 石密度node。')
    density_node_board324 = stone_density_node(stone_board324)
    # print(density_node_board324)
    density_node_board18x18 = line_to_table(density_node_board324, 18)
    # print(density_node_board18x18)

    row_format = "{:>6}" * 18
    for row in density_node_board18x18:
        print(row_format.format(*row))

    print('Trace   | 石密度sq。')
    density_sq_board324 = stone_density_sq(stone_board324)
    density_sq_board18x18 = line_to_table(density_sq_board324, 18)

    row_format = "{:>6.02f}" * 18
    for row in density_sq_board18x18:
        print(row_format.format(*row))

    ccw90 = 0
    print('Trace   | 東向き石密度node。')
    d_density_node_board324 = directed_stone_density_node(
        stone_board324, ccw90)
    d_density_node_board18x18 = line_to_table(d_density_node_board324, 18)

    row_format = "{:>6.02f}" * 18
    for row in d_density_node_board18x18:
        print(row_format.format(*row))

    print('Trace   | 東向き石密度sq。')
    d_density_sq_board324 = directed_stone_density_sq(
        stone_board324, ccw90)
    d_density_sq_board18x18 = line_to_table(d_density_sq_board324, 18)

    row_format = "{:>6.02f}" * 18
    for row in d_density_sq_board18x18:
        print(row_format.format(*row))

    print('Trace   | 北東向き石密度。')
    ccw90 = 1
    d_density_node_board324 = directed_stone_density_node(
        stone_board324, ccw90)
    d_density_node_board18x18 = line_to_table(d_density_node_board324, 18)

    row_format = "{:>6.02f}" * 18
    for row in d_density_node_board18x18:
        print(row_format.format(*row))

    print('Trace   | 連テスト。')
    scan_pure_board_with_dirty(lambda p: pass)

    print('Trace   | Finished.')


go()

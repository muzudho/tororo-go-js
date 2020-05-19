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

# print(board)

for stone in board:
    if stone == '.':
        print('<img src="img/s.png">', end='')
    elif stone == "x":
        print('<img src="img/b.png">', end='')
    elif stone == "o":
        print('<img src="img/w.png">', end='')
    elif stone == "/":
        print('<br>')
    elif stone == "\n":
        pass
    else:
        print(f"[{stone}]?", end='')

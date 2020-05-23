# 14パターンのヒモ。
himo13 = 0b00000101
himo14 = 0b00001001
himo15 = 0b00010001
himo16 = 0b00100001
himo17 = 0b01000001
himo25 = 0b00010010
himo27 = 0b01000010
himo35 = 0b00010100
himo36 = 0b00100100
himo37 = 0b01000100
himo38 = 0b10000100
himo47 = 0b01001000
himo57 = 0b01010000
himo58 = 0b10010000


def go():
    print('Trace   | Start.')

    for i in range(256):
        bit = f'{i:08b}'
        print(f'[{i:3}]   {bit[4]}{bit[5]}{bit[6]} check={check(i)}')
        print(f'        {bit[3]} {bit[7]}')
        print(f'        {bit[2]}{bit[1]}{bit[0]}')

    print('Trace   | Finish.')


def check(num):
    result = ''
    if num & himo13 == himo13:
        result += '[13]'

    if num & himo14 == himo14:
        result += '[14]'

    if num & himo15 == himo15:
        result += '[15]'

    if num & himo16 == himo16:
        result += '[16]'

    if num & himo17 == himo17:
        result += '[17]'

    if num & himo25 == himo25:
        result += '[25]'

    if num & himo27 == himo27:
        result += '[27]'

    if num & himo35 == himo35:
        result += '[35]'

    if num & himo36 == himo36:
        result += '[36]'

    if num & himo37 == himo37:
        result += '[37]'

    if num & himo38 == himo38:
        result += '[38]'

    if num & himo47 == himo47:
        result += '[47]'

    if num & himo57 == himo57:
        result += '[57]'

    if num & himo58 == himo58:
        result += '[58]'

    return result


go()

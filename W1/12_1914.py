move_arr = [None] * 101
txt_arr = [[[None, None, None] for _ in range(3)] for _ in range(21)]


def move(bottom, from_, to_):
    if txt_arr[bottom][from_ - 1][to_ - 1] != None:
        # print(bottom, from_, to_)
        # print(txt_arr[bottom][from_ - 1][to_ - 1])
        return move_arr[bottom], txt_arr[bottom][from_ - 1][to_ - 1]
    if bottom == 1:
        return 1, f"{from_} {to_}\n"
    between = 6 - from_ - to_

    # print(from_, between, to_)
    big_move1, text1 = move(bottom - 1, from_, between)
    big_move2, text2 = move(bottom - 1, between, to_)

    moved = big_move1 + 1 + big_move2
    text = text1 + f"{from_} {to_}\n" + text2

    move_arr[bottom] = moved

    txt_arr[bottom][from_ - 1][to_ - 1] = text

    return (moved, text)


def moveBig(bottom, from_, to_):
    if move_arr[bottom] != None:
        return move_arr[bottom]
    if bottom == 1:
        return 1
    between = 6 - from_ - to_

    # print(from_, between, to_)
    big_move1 = moveBig(bottom - 1, from_, between)
    big_move2 = moveBig(bottom - 1, between, to_)

    moved = big_move1 + 1 + big_move2
    move_arr[bottom] = moved

    return moved


got = int(input())
if got > 20:
    print(moveBig(got, 1, 3))
else:
    ret = move(got, 1, 3)
    print(f"{ret[0]}\n{ret[1]}", end="")

def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i, char in enumerate(game):
        if char == '/':
            result += 10 - last
        else:
            result += get_value(char)
        if frame < 10 and get_value(char) == 10:
            if char == '/':
                result += get_value(game[i+1])
            elif char == 'X' or char == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        last = get_value(char)
        if not in_first_half:
            frame += 1
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
        if char == 'X' or char == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):

    if char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    elif int(char) in range(1, 10):
        return int(char)
    else:
        raise ValueError()

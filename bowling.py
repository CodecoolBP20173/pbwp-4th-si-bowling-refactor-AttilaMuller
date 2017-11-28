def score(game):
    result = 0
    previous_score = 0
    frame = 1
    is_first_try = True
    for i, character in enumerate(game):
        if character == '/':
            result += 10 - previous_score
        else:
            result += get_value(character)
        if frame < 10 and get_value(character) == 10:
            if character == '/':
                result += get_value(game[i+1])
            elif character == 'X' or character == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])
        previous_score = get_value(character)
        if is_first_try is False:
            frame += 1
        if is_first_try is True:
            is_first_try = False
        else:
            is_first_try = True
        if character == 'X' or character == 'x':
            is_first_try = True
            frame += 1
    return result


def get_value(character):

    if character == 'X' or character == 'x' or character == '/':
        return 10
    elif character == '-':
        return 0
    elif int(character) in range(1, 10):
        return int(character)
    else:
        raise ValueError()

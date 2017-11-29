def score(game):

    ''' Calculates the score from the results of the player. '''

    result = 0
    frame = 1
    is_first_try = True

    for i, character in enumerate(game):

        if character == '/':  # Adds current try's value to result, in case of spare calculates actual try's value
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(character)

        if frame < 10 and get_value(character) == 10:  # Adds the extra points in case spare or strike
            if character == '/':
                result += get_value(game[i+1])
            elif character.lower() == 'x':
                result += get_value(game[i+1])
                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        if is_first_try is False:  # updates frame if it is the second try of the player
            frame += 1

        is_first_try = not is_first_try  # updates try for next loop

        if character.lower() == 'x':  # in case of a strike resets current try and adds a frame
            is_first_try = True
            frame += 1

    return result


def get_value(character):

    ''' Converts character into value. '''

    if character.lower() == 'x' or character == '/':
        return 10
    elif character == '-':
        return 0
    elif int(character) in range(1, 10):
        return int(character)
    else:
        raise ValueError()

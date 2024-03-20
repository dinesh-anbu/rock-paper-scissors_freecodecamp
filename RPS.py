def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    else:
        opponent_history.clear()

    counter = { 'R': 'P', 'P': 'S', 'S': 'R' }
    sol = "S"

    if len(opponent_history) >= 4:
        play_order = [ ''.join(opponent_history[k:k+4]) for k, v in enumerate(opponent_history[:-3]) ]

        potential_play = [ ''.join([ *opponent_history[-3:], v ]) for v in ['S', 'R', 'P'] ]

        sub_order = { k: play_order.count(k) for k in potential_play }

        pred = max(sub_order, key=sub_order.get)[-1]

        sol = counter[pred]

    return sol
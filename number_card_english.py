def Cards_number(points, card_random):

    if card_random == 2:
        points += 2
    elif card_random == 3:
        points += 3
    elif card_random == 4:
        points += 4
    elif card_random == 5:
        points += 5
    elif card_random == 6:
        points += 6
    elif card_random == 7:
        points += 7
    elif card_random == 8:
        points += 8
    elif card_random == 9:
        points += 9
    elif card_random == 10:
        points += 10
    elif card_random == "Jack":
        points += 10
    elif card_random == "Queen":
        points += 10
    elif card_random == "King":
        points += 10
    elif card_random == "Ace":
        points += 11
    return points
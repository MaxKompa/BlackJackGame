import random
import number_card_english

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]


def main():
    print("Welcome to the game of Blackjack")
    StartGame()


def StartGame():
    points_player = int(0)
    points_diller = int(0)

    name = str(input("Your name: "))
    print("Hello, " + name + ", let's play Blackjack")

    question = input("You ready?(Yes - y, or No - n): ")
    if question == "y" or question == "Yes":
        Game(points_player, points_diller)
    elif question == "n" or question == "No":
        exit()
    else:
        print("Try it again")
        StartGame()


def Game(points_player, points_diller):
    points = 0
    points_dill = 0

    #Handing out two open cards
    card_random = random.choice(cards)
    first_card = card_random
    card_random = random.choice(cards)
    second_card = card_random

    #Handing out cards to the dealer, one open, one not open
    card_random_diller = random.choice(cards)
    first_card_diller = card_random_diller
    card_random_diller = random.choice(cards)
    second_card_diller = card_random_diller

    #Points from the first card
    number = number_card_english.Cards_number(points, first_card)

    #Points from the first dealer card
    number_diller = number_card_english.Cards_number(points_dill, first_card_diller)

    #Points from the second card
    number2 = number_card_english.Cards_number(points, second_card)

    #Points from the second dealer's card, which is also a closed card
    number_diller2 = number_card_english.Cards_number(points_dill, second_card_diller)

    #Total player and dealer points
    points_player += number + number2
    points_diller += number_diller + number_diller2
    print("Your open first card: " + str(first_card) + "\nYour open second card: " + str(
        second_card) + "\nYour total score in the game: " + str(points_player))
    print("Dealer's first open card: " + str(first_card_diller) + "\nDealer's total score in the game: " + str(
        points_diller))

    print("To be continued?(Yes - y, or No - n): ")
    question = str(input())

    while question == "y" or question == "Yes" or question == "Get a card" or question == "Hit":
        points = 0
        points_dill = 0
        print("Your actions?(Get a card - Hit, Reject the card - Surrender): ")
        question = str(input())
        if question == "Get a card" or question == "Hit":
            card_random = random.choice(cards)
            number = number_card_english.Cards_number(points, card_random)
            points_player += number
            print("Your score in the game: " + str(points_player))
            if points_player > 21:
                print("You lost")
                print("Start again?(Yes - y, No - n): ")
                question = str(input())
                if question == "Yes" or question == "y":
                    main()
                elif question == "No" or question == "n":
                    exit()
        elif question == "Reject the card" or question == "Surrender":
            while points_diller < 17:
                card_random_diller = random.choice(cards)
                number_diller = number_card_english.Cards_number(points_dill, card_random_diller)
                points_diller += number_diller
            print("Your score in the game: " + str(points_player) + "\nDealer's score in the game: " + str(points_diller))
            if points_player < points_diller or points_player > 21 or points_player < points_diller and points_player > 21:
                print("You lost, the dealer won")
                print("Start again?(Yes - y, No - n): ")
                question = str(input())
                if question == "Yes" or question == "y":
                    main()
                elif question == "No" or question == "n":
                    exit()
            elif points_player > points_diller or points_player <= 21 or points_diller > 21 or points_diller > 21 and points_player < points_diller:
                print("Congratulations, you won, the dealer lost")
                print("Start again?(Yes - y, No - n): ")
                question = str(input())
                if question == "Yes" or question == "y":
                    main()
                elif question == "No" or question == "n":
                    exit()
            elif points_player == points_diller:
                print("Tie")
                print("Start again?(Yes - y, No - n): ")
                question = str(input())
                if question == "Yes" or question == "y":
                    main()
                elif question == "No" or question == "n":
                    exit()

    if points_player < points_diller or points_player > 21 or points_player < points_diller and points_player > 21:
        print("You lost, the dealer won")
        print("Start again?(Yes - y, No - n): ")
        question = str(input())
        if question == "Yes" or question == "y":
            main()
        elif question == "No" or question == "n":
            exit()
    elif points_player > points_diller or points_player <= 21 or points_diller > 21 or points_diller > 21 and points_player < points_diller:
        print("Congratulations, you won, the dealer lost")
        print("Start again?(Yes - y, No - n): ")
        question = str(input())
        if question == "Yes" or question == "y":
            main()
        elif question == "No" or question == "n":
            exit()
    elif points_player == points_diller:
        print("Tie")
        print("Start again?(Yes - y, No - n): ")
        question = str(input())
        if question == "Yes" or question == "y":
            main()
        elif question == "No" or question == "n":
            exit()


main()
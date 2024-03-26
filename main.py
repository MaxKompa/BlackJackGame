import random
import number_card

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Валет", "Валет", "Валет", "Валет", "Дама", "Дама", "Дама", "Дама", "Король", "Король", "Король", "Король", "Туз", "Туз", "Туз", "Туз"]

def main():
    print("Добро пожаловать в игру Блэк-джек")
    StartGame()

def StartGame():
    points_player = int(0)
    points_diller = int(0)



    name = str(input("Назовите своё имя: "))
    print("Здравствуй, " + name + ", давай сыграем в Блэк-джек")


    question = input("Ты хочешь сыграть?(Да - д, or Нет - н): ")
    if question == "д" or question == "Да":
        Game(points_player, points_diller)
    elif question == "н" or question == "Нет":
        exit()
    else:
        print("Попробуй, ещё раз")
        StartGame()



def Game(points_player, points_diller):
    points = 0
    points_dill = 0

    #Раздача двух открытых карт
    card_random = random.choice(cards)
    first_card = card_random
    card_random = random.choice(cards)
    second_card = card_random

    #Раздача карт диллеру, одна открытая, другая нет
    card_random_diller = random.choice(cards)
    first_card_diller = card_random_diller
    card_random_diller = random.choice(cards)
    second_card_diller = card_random_diller

    #Очки с первой карты
    number = number_card.Cards_number(points, first_card)

    #Очки с первой карты диллера
    number_diller = number_card.Cards_number(points_dill, first_card_diller)

    # Очки со второй карты
    number2 = number_card.Cards_number(points, second_card)

    #Очки со второй карты диллера, она же и закрытая
    number_diller2 = number_card.Cards_number(points_dill, second_card_diller)

    #Общие очки игрока и диллера
    points_player += number + number2
    points_diller += number_diller + number_diller2
    print("Ваша открытая первая карта: " + str(first_card) + "\nВаша открытая вторая карта: " + str(second_card) + "\nВаш счёт в игре: " + str(points_player))
    print("Первая открытая карта диллера: " + str(first_card_diller) + "\nОбщий счёт диллера в игре: " + str(points_diller))

    print("Продолжить?(Да - д, or Нет - н): ")
    question = str(input())

    while question == "д" or question == "Да" or question == "Взять карту" or question == "Hit":
        points = 0
        points_dill = 0
        print("Ваши действия?(Взять карту - Hit, Отказаться от карты - Surrender): ")
        question = str(input())
        if question == "Взять карту" or question == "Hit":
            card_random = random.choice(cards)
            number = number_card.Cards_number(points, card_random)
            points_player += number
            print("Ваш счёт: " + str(points_player))
            if points_player > 21:
                print("Вы проиграли")
                print("Начать заново?(Да - д, Нет - н): ")
                question = str(input())
                if question == "Да" or question == "д":
                    main()
                elif question == "Нет" or question == "н":
                    exit()
        elif question == "Отказаться от карты" or question == "Surrender":
            while points_diller < 17:
                card_random_diller = random.choice(cards)
                number_diller = number_card.Cards_number(points_dill, card_random_diller)
                points_diller += number_diller
            print("Ваш счёт: " + str(points_player) + "\nСчёт диллера: " + str(points_diller))
            if points_player < points_diller or points_player > 21 or points_player < points_diller and points_player > 21:
                print("Вы проиграли, диллер выиграл")
                print("Начать заново?(Да - д, Нет - н): ")
                question = str(input())
                if question == "Да" or question == "д":
                    main()
                elif question == "Нет" or question == "н":
                    exit()
            elif points_player > points_diller or points_player <= 21 or points_diller > 21 or points_diller > 21 and points_player < points_diller:
                print("Поздравляю, вы выиграли, диллер проиграл")
                print("Начать заново?(Да - д, Нет - н): ")
                question = str(input())
                if question == "Да" or question == "д":
                    main()
                elif question == "Нет" or question == "н":
                    exit()
            elif points_player == points_diller:
                print("Ничья")
                print("Начать заново?(Да - д, Нет - н): ")
                question = str(input())
                if question == "Да" or question == "д":
                    main()
                elif question == "Нет" or question == "н":
                    exit()

    if points_player < points_diller or points_player > 21 or points_player < points_diller and points_player > 21:
        print("Вы проиграли, диллер выиграл")
        print("Начать заново?(Да - д, Нет - н): ")
        question = str(input())
        if question == "Да" or question == "д":
            main()
        elif question == "Нет" or question == "н":
            exit()
    elif points_player > points_diller or points_player <= 21 or points_diller > 21 or points_diller > 21 and points_player < points_diller:
        print("Поздравляю, вы выиграли, диллер проиграл")
        print("Начать заново?(Да - д, Нет - н): ")
        question = str(input())
        if question == "Да" or question == "д":
            main()
        elif question == "Нет" or question == "н":
            exit()
    elif points_player == points_diller:
        print("Ничья")
        print("Начать заново?(Да - д, Нет - н): ")
        question = str(input())
        if question == "Да" or question == "д":
            main()
        elif question == "Нет" or question == "н":
            exit()

    

main()
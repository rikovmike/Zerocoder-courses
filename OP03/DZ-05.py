import random


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def get_player_choice():
    choice = input("Выберите: камень, ножницы или бумага: ").lower()
    while choice not in ["камень", "ножницы", "бумага"]:
        choice = input("Некорректный ввод. Попробуйте снова: камень, ножницы или бумага: ").lower()
    return choice


def determine_winner(player, computer):
    if player == computer:
        return "ничья"
    elif (player == "камень" and computer == "ножницы") or \
            (player == "ножницы" and computer == "бумага") or \
            (player == "бумага" and computer == "камень"):
        return "игрок"
    else:
        return "компьютер"


def main():
    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        print("\nТекущий счет - Игрок: {}, Компьютер: {}".format(player_score, computer_score))

        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print("Компьютер выбрал:", computer_choice)

        winner = determine_winner(player_choice, computer_choice)

        if winner == "игрок":
            player_score += 1
            print("Вы выиграли этот раунд!")
        elif winner == "компьютер":
            computer_score += 1
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд закончился вничью!")

    if player_score == 3:
        print("\nПоздравляем! Вы победили!")
    else:
        print("\nКомпьютер победил! Попробуйте снова!")


if __name__ == "__main__":
    main()
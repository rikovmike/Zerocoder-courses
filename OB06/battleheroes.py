import random


class Hero:
    def __init__(self, name, health=100, attack_power=20, difficulty=1):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.difficulty = difficulty  # Уровень сложности для компьютера (влияние на здоровье и силу атаки)

    def attack(self, other):
        """Атакует другого героя, уменьшая его здоровье на значение своей силы удара."""
        damage = self.attack_power
        # Вероятность критического удара
        if random.random() < 0.2:  # 20% шанс на критический удар
            damage *= 2  # Урон удваивается при критическом ударе
            print(f"Критический удар! Урон удвоен до {damage}")
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        """Возвращает True, если герой жив, иначе False."""
        return self.health > 0

    def get_status(self):
        """Возвращает строку с информацией о текущем здоровье героя."""
        return f"{self.name}: {self.health} HP"

    def level_up(self):
        """Улучшение героя. Увеличение здоровья и силы удара."""
        self.health += 20
        self.attack_power += 5
        print(
            f"{self.name} улучшил свои характеристики! Теперь у него {self.health} HP и сила удара {self.attack_power}.")

    def increase_difficulty(self, difficulty_level):
        """Увеличение сложности для компьютера: увеличение здоровья и силы удара."""
        self.difficulty = difficulty_level
        self.health += difficulty_level * 20  # Увеличиваем здоровье
        self.attack_power += difficulty_level * 5  # Увеличиваем силу удара
        print(f"{self.name} стал сильнее! Теперь у него {self.health} HP и сила удара {self.attack_power}.")


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        """Запускает игру, чередует ходы игрока и компьютера, пока кто-то не погибнет."""
        print("Игра начинается!")
        print(f"Сложность игры: {self.computer.difficulty} (для компьютера)")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} проиграл! {self.player.name} победил!")
                break

            # Ход компьютера
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} проиграл! {self.computer.name} победил!")
                break

    def player_turn(self):
        """Ход игрока. Игрок атакует."""
        print(self.player.get_status())
        print(self.computer.get_status())
        input("Нажмите Enter, чтобы атаковать!")
        self.player.attack(self.computer)
        print(self.computer.get_status())
        self.check_level_up(self.player)

    def computer_turn(self):
        """Ход компьютера. Компьютер атакует."""
        print(self.player.get_status())
        print(self.computer.get_status())
        print("Ход компьютера...")
        self.computer.attack(self.player)
        print(self.player.get_status())
        self.check_level_up(self.computer)

    def check_level_up(self, hero):
        """Проверяет, стоит ли улучшить героя после каждого хода."""
        if hero.health <= 50 and random.random() < 0.3:  # 30% шанс на улучшение при здоровье ниже 50
            hero.level_up()

        # Увеличение сложности для компьютера
        if isinstance(hero, Hero) and hero.name == "Компьютер":
            if hero.health <= 50 and random.random() < 0.3:  # 30% шанс для компьютера улучшиться
                hero.increase_difficulty(hero.difficulty + 1)


def main():
    # Выбор сложности для игры
    print("Выберите сложность игры:")
    print("1. Легкий")
    print("2. Средний")
    print("3. Сложный")

    difficulty = int(input("Введите номер сложности (1-3): "))
    while difficulty not in [1, 2, 3]:
        difficulty = int(input("Некорректный ввод. Введите номер сложности (1-3): "))

    # Создание персонажей
    player_name = input("Введите имя игрока: ")
    player = Hero(name=player_name, health=100, attack_power=20)

    # Создание компьютера с заданным уровнем сложности
    if difficulty == 1:
        computer = Hero(name="Компьютер", health=100, attack_power=15, difficulty=1)
    elif difficulty == 2:
        computer = Hero(name="Компьютер", health=150, attack_power=20, difficulty=2)
    elif difficulty == 3:
        computer = Hero(name="Компьютер", health=200, attack_power=25, difficulty=3)

    # Создание игры
    game = Game(player, computer)

    # Запуск игры
    game.start()


if __name__ == "__main__":
    main()

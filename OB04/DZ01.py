# Игра дополнена элементами интерактива:
# - здоровье и смерть игрока
# - ответная атака монстра
# - мощность оружия и девиации в ней
# - генерация имени монстров


import json
from abc import ABC, abstractmethod
import random
from time import sleep


# Шаг 1: Создаем абстрактный класс Weapon
class Weapon(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_attack_power(self):
        pass

# Шаг 2: Реализуем конкретные типы оружия
class Sword(Weapon):
    def __init__(self):
        super().__init__("Меч")
    def attack(self):
        return "Боец наносит удар мечом."

    def get_attack_power(self):
        return 5  # Мощность атаки меча

class Bow(Weapon):
    def __init__(self):
        super().__init__("Лук")

    def attack(self):
        return "Боец наносит удар из лука."

    def get_attack_power(self):
        return 3  # Мощность атаки лука

# Класс Monster
class Monster:
    def __init__(self, health,name):
        self.health = health
        self.name=name

    def take_damage(self, damage):
        self.health -= damage
        if self.health <0: self.health=0
        print(f"{self.name} получает {damage} урона! Осталось здоровья: {self.health}")

    def get_name(self):
        return self.name

    def is_defeated(self):
        return self.health <= 0

    def attack(self):
        # Случайный урон от монстра от 0 до 2
        damage = random.randint(0, 2)
        return damage

# Шаг 3: Модифицируем класс Fighter
class Fighter:
    def __init__(self, name, health, weapon: Weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} меняет оружие на {self.weapon.get_name()}.")

    def attack(self, monster: Monster):
        print(self.weapon.attack())
        # Случайное отклонение от 80% до 120% от мощности атаки
        deviation = random.uniform(0.8, 1.2)
        damage = int(self.weapon.get_attack_power() * deviation)
        monster.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает {damage} урона! Осталось здоровья: {self.health}.")
        if self.health <= 0:
            self.health=0
            self.die()

    def die(self):
        print(f"{self.name} погиб!")

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    while not monster.is_defeated() and fighter.health > 0:
        fighter.attack(monster)
        sleep(0.5)
        if not monster.is_defeated():
            # Монстр атакует бойца
            damage = monster.attack()
            fighter.take_damage(damage)
            print(f"{monster.get_name()} атакует {fighter.name} и наносит {damage} урона.")
            sleep(0.5)
    if monster.is_defeated():
        print("Монстр побежден!")
        sleep(0.5)


def generate_monster_name(monsternames):
    monstername=" ".join((random.choice(monsternames["first"]),random.choice(monsternames["second"])))
    if random.choice((0,1)) == 1:
        monstername+=" "+random.choice(monsternames["third"])
    return monstername

# Демонстрация работы
if __name__ == "__main__":

    with open("monster_names_db.json", "r", encoding="utf-8") as file:
        monsternames = json.load(file)

    # Создаем бойца с мечом
    fighter = Fighter("Боец", 10, Sword())
    monster = Monster(random.randint(5, 20),generate_monster_name(monsternames))


    # Цикл для выбора оружия и боя
    while True:
        print(f"\nВас атакует {monster.get_name()}:")
        print("Выберите оружие:")
        print("1. Меч")
        print("2. Лук")
        print("0. Выйти из игры")

        choice = input("Ваш выбор: ")

        if choice == '1':
            fighter.change_weapon(Sword())
        elif choice == '2':
            fighter.change_weapon(Bow())
        elif choice == '0':
            print("Спасибо за игру!")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")
            continue

        print(f"\n{fighter.name} выбирает {fighter.weapon.get_name()}.")
        battle(fighter, monster)

        # Проверяем, жив ли игрок после боя
        if fighter.health <= 0:
            print(f"{fighter.name} не сможет продолжать борьбу.")
            break

        # Сбрасываем здоровье монстра для следующего боя
        monster = Monster(random.randint(5, 20),generate_monster_name(monsternames))
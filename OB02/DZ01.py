class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id  # Приватный атрибут
        self.__name = name  # Приватный атрибут
        self.__access_level = access_level  # Приватный атрибут

    # Методы для получения значений атрибутов
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Методы для изменения значений атрибутов
    def set_name(self, new_name):
        self.__name = new_name

    def set_access_level(self, new_access_level):
        if new_access_level in ['user', 'admin']:
            self.__access_level = new_access_level
        else:
            print("Недопустимый уровень доступа.")

    def __str__(self):
        return f"ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__users_list = []  # Приватный атрибут для списка пользователей

    # Метод для добавления пользователя
    def add_user(self, user):
        if isinstance(user, User):
            self.__users_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен в систему.")
        else:
            print("Можно добавлять только пользователей.")

    # Метод для удаления пользователя
    def remove_user(self, user_id):
        for user in self.__users_list:
            if user.get_user_id() == user_id:
                self.__users_list.remove(user)
                print(f"Пользователь с ID {user_id} удален из системы.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    # Метод для вывода списка пользователей
    def list_users(self):
        if self.__users_list:
            print("Список пользователей:")
            for user in self.__users_list:
                print(user)
        else:
            print("Список пользователей пуст.")

    def __str__(self):
        return f"Администратор: {self.get_name()}, ID: {self.get_user_id()}, Access Level: {self.get_access_level()}"


# Пример использования
admin = Admin(1, "Alice")
user1 = User(2, "Bob")
user2 = User(3, "Charlie")

admin.add_user(user1)
admin.add_user(user2)

admin.list_users()

admin.remove_user(2)
admin.list_users()

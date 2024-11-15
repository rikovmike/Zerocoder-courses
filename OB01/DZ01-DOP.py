class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина, если он существует."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара. Если товар отсутствует, выводит сообщение."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def display_items(self):
        """Выводит все товары и их цены."""
        if not self.items:
            print(f"Ассортимент магазина `{self.name}` пуст.")
        else:
            print(f"Ассортимент магазина `{self.name}`:")
            for item, price in self.items.items():
                print(f"{item}: {price:.2f} руб.")


if __name__ == "__main__":

    stores=[]
    stores.append(Store("Магазин свежих продуктов", "Улица 1, дом 2"))
    stores.append(Store("Магазин мясной", "Мясная площадь, дом 1"))
    stores.append(Store("Магазин скриптов", "Питоновский проезд, дом 13"))

    # Добавляем товары
    stores[0].add_item("яблоки", 50)
    stores[0].add_item("бананы", 75)

    # Отображаем ассортимент
    stores[0].display_items()

    # Получаем цену товара
    print("Цена яблок:", stores[0].get_price("яблоки")," руб.")

    # Обновляем цену товара
    stores[0].update_price("яблоки", 60)
    print("Обновленная цена яблок:", stores[0].get_price("яблоки")," руб.")

    # Удаляем товар
    stores[0].remove_item("бананы")

    # Отображаем ассортимент после удаления товара
    stores[0].display_items()
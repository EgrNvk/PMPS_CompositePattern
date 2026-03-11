from abc import ABC, abstractmethod

class MenuComponent(ABC):

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def show(self):
        pass

class MenuItem(MenuComponent):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show(self):
        print("\t",self.name, "-", self.price, "грн")


class MenuSet(MenuComponent):

    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component):
        self.items.append(component)

    def get_price(self):
        total = 0
        for item in self.items:
            total += item.get_price()
        return total

    def show(self):
        print("Набір:", self.name)

        for item in self.items:
            item.show()

        print("Разом:", self.get_price(), "грн")


espresso = MenuItem("Еспресо", 50)
latte = MenuItem("Латте", 70)
croissant = MenuItem("Круасан", 60)
cheesecake = MenuItem("Чизкейк", 90)

breakfast_set = MenuSet("Сніданок")
breakfast_set.add(espresso)
breakfast_set.add(croissant)
breakfast_set.show()
print("="*30)

dessert_set = MenuSet("Десертний набір")
dessert_set.add(latte)
dessert_set.add(cheesecake)
dessert_set.show()
print("="*30)

big_breakfast = MenuSet("Cніданок на двох")
big_breakfast.add(breakfast_set)
big_breakfast.add(dessert_set)
big_breakfast.show()
print("="*30)
from abc import ABC,abstractmethod



class Product(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
class Sushi(Product):
    @property
    def name(self):
        return 'Суши'

class Burger(Product):
    @property
    def name(self):
        return 'Бургер'

class OrderBuilder(ABC):

    @abstractmethod
    def serve(self):
        pass

    @abstractmethod
    def pack(self):
        pass

    @abstractmethod
    def add_cutlery(self,cutlery):
        pass

    @abstractmethod
    def add_topings(self):
        pass

    @abstractmethod
    def add_gloves(self):
        pass

    @abstractmethod
    def get_ready_order(self)->Product:
        pass

class SushiOrderBuilder(OrderBuilder):
    def serve(self):
        print('Делаем роллы')

    def pack(self):
        print('Упаковываем суши в контейнер')

    def add_cutlery(self,cutlery='Палочки'):
        print(f'Кладем {cutlery}')
    def add_topings(self):
        print('кладем соевый соус')
    def get_ready_order(self) ->Product:
        return Sushi()

    def add_gloves(self):
        pass
class BurgerOrderBuilder(OrderBuilder):
    def serve(self):
        print('Делаем бургер')

    def pack(self):
        print('Упаковываем бургер в бумагу')

    def add_cutlery(self):
        pass
    def add_topings(self):
        print('кладем доп котлету')
    def get_ready_order(self) ->Product:
        return Burger()
    def add_gloves(self):
        print('Кладем перчатки')

class Director:
    def __init__(self,orderbuilder:OrderBuilder):
        self.orderbuilder=orderbuilder

    def pack_sushi(self):
        self.orderbuilder.serve()
        self.orderbuilder.add_topings()
        self.orderbuilder.add_cutlery()
        self.orderbuilder.pack()
        return self.orderbuilder.get_ready_order()
    def pack_burger(self):
        self.orderbuilder.serve()
        self.orderbuilder.add_topings()
        self.orderbuilder.add_gloves()
        self.orderbuilder.pack()
        return self.orderbuilder.get_ready_order()

d=Director(BurgerOrderBuilder())
order=d.pack_burger()

d=Director(SushiOrderBuilder())
order=d.pack_burger()
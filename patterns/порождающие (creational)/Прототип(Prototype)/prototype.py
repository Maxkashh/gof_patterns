# Шаблон проектирования Прототип (Prototype) в Python является частью творческого шаблона проектирования.
# Его основная цель — сократить количество классов для приложения.
# Он предоставляет возможность создать копию существующего объекта независимо от фактической реализации его классов, проще говоря,
# вновь созданный объект требует больше ресурсов, чем мы хотим использовать или иметь в наличии, поэтому мы создаем точную копию доступного объекта.
#
# Например, файл скачан с большого сервера, но он уже есть в памяти, мы могли бы его клонировать и работать над новой копией оригинала.
#
# Шаблон проектирования прототипа играет важную роль, когда формирование объекта весьма удобно с точки зрения использования времени и ресурсов.
# Мы можем получить копию исходного объекта и изменить ее в соответствии с нашими потребностями.
import copy
import datetime
from abc import ABC, abstractmethod
import time


# Class Creation
class Prototype(ABC):
    # Constructor:
    def __init__(self):
        # Mocking an expensive call
        time.sleep(3)
        # Base attributes
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None

    # Clone Method:
    @abstractmethod
    def clone(self):
        pass
class Shopkeeper(Prototype):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        # Mock expensive call
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        # Subclass-specific Attribute
        self.charisma = 30

    # Overwriting Cloning Method:
    def clone(self):
        return copy.deepcopy(self)


class Warrior(Prototype):
    def __init__(self, height, age, defense, attack):
        # Call superclass constructor, time.sleep() and assign base values
        # Concrete class attribute
        self.stamina = 60
    # Overwriting Cloning Method
    def clone(self):
        return copy.deepcopy(self)


class Mage(Prototype):
    def __init__(self, height, age, defense, attack):

    # Call superclass constructor, time.sleep() and assign base values
     self.mana = 100

    # Overwriting Cloning Method


    def clone(self):
        return copy.deepcopy(self)


print('Instantiating 1000 NPCs: ', datetime.datetime.now().time())
shopkeeper_template = Shopkeeper(180, 22, 5, 8)
warrior_template = Warrior(185, 22, 4, 21)
mage_template = Mage(172, 65, 8, 15)
for i in range(333):
    shopkeeper_clone = shopkeeper_template.clone()
    warrior_clone = warrior_template.clone()
    mage_clone = mage_template.clone()
    print(f'Finished creating NPC trio clone {i} at: ', datetime.datetime.now().time())
print('Finished instantiating NPC population at: ', datetime.datetime.now().time())
class AbstractFigure():
    """Общая реализация Фигуры"""
    def __init__(self, ImplementColoRClass):
        self.bridge_color = ImplementColoRClass



class Circle(AbstractFigure):
    """Реализация круга"""
    def draw(self):
        print(f"Нарисовать  Круг цветом {self.bridge_color.color}")


class Square(AbstractFigure):
    """Реализация квадрата"""
    def draw(self):
        print(f"Нарисовать  Квадрат цветом {self.bridge_color.color}")


class AbstractLine():
    """ Вынесенные в отдельный класс манипуляции с цветом для разгрузки основного  класса AbstractFigure
        для упрощения и более гибкой работы. В данном контексте является мостом для работы с цветом у класса AbstractFigure.
    """
    def __init__(self):
        self.color = "White"

    def info_color(self):
        print(f"My color {self.color}")


class BlueLine(AbstractLine):
    """ Реализация  Голубого цвета """
    def __init__(self):
        super().__init__()
        self.color = "Blue"


class RedLine(AbstractLine):
    """ Реализация  Красного цвета """
    def __init__(self):
        super().__init__()
        self.color = "Red"


class GreenLine(AbstractLine):
    def __init__(self):
        super().__init__()
        self.color = "Green"



if __name__ == '__main__':

    red_squar=Square(RedLine())
    red_squar.draw()
    blue_squar = Square(BlueLine())
    blue_squar.draw()
    red_circle=Circle(RedLine())
    red_circle.draw()
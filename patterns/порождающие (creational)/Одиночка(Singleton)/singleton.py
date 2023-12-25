

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance=super().__new__(cls)
        return cls.instance

class SingletonAnother:
    __inst=None
    def __new__(cls, *args, **kwargs):
        if cls.__inst is None:
            cls.__inst=super().__new__(cls)
        return cls.__inst

o1=Singleton()
o2=Singleton()
print(id(o1))
print(id(o2))

o1=SingletonAnother()
o2=SingletonAnother()
print(id(o1))
print(id(o2))
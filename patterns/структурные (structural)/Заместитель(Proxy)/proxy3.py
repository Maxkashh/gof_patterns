import abc
import random


class AbstractClass(metaclass=abc.ABCMeta):
    """ interface for real and proxy object """

    @abc.abstractmethod
    def sort_digits(self, reverse=False):
        pass


class RealClass(AbstractClass):
    """ RealClass that holds a larger object """

    def __init__(self):
        self.digits = []

        for i in range(1000000):
            self.digits.append(random.random())

    def sort_digits(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()


class ProxyClass(AbstractClass):
    """ A proxy class that has the same interface as RealClass. """

    ref_count = 0

    def __init__(self):
        """ Creates an object if it doesn't exist and caches it otherwise """

        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealClass()
            print('New object generated')
        else:
            print('Using cached object')

        self.__class__.ref_count += 1
        print('Reference Count:', self.__class__.ref_count)

    def sort_digits(self, reverse=False):
        print('Sort method')
        print(locals().items())

        # invokes the sort_digits method of real class
        self.__class__.cached_object.sort_digits(reverse=reverse)

    def __del__(self):
        """ Delete the object when the number of reference is 0 """
        self.__class__.ref_count -= 1

        if self.__class__.ref_count == 0:
            print('Deleting cached object')
            del self.__class__.cached_object

        print('Reference Count:', self.__class__.ref_count)


if __name__ == '__main__':
    proxA = ProxyClass()
    print()

    proxB = ProxyClass()
    print()

    proxC = ProxyClass()
    print()

    proxA.sort_digits(reverse=True)
    print()

    print('Deleting proxA')
    del proxA

    print('Deleting proxB')
    del proxB

    print('Deleting proxC')
    del proxC

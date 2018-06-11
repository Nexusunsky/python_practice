# Abs base class
import abc
from abc import ABC


class Clam(object):
    pass


class Talker(ABC):
    @abc.abstractmethod
    def talk(self):
        pass


class Knigget(Talker):

    def talk(self):
        pass


if __name__ == '__main__':
    Talker.register(Clam)
    print(issubclass(Clam, Talker))
    Clam().talk()

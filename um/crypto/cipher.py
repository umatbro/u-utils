from abc import ABCMeta, abstractmethod


class Cipher(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def encode(self):
        raise NotImplementedError

    @abstractmethod
    def decode():
        raise NotImplementedError

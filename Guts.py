import random

class guts:

    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def __str__(self):
        returnString = str(random.randint(1, self.get_size()))
        return returnString

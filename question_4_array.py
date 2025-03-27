from abc import ABC,abstractmethod

class Array(ABC):
    def __init__(self):
        self.next_equation = None
        self.number_array = []

    def set_next(self, equation):
        self.next_equation = equation

    @abstractmethod
    def equation(self):
        pass

    def next_equation(self):
        if self.next_equation:
            self.next_equation.number_array = self.number_array
            self.next_equation.equation()
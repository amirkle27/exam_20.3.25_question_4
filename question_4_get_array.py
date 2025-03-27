from question_4_array import Array
from typing import override
import random

class GetArray(Array):

    def get_array(self):
        numbers = input("Please enter an array of numbers or press [A] if you want the system to do it for you Automatically")
        if numbers.lower() == 'a':
            self.number_array = [random.randint(1, 100) for _ in range(10)]
        else:
            self.number_array = [int(num.strip()) for num in numbers.split(',')]
        print(f" Initial Array:  {self.number_array}\n")
        Array.next_equation(self)

    @override
    def equation(self):
        pass

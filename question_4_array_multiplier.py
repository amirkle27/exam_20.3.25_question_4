from question_4_array import Array
from typing import override
import random

class ArrayMultiplier(Array):

    @override
    def equation(self):
        multiply = input("Would you like to multiply the numbers? [Y/N]")
        if multiply.lower() in ['y','yes']:
            multiplication_factor = input("Please enter a multiplication_factor for the numbers in the array press [A] if you want the system to do it for you Automatically")
            if multiplication_factor.lower() == 'a':
                multiplication_factor = random.randint(1, 10)
            multiplication_factor = int(multiplication_factor)
            self.number_array = [num * multiplication_factor for num in self.number_array]
            print(f"\n - Multiplexed numbers by {multiplication_factor}:  {self.number_array}")
        Array.next_equation(self)
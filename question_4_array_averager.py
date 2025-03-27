from question_4_array import Array
from typing import override

class ArrayAverager(Array):
    @override
    def equation(self):
        multiply = input("Would you like to calculate an average for the numbers? [Y/N]")
        if multiply.lower() in ['y', 'yes']:
            average_calc = sum(num for num in self.number_array) / len(self.number_array)
            print(f"\n - Average number for {self.number_array}:  {average_calc:.2f}")
        else:
            Array.next_equation(self)
        Array.next_equation(self)
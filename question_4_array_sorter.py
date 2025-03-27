from question_4_array import Array
from typing import override

class ArraySorter(Array):
    def __init__(self):
        super().__init__()

    @override
    def equation(self):
        sort = input("Would you like to sort the numbers in the array? [Y/N]")
        if sort.lower() in ['y','yes']:
            self.number_array = sorted(self.number_array)
            print(f"\n Sorted numbers:  {self.number_array}")
        Array.next_equation(self)
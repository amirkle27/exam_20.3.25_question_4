from typing import override
from question_4_array import Array
import statistics

class ArraySTD(Array):
    def __init__(self):
        super().__init__()
        self.std_deviation = None

    @override
    def equation(self):
        std = input("Would you like to see an STD for the array? [Y/N]")
        if std.lower() in ['y', 'yes']:
            if len(self.number_array) > 1:
                self.std_deviation = statistics.stdev(self.number_array)
                print(f"\n - Standard deviation: {self.std_deviation:.2f}\n")
            else:
                print(f"\n - Cannot calculate standard deviation with less than 2 numbers")
            print(f"\n - Final array: {self.number_array}\n\n")
        print("End of program.\n Thank you so much, and May The Force Be With You!")
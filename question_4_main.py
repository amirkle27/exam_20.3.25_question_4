from question_4_get_array import GetArray
from question_4_array_sorter import ArraySorter
from question_4_array_multiplier import ArrayMultiplier
from question_4_array_averager import ArrayAverager
from question_4_array_std import ArraySTD



get_array = GetArray()
sorter = ArraySorter()
multiplier = ArrayMultiplier()
averager = ArrayAverager()
std = ArraySTD()

get_array.set_next(sorter)
sorter.set_next(multiplier)
multiplier.set_next(averager)
averager.set_next(std)

if __name__ == "__main__":
    get_array.get_array()
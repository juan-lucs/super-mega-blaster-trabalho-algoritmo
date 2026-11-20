#!/usr/bin/env python3

import random

random_list = random.sample(range(101), 30)

def bin_search(numbers: list, value: int) -> int:
    if (value >= numbers[0] and value <= numbers[len(numbers)-1]) and len(numbers) > 1:
        return rbin_search(numbers, value)
    else:
        return 0

def rbin_search(numbers: list, value: int) -> int:
    length = len(numbers) // 2
    position = length - 1
    while value != numbers[position] and (position > 0 and position < len(numbers) - 1):
        if length > 1:
            length //= 2
        if value == numbers[position]:
            return position
        elif value > numbers[position]:
            position += length
        else:
            position -= length
    return position

lista = [1,1,3,7,9,11,12,17,19,24]

print(bin_search(lista, 7))

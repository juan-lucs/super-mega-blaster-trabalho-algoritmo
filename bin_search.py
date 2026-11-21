#!/usr/bin/env python3

import random

random_list = random.sample(range(101), 31)

def selection_sort(numbers: list) -> list:
    for i in range(len(numbers)-1):
        smallest = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[smallest]:
                smallest = j
        if i == smallest:
            continue
        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]
    return numbers

def insertion_sort(numbers: list) -> list:
    for i in range(1, len(numbers)):
        for j in range(i-1, -1, -1):
            if numbers[j] > numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i -= 1
    return numbers

def merge_sort(numbers: list, length: int) -> list:
    if length <= 1:
        return numbers
    else:
        half_length = length // 2
        first_half = merge_sort(numbers[0:half_length], half_length)
        second_half = merge_sort(numbers[half_length:length], length - half_length)
        new_piece = []
        i = 0
        j = 0
        while i <= (half_length - 1) and j <= (length - half_length) - 1:
            if first_half[i] < second_half[j]:
                new_piece.append(first_half[i])
                i += 1
            else:
                new_piece.append(second_half[j])
                j += 1
        if i >= half_length:
            for index in range(j, length - half_length):
                new_piece.append(second_half[index])
        else:
            for index in range(i, half_length):
                new_piece.append(first_half[index])
        return new_piece

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

print(random_list)
print(len(random_list))
print(merge_sort(random_list, len(random_list)))

#!/usr/bin/env python3
import random

lista = [42, 15, 8, 23, 4, 16, 99, 1]

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
        min = numbers[i]
        for j in range(i-1, -1, -1):
            if min < numbers[j]:
                numbers[i] = numbers[j]
                i -= 1
            else:
                break
        numbers[i] = min

    return numbers

def merge_sort(numbers: list) -> list:
    length = len(numbers)
    if length <= 1:
        return numbers
    else:
        half_length = length // 2
        first_half = merge_sort(numbers[0:half_length])
        second_half = merge_sort(numbers[half_length:length])
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

print(insertion_sort(lista))

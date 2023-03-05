# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


nums_list = [int(i) for i in input().split()]
num_min = int(input())
num_max = int(input())

print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])
#!/bin/python3

import os

def filter_ones_and_zeros(data_array, idx):
    data_one = []
    data_zero = []
    for j in range(len(data_array)):
        if len(data_array) >= 1:
            if data_array[j][idx] == "1" and data_array[j] not in data_one:
                data_one.append(data_array[j])
            elif data_array[j][idx] == "0" and data_array[j] not in data_zero:
                data_zero.append(data_array[j])
    return data_array, data_one, data_zero

def oxygen(data_array, idx):
    if len(data_array) == 1:
        return data_array
    data_row, data_one, data_zero = filter_ones_and_zeros(data_array, idx)
    data_row = data_one if len(data_one) >= len(data_zero) else data_zero
    return data_row

def co2(data_array, idx):
    if len(data_array) == 1:
        return data_array
    data_row, data_one, data_zero = filter_ones_and_zeros(data_array, idx)
    data_row = data_zero if len(data_one) >= len(data_zero) else data_one
    return data_row


def life_support_rating(data_array):
    oxygen_rating = data_array
    co2_rating = data_array
    for i in range(len(co2_rating[0])):
        oxygen_rating = oxygen(oxygen_rating, i)
        co2_rating = co2(co2_rating, i)
    print(f"oxygen_rating: {oxygen_rating}")
    print(f"co2_rating: {co2_rating}")
    oxygen_dec = int(oxygen_rating[0], 2)
    co2_dec = int(co2_rating[0], 2)
    life_support_rating = oxygen_dec * co2_dec
    print(f"Life support rating: {life_support_rating}")


def main():
    path = f"{os.path.abspath(os.path.curdir)}/day3"
    print(path)
    with open(f"{path}/input.txt", "r") as fd:
        data_array = [line.strip() for line in fd.readlines()]
    life_support_rating(data_array)

if __name__ == "__main__":
    main()

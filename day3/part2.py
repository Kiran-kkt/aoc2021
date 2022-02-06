#!/bin/python3

import os

def oxygen(data_array, idx):
    data_one = []
    data_zero = []

    if len(data_array) == 1:
        return data_array

    for j in range(0, len(data_array)):
        if len(data_array) >=1:
            if data_array[j][idx] == "1" and data_array[j] not in data_one:
                data_one.append(data_array[j])
            elif data_array[j][idx] == "0" and data_array[j] not in data_zero:
                data_zero.append(data_array[j])
    if len(data_one) >= len(data_zero):
        data_array = data_one
    else:
        data_array = data_zero
    return data_array

def co2(data_array, idx):
    data_one = []
    data_zero = []

    if len(data_array) == 1:
        return data_array

    for j in range(0, len(data_array)):
        if len(data_array) >=1:
            if data_array[j][idx] == "1" and data_array[j] not in data_one:
                data_one.append(data_array[j])
            elif data_array[j][idx] == "0" and data_array[j] not in data_zero:
                data_zero.append(data_array[j])
    if len(data_one) >= len(data_zero):
        data_array = data_zero
    else:
        data_array = data_one
    return data_array


def life_supporting_rating(data_array):
    oxygen_rating = data_array
    co2_rating = data_array
    for i in range(0, len(data_array[0])):

        oxygen_rating = oxygen(oxygen_rating, i)
        co2_rating = co2(co2_rating, i)
    #    if count_one >= count_zero:
    #        oxygen_rating = data_one
    #        co2_rating = data_zero
    #    else:
    #        oxygen_rating = data_zero
    #        co2_rating = data_one
    print(f"oxygen_rating: {oxygen_rating}")
    print(f"co2_rating: {co2_rating}")
    oxygen_dec = int(oxygen_rating[0], 2)
    co2_dec = int(co2_rating[0], 2)
    life_support_rating = oxygen_dec * co2_dec
    print(f"Life support rating: {life_support_rating}")


def main():
    path = os.path.abspath(os.path.curdir) + "/day3"
    print(path)
    with open(path+"/input.txt", "r") as fd:
        data_array = [line.strip() for line in fd.readlines()]
    life_supporting_rating(data_array)

if __name__ == "__main__":
    main()

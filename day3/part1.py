
import os

def power_consumption(data_array):
    gamma_value = ""
    epsilon_value = ""
    for i in range(0, len(data_array[0])):
        count_one = 0
        count_zero = 0
        for j in range(0, len(data_array)):
            if data_array[j][i] == "1":
                count_one += 1
            elif data_array[j][i] == "0":
                count_zero += 1
        if count_zero > count_one:
            gamma_value += "0"
            epsilon_value += "1"
        else:
            gamma_value += "1"
            epsilon_value += "0"
    gamma_value = int(gamma_value, 2)
    epsilon_value = int(epsilon_value, 2)

    print(gamma_value * epsilon_value)

def main():
    path = os.path.abspath(os.path.curdir) + "/day3"
    print(path)
    with open(path+"/input.txt", "r") as fd:
        data_array = [line.strip() for line in fd.readlines()]
    power_consumption(data_array)

if __name__ == "__main__":
    main()
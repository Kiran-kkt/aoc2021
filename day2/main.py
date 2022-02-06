#!/usr/bin/python3

import os

INPUT_FILE = os.path.abspath("input.txt")

def multiply(h_pos, d_pos):
    print(h_pos * d_pos)

def main():
    with open(INPUT_FILE, "r") as fd:
        data_array = [tuple(line.strip().split(" ")) for line in fd.readlines()]
        horizontal_pos = 0
        depth_pos = 0
        aim = 0
        for data in data_array:
            if data[0] == 'forward':
                horizontal_pos += int(data[1])
                depth_pos += aim * int(data[1])
                continue
            if data[0] == 'down':
                #depth_pos += int(data[1])
                aim += int(data[1])
                continue
            if data[0] == 'up':
                #depth_pos -= int(data[1])
                aim -= int(data[1])
                continue
        print(f"H pos: {horizontal_pos}")
        print(f"D pos: {depth_pos}")
        multiply(horizontal_pos, depth_pos)

if __name__ == "__main__":
    main()


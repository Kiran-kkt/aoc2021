def main():
    with open("advent_of_code_input.txt", "r") as fd:
        depth_array = [int(line.strip()) for line in fd.readlines()]
    
    fluctuate = ["N/A"]

    for i in range(0,len(depth_array)-1):
        if depth_array[i] < depth_array[i+1]:
            fluctuate.append("increased")
        else:
            fluctuate.append("decreased")
    
    print(f"Number of measurements: {len(depth_array)}")
    print("Increased measurements: %d" %fluctuate.count("increased"))



if __name__ == "__main__":
    main()
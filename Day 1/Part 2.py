#Day 1: Calorie Counting
with open("input.txt", "r") as input:
    lines = input.readlines()
    elf_sum = 0
    calories = []
    # finds the sum of each elf's calories
    for line in lines:
        if line.strip():
            elf_sum += int(line)
        else:
            # for new line, set sum back to zero for next elf
            calories.append(elf_sum)
            elf_sum = 0

# finds the sum of the calories that the 3 most prepared elves are carrying
calories.sort(reverse=True)
topThree = sum(calories[0:3])
print(topThree)

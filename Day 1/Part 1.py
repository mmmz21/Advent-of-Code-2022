# Day 1: Counting Calories
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

# checks to see which elf has the most calories
most_calories = calories[0]
for entry in calories:
    if entry > most_calories:
        most_calories = entry
print(most_calories)

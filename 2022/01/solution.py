## advent of code 2022
## https://adventofcode.com/2022
## day 01

def parse_input(lines):
    elves = []
    elf_calories = 0
    for line in lines:
        if line.strip() != "":
            elf_calories += int(line.strip())
        else:
            elves.append(elf_calories) 
            elf_calories = 0
    elves.append(elf_calories)
    return elves

def part1(data):
    return(max(data))

def part2(data):
    return(sum(sorted(data)[-3:]))

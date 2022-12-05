############
#  PART 1  #
############
elves_calories = [[]]
with open('input.txt', 'r') as f:

    line = f.readline()
    while line:
        try:
            elves_calories[-1] += [int(line)]
        except: 
            elves_calories.append([])

        line = f.readline()

elves_calories_per_bag = [sum(ec) for ec in elves_calories]
elves_calories_per_bag.sort()
print(f'The Elf that is carrying more calories is carrying {elves_calories_per_bag[-1]} calories.')


############
#  PART 2  #
############
print(f'The top three elves that are carrying more calories are carrying {sum(elves_calories_per_bag[-3:])} calories.')

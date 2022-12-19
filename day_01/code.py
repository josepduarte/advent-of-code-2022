############
#  PART 1  #
############
print('> Part 1')

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
print(elves_calories_per_bag[-1])


############
#  PART 2  #
############
print('> Part 2')

print(sum(elves_calories_per_bag[-3:]))

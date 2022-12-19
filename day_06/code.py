import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

for l in lines:
    for i in range(0, len(l)):
        if len(set(l[i:i+4])) == 4:
            print(i+4)
            break

############
#  PART 2  #
############
print('> Part 2')

for l in lines:
    for i in range(0, len(l)):
        if len(set(l[i:i+14])) == 14:
            print(i+14)
            break

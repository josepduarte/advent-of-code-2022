with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
priorities_total = 0
for l in lines:
    priorities_total += next(
        ord(item_type) - 96 if item_type.islower() else ord(item_type) - 38 
        for item_type in l[:int(len(l)/2)] if item_type in l[int(len(l)/2):]
    )

print(f'The sum of the priorities for the items that appear in both comportments is {priorities_total}')

############
#  PART 2  #
############
priorities_total = 0
for i in range(0, len(lines), 3):
    priorities_total += next(
        ord(item_type) - 96 if item_type.islower() else ord(item_type) - 38 
        for item_type in lines[i] if item_type in lines[i+1] and item_type in lines[i+2] 
    )

print(f'The sum of the priorities for the items that appear in the 3 comportments is {priorities_total}')

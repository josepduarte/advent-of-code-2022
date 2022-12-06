import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

# Parse the stacks figure 
crate_lines = [[]]
for l in lines:
    if '[' not in l:
        crate_lines = crate_lines[:-1]
        break

    for i in range(1, len(l), 4):
        crate_lines[-1] += [l[i]]
            
    crate_lines.append([])

crate_stacks = []
for stack in [list(x) for x in zip(*crate_lines)]:
    stack.reverse()
    crate_stacks.append([x for x in stack if x != ' '])
    
# To be used on part 2
crate_stacks_copy = copy.deepcopy(crate_stacks)

############
#  PART 1  #
############
print('> Part 1')

for action in lines[len(crate_lines)+2:]:
    action_parts = action.replace('\n', '').split(' ')
    move_count, stack_from, stack_to = int(action_parts[1]), int(action_parts[3]) - 1, int(action_parts[5]) - 1

    for i in range(0, move_count):
        crate_stacks[stack_to].append(crate_stacks[stack_from].pop())

print("".join([x[-1] for x in crate_stacks]))

############
#  PART 2  #
############
print('> Part 2')

for action in lines[len(crate_lines)+2:]:
    action_parts = action.replace('\n', '').split(' ')
    move_count, stack_from, stack_to = int(action_parts[1]), int(action_parts[3]) - 1, int(action_parts[5]) - 1

    crate_stacks_copy[stack_to].extend(crate_stacks_copy[stack_from][-move_count:])
    for i in range(0, move_count):
        crate_stacks_copy[stack_from].pop()

print("".join([x[-1] for x in crate_stacks_copy]))

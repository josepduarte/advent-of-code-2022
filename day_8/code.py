import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

# Build the grid
trees_grid = []
for line in lines:
    l = []
    l[0:] = line.strip()
    trees_grid.append(l)

# Transpose the grid to make it easier for the Up and Bottom 
transpose_trees_grid = [list(x) for x in zip(*trees_grid)]

# Count the visible trees
visible_trees_count = 0
for i in range(0, len(trees_grid)):
    for j in range(0, len(trees_grid[0])):
        tree_height = trees_grid[i][j]

        # ←
        if not trees_grid[i][:j] or max(trees_grid[i][:j]) < tree_height:
            visible_trees_count += 1
            continue

        # →
        if not trees_grid[i][j+1:] or max(trees_grid[i][j+1:]) < tree_height:
            visible_trees_count += 1
            continue

        # ↑ 
        if not transpose_trees_grid[j][:i] or max(transpose_trees_grid[j][:i]) < tree_height:
            visible_trees_count += 1
            continue

        # ↓
        if not transpose_trees_grid[j][i+1:] or max(transpose_trees_grid[j][i+1:]) < tree_height:
            visible_trees_count += 1
            continue

print(visible_trees_count)

############
#  PART 2  #
############
print('> Part 2')

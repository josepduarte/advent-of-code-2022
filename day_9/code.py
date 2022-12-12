import copy
import math


with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

class Node:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_distance(self, other_node):
        return math.sqrt(math.pow(self.x - other_node.x, 2) + math.pow(self.y - other_node.y, 2))

    def get_possible_next_positions(self):
        possible_positions = []
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                possible_positions += [(self.x + x, self.y + y)]

        return possible_positions

    def mirror_node(self, other_node):
        self.x = other_node.x
        self.y = other_node.y

    def __eq__(self, other_node): 
        return self.x == other_node.x and self.y == other_node.y
        

class Head(Node):
    def __init__(self, x: int, y: int, previous_position: Node):
        super().__init__(x, y)
        self.previous_node = previous_position

    def move(self, movement: str):
        movement_mapping = {
            'U': (0, 1),
            'D': (0, -1),
            'R': (1, 0),
            'L': (-1, 0),
        }
        
        # Update previous position to current position
        self.previous_node.mirror_node(self)

        # Apply the movement to the current position
        self.x += movement_mapping[movement][0]
        self.y += movement_mapping[movement][1]

class Tail(Node):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.previous_positions = [Node(x, y)]

    def mirror_node(self, other_node: Node):
        if other_node not in self.previous_positions:
            self.previous_positions.append(copy.deepcopy(other_node))
        return super().mirror_node(other_node)

# MAIN
tail = Tail(0, 0)
head = Head(0, 0, previous_position=Node(0, 0))

for line in lines:
    movement, steps = line.strip().split(' ')

    for i in range(0, int(steps)):
        head.move(movement=movement)

        if tail.calculate_distance(head) >= 2.0:
            tail.mirror_node(head.previous_node)

print(len(tail.previous_positions))

############
#  PART 2  #
############
print('> Part 2')

# MAIN 
tail = Tail(0, 0)
head = Head(0, 0, previous_position=Node(0, 0))
nodes = [Node(0, 0) for i in range(0, 8)]

# MAIN ( ... probably the most inefficient code you will ever see ...)
tail = Tail(0, 0)
head = Head(0, 0, previous_position=Node(0, 0))

for line in lines:
    movement, steps = line.strip().split(' ')

    for i in range(0, int(steps)):
        # Move head
        head.move(movement=movement)

        # Move the first node
        for j in range(0, len(nodes)):

            if j == 0:
                if nodes[j].calculate_distance(head) >= 2.0:
                    nodes[j].mirror_node(head.previous_node)
            
            else: 
                if nodes[j].calculate_distance(nodes[j-1]) >= 2.0:
                    # Get the possible positions
                    possible_positions = [
                        x for x in nodes[j].get_possible_next_positions() 
                        if x in nodes[j-1].get_possible_next_positions()
                    ]

                    # Get the position that is closer to the previous
                    possible_positions = sorted(possible_positions, key=lambda p: nodes[j-1].calculate_distance(
                        Node(p[0], p[1]))
                    )

                    # Move to next position
                    next_position = possible_positions[0]
                    nodes[j].mirror_node(Node(next_position[0], next_position[1]))
                        
        # Move tail
        if tail.calculate_distance(nodes[-1]) >= 2.0:
            # Get the possible positions
            possible_positions = [
                x for x in nodes[-1].get_possible_next_positions() 
                if x in tail.get_possible_next_positions()
            ]

            # Get the position that is closer to the previous
            possible_positions = sorted(possible_positions, key=lambda p: nodes[-1].calculate_distance(
                Node(p[0], p[1]))
            )

            # Move to next position
            next_position = possible_positions[0]
            tail.mirror_node(Node(next_position[0], next_position[1]))
            
print(len(tail.previous_positions))

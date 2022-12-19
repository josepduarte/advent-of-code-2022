with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

class CPU:

    def __init__(self, code_lines):
        self.cycle = 1
        self.register_value = 1
        self.code_lines = code_lines
        self.instructions_stack = []
        self.compiled = False

    def compile(self):
        for code_line in self.code_lines:
            parsed_code_line = code_line.strip().split(' ')

            if 'noop' in parsed_code_line:
                self.instructions_stack.append(('noop', None))
            elif 'addx' in parsed_code_line:
                self.instructions_stack.extend([('noop', None), (parsed_code_line[0], parsed_code_line[1])])
            else:
                raise ValueError('UNKNOWN INSTRUCTION')

        self.compiled = True

    def run(self):
        if not self.compiled:
            raise ValueError('COMPILE FIRST!')

        instruction_operation, instruction_operand = self.instructions_stack.pop(0)
        if instruction_operation == 'addx':
            self.register_value += int(instruction_operand)
        elif instruction_operation == 'noop': 
            pass
        else:
            raise ValueError('RUNTIME ERROR')
        
        self.cycle += 1

    def get_signal_strength(self):
        return self.cycle * self.register_value

# MAIN
communication_system_cpu = CPU(code_lines=lines)
communication_system_cpu.compile()

signal_strengths = []
for c in [20, 60, 100, 140, 180, 220]:
    while communication_system_cpu.cycle < c:
        communication_system_cpu.run()
    signal_strengths += [communication_system_cpu.get_signal_strength()]

print(sum(signal_strengths))

############
#  PART 2  #
############
print('> Part 2')

crt_image = [['.'] * 40 for i in range(0, 6)]

communication_system_cpu = CPU(code_lines=lines)
communication_system_cpu.compile()

while communication_system_cpu.instructions_stack:
    sprite_position = communication_system_cpu.register_value
    
    cpu_cycle_line_position = (communication_system_cpu.cycle - 1) % 40
    crt_row = int(communication_system_cpu.cycle / 40)
    if cpu_cycle_line_position in [sprite_position - 1, sprite_position, sprite_position + 1]:
        crt_image[crt_row][cpu_cycle_line_position] = '#'

    communication_system_cpu.run()

# Draw :)
print('\n'.join([''.join(line) for line in crt_image]))

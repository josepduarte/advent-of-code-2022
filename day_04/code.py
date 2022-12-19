with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

fully_overlapping_assignments = 0
for line in lines:
    elf_1_sections, elf_2_sections = (x.strip().split('-') for x in line.split(','))

    elf_1_sections_range =  range(int(elf_1_sections[0]), int(elf_1_sections[-1]) + 1)
    elf_2_sections_range = range(int(elf_2_sections[0]), int(elf_2_sections[-1]) + 1)

    fully_overlapping_assignments += int(
        all(section in elf_2_sections_range for section in elf_1_sections_range)
        or all(section in elf_1_sections_range for section in elf_2_sections_range)
    )

print(fully_overlapping_assignments)

############
#  PART 2  #
############
print('> Part 2')

overlapping_assignments = 0
for line in lines:
    elf_1_sections, elf_2_sections = (x.strip().split('-') for x in line.split(','))

    elf_1_sections_range =  range(int(elf_1_sections[0]), int(elf_1_sections[-1]) + 1)
    elf_2_sections_range = range(int(elf_2_sections[0]), int(elf_2_sections[-1]) + 1)

    overlapping_assignments += int(
        any(section in elf_2_sections_range for section in elf_1_sections_range)
        or any(section in elf_1_sections_range for section in elf_2_sections_range)
    )

print(overlapping_assignments)

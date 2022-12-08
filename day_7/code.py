import copy

with open('input.txt', 'r') as f:
    lines = f.readlines()

############
#  PART 1  #
############
print('> Part 1')

#
# Enums (to make it a bit more readable)
#
class EntryType(object):
    DIRECTORY = 'directory'
    FILE = 'file'


#
# Determine the files tree 
#
root_directory = {'_size':0, '_type': EntryType.DIRECTORY}

# Create a pointer to point to the current location/directory
currenct_directory = root_directory

# To be able to naviagate to the parent 
file_system_full_path = []

for l in lines:
    command_parts = l.strip().split(' ')

    # Deal with Change Directory command
    if command_parts[0] == '$' and  command_parts[1] == 'cd':
        next_dir = command_parts[-1]

        if next_dir == '/':
            # Go to the root directory
            currenct_directory = root_directory

            # Update full path
            file_system_full_path = []

        elif next_dir == '..':
            # Update full path 
            file_system_full_path.pop()

            # Go to the parent directory
            currenct_directory = root_directory
            for p in file_system_full_path:
                currenct_directory = currenct_directory[p]

        else:
            # Create next directory if it does not exist
            if next_dir not in currenct_directory:
                currenct_directory[next_dir] = {'_size':0, '_type': EntryType.DIRECTORY}
            
            # Move to the next directory
            currenct_directory = currenct_directory[next_dir]

            # Update full path 
            file_system_full_path += [next_dir]

    # Deal with dir entries
    elif command_parts[0] == 'dir':
        directory_name = command_parts[-1]
        if directory_name not in currenct_directory:
            currenct_directory[directory_name] = {'_size':0, '_type': EntryType.DIRECTORY}

    # Deal with file entries
    elif command_parts[0] != '$':
        filesize, filename = int(command_parts[0]), command_parts[1]

        if filename not in currenct_directory:
            currenct_directory[filename] = {'_size':filesize, '_type': EntryType.FILE}

            # Update the size to all the parent directories
            root_directory['_size'] += filesize
            temp_directory_pointer = root_directory
            for p in file_system_full_path:
                temp_directory_pointer = temp_directory_pointer[p]
                temp_directory_pointer['_size'] += filesize

    # Deal with ls (and everything else)
    else: 
        pass  # :) 


# 
# Get the directories given a custom filter method for the size
#
def get_directories(parent_directory, size_filter_method):
    smaller_directories = []
    for entry_name, entry_content in parent_directory.items():
        if isinstance(entry_content, dict) and entry_content['_type'] == EntryType.DIRECTORY:
            if size_filter_method(entry_content['_size']):
                smaller_directories += [{'name': entry_name, 'size': entry_content['_size']}]
            
            smaller_directories += get_directories(entry_content, size_filter_method)

    return smaller_directories

size_filter_method = lambda x: x < 100000
print(sum(directory['size'] for directory in get_directories({'/': root_directory}, size_filter_method)))

############
#  PART 2  #
############
print('> Part 2')
FILESYSTEM_SIZE = 70000000
UPDATE_SIZE = 30000000

size_filter_method = lambda x: x > UPDATE_SIZE - (FILESYSTEM_SIZE - root_directory['_size'])  
print(min(directory['size'] for directory in get_directories({'/': root_directory}, size_filter_method)))

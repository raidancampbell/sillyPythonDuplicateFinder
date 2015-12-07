import inflect
p = inflect.engine()
import re
from os import listdir
from os.path import isfile, join

# why was 6 afraid of 7?  because 789
def is_number(str_num):
    try:
        int(str_num)
        return True
    except ValueError:
        return False

# the bird is the word
def num_to_word(string):
    return_var = ''
    for word in string.split(' '):
        return_var += (word if not is_number(string) else p.number_to_words(string)) + ' '
    return return_var

# metadata has the best strippers
def strip_metadata(str_data):
    filename = re.search(".{46}(.+)", str_data)  # magic number.  works for me.
    if not filename:
        return str_data
    return_var = ''
    for char in filename.group(1):
        if char is not '[':
            return_var += char
        else:
            break
    return_var = return_var.strip()
    has_extension = re.search("(\.\w..?.?)", return_var)
    #  matches things like .avi, .mp4, .m4v, .ts, and .divx
    if has_extension:  # remove it
        return return_var.replace(has_extension.group(1), "").strip()
    return return_var

# whats a dicfore?  ha ha ha
def file_to_string(filename):
    with open(filename, "r") as my_file:
        return my_file.readlines()

# slice n dice
def slice_iterator(my_list):
    for i in range(len(my_list)):
        yield my_list[i:i]

# where?
def get_files_from_directory(directory_name):
    return [join(directory_name, f) for f in listdir(directory_name) if isfile(join(directory_name, f))]

#  begin execution.  its a very bloody process.  Because I already decided this is a hacky thing, it doesn't get a main method

input_files = {}
for file in get_files_from_directory("input"):
    input_files[file] = list(map(lambda x: num_to_word(strip_metadata(x.strip().lower())), file_to_string(file)))

for file_name in input_files.keys():  # for each file in the directory
    for entry in input_files[file_name]:  # for each line in that file
        for other_file_name in input_files.keys():
            if entry in input_files[other_file_name] and file_name is not other_file_name:
                print('{:>50} found in {:>25} and {:>25}'.format(entry, file_name, other_file_name))

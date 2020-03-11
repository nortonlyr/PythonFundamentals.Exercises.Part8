import os
path = '/Users/nli/desktop/'
for dir_path, dir_names, file_names in os.walk(path):
    for file_name in file_names:
        print(os.path.join(dir_path, file_name))
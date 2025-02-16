#! /home/romel-linux/untitledProjects/.myenv_main/bin/python
#shebang works{{all that is needed
#is a description for the program}}

#import shutil
import shutil
import os
from send2trash import send2trash
from pprint import pprint
import re
from secretkeys import secret_key_1, secret_key_2, secret_key_3, secret_key_4, new_name_for_3rd_batch_rename, source_folder

#switch the names of the particular ###:edit:
secret_key_3 = new_name_for_3rd_batch_rename

#basedir
basedir = os.getcwd()
print("basedir,", basedir)

#get videos dir.name
videosdir = f"{source_folder}"

#name output dir
output_dir = f"{source_folder}___modified"
print("output_dir,", output_dir)
return_output = os.path.isdir(output_dir)
print("return_output,", return_output)


#if output_dir DOES NOT EXIST: #create a new dir
if not return_output:
    os.mkdir(output_dir)
    print("dir-created")

# create a new list out of sorted(os.listdir(*)), to use re
test_string ="2025-01-12 16-05-48 akdjfkalsdjflakjswelkrjlkjsdf;ajsf;lskdj"
regExExample = re.compile(r'(\d\d\d\d-\d\d-\d\d) (\d\d-\d\d-\d\d)')
output_regEx = regExExample.search(test_string)
def test_prints():
    # print(dir(output_regEx))
    print(output_regEx.span())
    print(output_regEx.group())
    print(output_regEx.group()[17], output_regEx.group()[18])
    print(output_regEx.pos)
    print(output_regEx.string[output_regEx.end():])
    #dont forget to strip leading spaces
test_prints()

#create a unique list of numbers because I need to skip a number
def range_function():
    for i in range(1,20):
        if not i == 3:
            print(i)
        else:
            continue


#
def function__1():
    new_list = []
    for i in sorted(os.listdir(videosdir)):
        output_regEx = regExExample.search(i)
        output_regEx_position = output_regEx.end()
        toBeCopied_or_moved = i[output_regEx_position:].lstrip()
        print("TEST-PRINT:", toBeCopied_or_moved)
        combined_item = os.path.join(videosdir, toBeCopied_or_moved)
        new_list.append(combined_item)
    return new_list
    # pprint(new_list)

#get base
def function__2(elem):
    basename_modified_prepended = secret_key_3
    for ei, i in enumerate(elem):
        basename = os.path.basename(i)
        dirname = os.path.dirname(i)
        basename_modified = f"{basename_modified_prepended} {basename}"
        elem[ei] = os.path.join(dirname, basename_modified)
    return elem 

#
def original_list():
    original_list = []
    for i in sorted(os.listdir(videosdir)):
        original_list.append(i)
    return original_list

#
def get_dir_name():
    pass

#
def get_cwd():
    return os.getcwd()

# define proj_dir
def get_proj_dir():
    path_to_proj_dir = " this is a string "
    return path_to_proj_dir


def for_Each(elem):
    for every_item in elem:
        print(every_item)


#test print(s):
# pprint(sorted(os.listdir(videosdir)))
print("\nNew-line:")

if __name__ == '__main__':
    original_list = original_list()
    directory_name = videosdir
    elem = function__1()
    lists_of_simpleBasenames = []
    for i in elem:
        lists_of_simpleBasenames.append(os.path.basename(i))
    elem = function__2(elem)
    lists_of_modifiedBasenames = []
    for i in elem:
        lists_of_modifiedBasenames.append(os.path.basename(i))
    print("len(lists_of_simpleBasenames),", len(lists_of_simpleBasenames))
    print(videosdir) # this is a path
    print("len(os.listdir(videosdir)),",len(os.listdir(videosdir)))
    items_in_directory = sorted(os.listdir(videosdir))
    if os.listdir(output_dir):
        print("len-dir,", len(os.listdir(output_dir)))
        # send2trash(output_dir)
        # print('dir-sent-trash')
        shutil.rmtree(output_dir)
        print('shutil-rmtree')
        os.mkdir(output_dir)
        print('dir-re-created')
    for index, items in enumerate(items_in_directory):
        regexObj = re.compile(f'{lists_of_simpleBasenames[index]}').search(items_in_directory[index])
        start_pos = regexObj.start()
        end_pos = regexObj.endpos
        check_criteria = items_in_directory[index][start_pos:end_pos]
        if re.compile(check_criteria).search(lists_of_modifiedBasenames[index]):
            dir_name = videosdir
            base_name = items_in_directory[index]
            path_source = os.path.join(dir_name, base_name)
            dirname_output = output_dir
            basename_output = lists_of_modifiedBasenames[index]
            path_output = os.path.join(dirname_output, basename_output)
            shutil.copy(path_source, path_output)
            print('files-added')
        else: 
            print("False---")

    for i in sorted(os.listdir(dirname_output)):
        print(i)
    
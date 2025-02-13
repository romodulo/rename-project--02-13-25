#! /home/romel-linux/untitledProjects/.myenv_main/bin/python
#shebang works{{all that is needed
#is a description for the program}}

#import shutil
import shutil
import os
from send2trash import send2trash
from pprint import pprint
import re
from secretkeys import secret_key_1, secret_key_2, secret_key_3


#basedir
basedir = os.getcwd()
print("basedir,", basedir)

#get videos dir.name
videosdir = f"{secret_key_1}/backup--2-13-25-OBS-self-recordings"

#name output dir
output_dir = f"{secret_key_1}/backup--2-13-25-OBS-self-recordings___modified"
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
        combined_item = os.path.join(videosdir, toBeCopied_or_moved)
        new_list.append(combined_item)
    return new_list
    # pprint(new_list)

#get base
def function__2(elem):
    basename_modified_prepended = secret_key_3
    count = 0
    for ei, i in enumerate(elem):
        if count < 9:
            if not ((ei + 1) == 3):
                basename = os.path.basename(i)
                dirname = os.path.dirname(i)
                basename_modified = f"{basename_modified_prepended} |0{count+1}| {basename}"
                count += 1
                elem[ei] = os.path.join(dirname, basename_modified)
            else:
                basename = os.path.basename(i)
                dirname = os.path.dirname(i)
                basename_modified = f"{basename_modified_prepended} |0{count+2}| {basename}"
                count += 2
                elem[ei] = os.path.join(dirname, basename_modified)
        elif count >= 9:
            if not ((ei + 1) == 3):
                basename = os.path.basename(i)
                dirname = os.path.dirname(i)
                basename_modified = f"{basename_modified_prepended} |{count+1}| {basename}"
                count += 1
                elem[ei] = os.path.join(dirname, basename_modified)
            else:
                basename = os.path.basename(i)
                dirname = os.path.dirname(i)
                basename_modified = f"{basename_modified_prepended} |{count+2}| {basename}"
                count += 2
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
pprint(os.listdir(output_dir))

if __name__ == '__main__':
    original_list = original_list()
    # for_Each(original_list)
    #what is the directory_name:
    directory_name = videosdir
    #what will the file_paths look like
    #when I join strings together
    # for i in original_list:
    #     print(os.path.join(directory_name, i))
    #what is the output_directory? #output_dir
    
    #
    elem = function__1()
    lists_of_simpleBasenames = []
    for i in elem:
        lists_of_simpleBasenames.append(os.path.basename(i))
    # for i in lists_of_simpleBasenames:
    #     print(i)
    # for_Each(elem)
    #
    #
    #
    elem = function__2(elem)
    lists_of_modifiedBasenames = []
    for i in elem:
        lists_of_modifiedBasenames.append(os.path.basename(i))
    # for i in lists_of_modifiedBasenames:
    #     print(i)
    # for i in original_list:
    #     print(i)
    # for_Each(elem)
    #
    #
    #
    print(len(lists_of_simpleBasenames))
    print(videosdir) # this is a path
    print(len(os.listdir(videosdir)))
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
        # print(dir(regexObj))
        start_pos = regexObj.start()
        # print("start_pos", start_pos)
        end_pos = regexObj.endpos
        # print("end_pos", end_pos)
        check_criteria = items_in_directory[index][start_pos:end_pos]
        # print(lists_of_modifiedBasenames[index])
        # print(check_criteria)
        # print(items_in_directory[index])
        if re.compile(check_criteria).search(lists_of_modifiedBasenames[index]):
            dir_name = videosdir
            base_name = items_in_directory[index]
            path_source = os.path.join(dir_name, base_name)
            # print(path_source)
            dirname_output = output_dir
            # print("isDir?:", os.path.isdir(dirname_output))
            basename_output = lists_of_modifiedBasenames[index]
            path_output = os.path.join(dirname_output, basename_output)
            shutil.copy(path_source, path_output)
            # print('output-dir-is-empty', output_dir, os.path.isdir(output_dir))
            print('files-added')
        else: 
            print("False---")

    for i in sorted(os.listdir(dirname_output)):
        print(i)
    
    # for i in elem:
    #     print(i)
    
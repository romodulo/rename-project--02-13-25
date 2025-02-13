#! /home/romel-linux/untitledProjects/.myenv_main/bin/python
#shebang works{{all that is needed
#is a description for the program}}

#import shutil
import shutil
import os
from pprint import pprint
#import send2trash below
from secretkeys import secret_key_1, secret_key_2

insertSecretKey1 = secret_key_1
insertSecretKey2 = secret_key_2


#basedir
basedir = os.getcwd()
print("basedir,", basedir)

#get abs, path
variableA = os.path.abspath(".")
print(variableA)

#get abs path videos
variableD = os.path.abspath("a")
print(variableD)

#get relpath {{appended}} {{variable out of order}}
variableC = os.path.relpath(insertSecretKey1, ".")
print(variableC)

#chdir
os.chdir('/')
variableB = os.getcwd()
print(variableB)

#os
os.path.isdir(variableA)


# run
# shutil.copy()


#Variables-Restart #added a basedir 'variable' up top
os.chdir(basedir)
variableE = os.getcwd()
print(variableE)

#get dirname of basedir
variableF = os.path.dirname(variableE)
print(variableF)

#
variableG = os.path.join(variableF, "Videos")
print("variableG", variableG)

#
variableH = os.path.join(variableG, 'OBS-self-recordings-2--2nd---branch')
print("variableH", variableH)

#list
variableI = sorted(os.listdir(variableH))
print('variableI: is listdir(variableH) \#sorted')
# print("variableI: ")  #part of pprint example
# pprint(variableI)#sorts #successfully  #pprint example

#
#variableH holds directory
#1.)copy variableH to a different directory
#2.)modify different directory with python scriipt
#variableG holds directory '~/Videos'
#3.)copy directory 'variableH' to a new Dir in directory 'variableG'
#3-1.)mkdir called 'routerVideosBackup' in directory 'variableG'
#3-2.)copy 'variableH' to os.path.join(variableG, 'routerVideosBackup')
#optional3.)use os.makedirs(path)
#new set-up procedure order:
#os.path.join first
#then. os.makedirs(path):
stringJoin = os.path.join(variableG, 'routerVideosBackup')
if not os.path.exists(stringJoin):
    os.makedirs(stringJoin)
    # copy dirs
    if os.path.exists(stringJoin):
        #delete path that already exists
        #i know: redundent,
        #but it has to be done.
        shutil.rmtree(stringJoin)
        shutil.copytree(variableH, stringJoin)
        print("'rmtree:'", stringJoin, " accomplished")
        print("shutil.copytree-accomplished ")
if os.path.exists(stringJoin): #this just checks if a path
                               #exists. I don't know why it's there
    print("path EXistS")       #, but will just keep it there. 
#dev-mode:
# def dev_mode(): #reposition
#del stringJoin Dir
# pip install send2trash
# import said module into __main__
import send2trash
#these definitions
#are no longer required:
def dev_mode():
    #delete newly created dir
    send2trash.send2trash(stringJoin)
    print(stringJoin, " sent to trash")
def dev_mode_shutil():
    #delete newly created dir
    shutil.rmtree(stringJoin)
    print("shutil.rmtree:", stringJoin, " deleted")
# dev_mode() #safer- dev-mode
# dev_mode_shutil()

#new logic here:
print('stringJoin:', stringJoin)
if os.path.exists(stringJoin):
    print(stringJoin)
    DirlistStringJoin = sorted(os.listdir(stringJoin))
    # pprint(DirlistStringJoin) # pprint example
    print("path EXistS-2")

#manipulate list here:
#check if path exists:
if os.path.exists(stringJoin):
    print(len(DirlistStringJoin))

#create a dirname
currentFile = f"{insertSecretKey2}/rename.py"
dirName = os.path.dirname(currentFile)
print('dirname:', dirName)
baseName = os.path.basename(currentFile)
print('basename:', baseName)
siblingFolder = "evenNumbersList"
print('siblingFolder', siblingFolder)
sourceFile_01 = "ModifiedpendingString.txt"
joinedPaths = os.path.join(dirName, siblingFolder, sourceFile_01)

#what is my list of files to rename
# variableI
pprint(variableI)

#test open file
print('joinedPaths:', joinedPaths)
fileObject = open(joinedPaths, "r")
# print(fileObject.read())
fileObject.close()

#open: ModifiedpendingString.txt
#close
# modifiedToAppendObj = open(os.path.join(baseModifiedpendingString.txt, "r")
# readlines = modifiedToAppendObj.read()
# pprint(readlines)

#if this then this
#
#
#i think i need to create a new python
#file to accomplish my task
#to avoid code getting too
#messy.
#
#
#
#

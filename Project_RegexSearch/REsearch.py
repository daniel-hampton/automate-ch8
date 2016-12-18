#! python3
# REsearch.py performs a regex search on all .txt files in a folder supplied by the user. Results printed to screen.

import re
import os

# Get folder to search from user.
while True:
    folderPath = os.path.abspath(input('Enter the folder path to search: \n'))
    if os.path.isdir(folderPath):
        break
    else:
        print('The string entered was not a valid path. Ctrl-C to quit')
        continue

# Get the regex from the user.
userRegexInput = input('Enter the regex:\n')
userRegex = re.compile(r'{}'.format(userRegexInput))

# Retrieves list of absolute file paths separate from directories.
fileNames = [os.path.join(folderPath, file) for file in os.listdir(folderPath) if os.path.isfile(
    os.path.join(folderPath, file))]

# Separate list of only the .txt files.
textFiles = [file for file in fileNames if file.endswith('.txt')]

# Loop through text files printing out the lines where matches are found.
for file in textFiles:

    (dirName, baseName) = os.path.split(file)
    print('Results for {}:\n'.format(baseName))

    fileObject = open(file, 'r', encoding='utf-8')
    textList = fileObject.readlines()

    for item in textList:
        mo = userRegex.search(item)
        if mo is None:
            continue
        else:
            print(item)

    fileObject.close()

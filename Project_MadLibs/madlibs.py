#! python3
# madlibs.py reads a text file for instances of: ADJECTIVE, NOUN, ADVERB, or VERB and prompts the user to
# replace them with their own words. Writes a new text file with the replacements to the cwd.

import re
import os

# Prompt user for text file to read
while True:
    inputFilename = input('Enter the path or name of the text file to read:\n')
    if os.path.isfile(inputFilename):
        break
    elif inputFilename.lower() == 'quit':
        print('Hit ctrl-c to end the program.')
        continue
    else:
        print('The name or path entered was not a valid file')
        continue

# Define regex and dict of prompts to display to user when keywords are found.
inputTextFile = open(inputFilename, 'r')
newTextString = inputTextFile.read()
wordRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
targetWords = {'ADJECTIVE': 'Enter an adjective:\n',
               'NOUN': 'Enter a noun:\n',
               'ADVERB': 'Enter an adverb:\n',
               'VERB': 'Enter a verb:\n'}

# Loop through text to find target words and prompt for replacement.
while True:
    mo = wordRegex.search(newTextString)
    if mo is None:
        break
    elif mo.group() in targetWords:
        replacementWord = input(targetWords[mo.group()])
        newTextString = wordRegex.sub(replacementWord, newTextString, count=1)
    else:
        print('something went wrong.')
        break

print(newTextString)

inputTextFile.close()

# Write the new text file to the current working directory.
outputFile = open('madlibsoutput.txt', 'w')
outputFile.write(newTextString)

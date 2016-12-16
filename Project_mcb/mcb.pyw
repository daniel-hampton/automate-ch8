#! python3
# mcb.pyw - Saves and loads pieces of text tot he clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve
import pyperclip
import sys
import os   # modified from book example

# path was added. Not in book example. Did not want data files in home directory.
path = 'C:/Users/HOME4400/PycharmProjects/AutomateTheBoringStuff/Chapter8_ReadingAndWritingFiles/Project_mcb/'
mcbShelf = shelve.open(os.path.join(path, 'mcb'))

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()

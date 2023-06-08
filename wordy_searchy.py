"""Created: 2023-06-08 by @VictorieeMan
This script can help you with solving word puzzles.
Add a dictionary of words to the input.txt file, then run the script.

Recommended usage:
1. Get words from using the Merriam-Webster word Finder (https://www.merriam-webster.com/wordfinder)
2. Copy the words to the input.txt file
3. Run the script

If manually adding words or getting words from another source, make sure that the words are in the following format:
- one word per line
"""

import re

# Read input file
temp = []

with open('input.txt', 'r') as file:
    for line in file:
        # Remove new line characters
        line = line.replace('\n', '')
        # Remove whitespaces
        word = line.replace(' ', '')
        temp.append(word)

temp = [word for word in temp if word != '']
potential_words = temp

# Instructions
recommended_usage = "Recommended usage: \n" + \
                    "1. Get words from using the Merriam-Webster word Finder (https://www.merriam-webster.com/wordfinder) \n" + \
                    "2. Copy the words to the input.txt file \n" + \
                    "3. Run the script \n\n"

print(recommended_usage)

instructions_help = "Instructions: \n" + \
                    "- Enter a new rule to filter the words. \n" + \
                    "\t- Use a single character to remove words with that character.\n" + \
                    "\t  Ex. \"k\" Will remove all words containing the letter k. \n\n" + \
                    "\t- Use '+[char]' to remove words without that character. \n" + \
                    "\t  Ex. \"+k\" Will remove all words not containing the letter k. \n\n" + \
                    "\t- Use '-[position][char]' to remove words with that character at that position. \n" + \
                    "\t  Ex. \"-3k\" Will remove all words with the letter k at the 3rd position. \n\n" + \
                    "\t- Use '=[position][char]' to remove words without that character at that position. \n" + \
                    "\t  Ex. \"=3k\" Will remove all words without the letter k at the 3rd position. \n\n" + \
                    "\t- Use ':[length]' to remove words with length not equal to that length. \n" + \
                    "\t  Ex. \":5\" Will remove all words with length not equal to 5. \n\n" + \
                    "\t- Use '>[length]' to remove words with length less than that length. \n" + \
                    "\t  Ex. \">5\" Will remove all words with length less than 5. \n\n" + \
                    "\t- Use '<[length]' to remove words with length greater than that length. \n" + \
                    "\t  Ex. \"<5\" Will remove all words with length greater than 5. \n\n" + \
                    "- Enter 'exit!' to exit the program. \n" + \
                    "- Enter 'clear' to clear the rules and start over. \n" + \
                    "- Enter 'help' to see the instructions again. \n"

print(instructions_help)

while(True):
    char = input('Enter a new rule: ')
    if char == 'exit!':
        break
    elif char == 'clear':
        potential_words = temp
        continue
    elif char == 'help':
        print(instructions_help)
        continue

    if len(char) == 1:
        # Remove words with char
        potential_words = [word for word in potential_words if not re.search(char, word)]
    
    elif char[0] == '+':
        # Remove words without char
        # sample input: "+b",
        # means that words without b will be removed

        # Get char
        char = char[1]

        # Remove words without char
        potential_words = [word for word in potential_words if re.search(char, word)]

    elif char[0] == '-':
        # Remove words with char at given position
        # sample input: "-3b",
        # means that words with b at 3rd position will be removed

        # Get position
        position = int(char[1])
        # Get char
        char = char[2]

        # Remove words with char at position
        potential_words = [word for word in potential_words if word[position - 1] != char]

    elif char[0] == '=':
        # Remove words without char at given position
        # sample input: "=3b",
        # means that words without b at 3rd position will be removed

        # Get position
        position = int(char[1])
        # Get char
        char = char[2]

        # Remove words without char at position
        potential_words = [word for word in potential_words if word[position - 1] == char]

    elif char[0] == ":" and isinstance(char[:-1], int):
        # Remove words with length not equal to given length
        # sample input: ":5",
        # means that words with length not equal to 5 will be removed

        # Get length
        length = int(char[1:])

        # Remove words with length not equal to given length
        potential_words = [word for word in potential_words if len(word) == length]
    
    elif char[0] == ">" and isinstance(int(char[1:]), int):
        # Remove words with length less than given length
        # sample input: ">5",
        # means that words with length less than 5 will be removed

        # Get length
        length = int(char[1:])

        # Remove words with length less than given length
        potential_words = [word for word in potential_words if len(word) > length]

    elif char[0] == "<" and isinstance(int(char[1:]), int):
        # Remove words with length greater than given length
        # sample input: "<5",
        # means that words with length greater than 5 will be removed

        # Get length
        length = int(char[1:])

        # Remove words with length greater than given length
        potential_words = [word for word in potential_words if len(word) < length]
    
    else:
        print("Unknown command, please try again.")
        print(instructions_help)
        continue

    print('Potential words: ')
    for word in potential_words:
        print(word)
    print('\nNumber of potential words: ' + str(len(potential_words)))
    print('\n')
    
print("Done!")

### End of script ###

### License ###
"""
ISC License

Copyright (c) 2023 VictorieeMan

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""
# Welcome to R2O. Please read README.md for more information

import os
import sys
from typing import List

MAIN_EMOJI = "\U0001F5CA" * ("--no-emojis" not in sys.argv)

def bidirectional_pad(text: str, pad: str, num: int = 1) -> str:
    return (pad * num) + text + (pad * num)

def colour_select() -> str:
    highlight_colour = ''
    red = '#FF5582A6'
    orange = '#BD6500'
    yellow = '#BABD00'
    green = '#69E772'
    blue = '#69E7E4'
    purple = '#AD21D9'

    while(1):
        colour = input(
            "\n"
            + bidirectional_pad("Please enter which colour you want the new obsidian highlights to be in:", MAIN_EMOJI)
            + "\n\n"
            + bidirectional_pad("1. red", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("2. orange", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("3. yellow", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("4. green", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("5. blue", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("6. purple", MAIN_EMOJI)
        )
        
        match colour:
            case '1':
                highlight_colour = red
                return highlight_colour
            case '2':
                highlight_colour = orange
                return highlight_colour 
            case '3':
                highlight_colour = yellow
                return highlight_colour
            case '4':
                highlight_colour = green
                return highlight_colour
            case '5':
                highlight_colour = blue
                return highlight_colour
            case '6':
                highlight_colour = purple
                return highlight_colour
            case _:
                print("\n" + bidirectional_pad("Invalid colour choice", MAIN_EMOJI))
            
    
def menu_select() -> str:
    return input(
        "\n"
        + bidirectional_pad("What would you like to do?", MAIN_EMOJI, 3)
        + "\n\n"
        + bidirectional_pad("1. Read a file", MAIN_EMOJI)
        + "\n"
        + bidirectional_pad("2. Read a text from the stdin", MAIN_EMOJI)
        + "\n"
        + bidirectional_pad(
            "3. Read a file and append it to another file",
            MAIN_EMOJI,
        )
        + "\n"
        + bidirectional_pad("4. Exit", MAIN_EMOJI)
        + "\n"
    )


def intake_name(filename: str):
    """
    Function to intake a filename and open the file in read mode.
    If the file does not exist the function
    will be repeatedly ask for a valid filename.
    It return a list, with each element being a line from the file
    """
    while not os.path.isfile(filename):
        filename = input(
            bidirectional_pad(
                "File not found, please enter the name of the file",
                MAIN_EMOJI,
            )
        )

    with open(filename, "r", encoding="utf-8") as readfile:
        lines = readfile.readlines()
        return lines


def file_amalgam(lines):
    """
    Function to intake a filename and open the file in append mode.
    If the file does not exist the function
    will be repeatedly ask for a valid filename.
    """
    path = input(
        bidirectional_pad(
            "Please enter the name of the file you wish to add to",
            MAIN_EMOJI,
        )
        + "\n (This will overwrite any existing file of the same name) \n"
    )

    while not os.path.isfile(path):
        path = input(
            bidirectional_pad(
                "Please enter the name of the file you wish to add to",
                MAIN_EMOJI,
            )
            + "\n (This will overwrite any existing file of the same name) \n"
        )

    with open(
        path,
        "a",
        encoding="utf-8",
    ) as destination:
        new_data = slayer(lines)
        destination.writelines(new_data)

def syntax_lang_select(line):
    '''Function to intake the language that the user wants the Syntax Highlighting of Code Snippets to be in
    '''
    
    while(1):
        lang = input(
            "\n"
            + bidirectional_pad("A code snippet has been detected. Please enter which Programming Language you want the Syntax Highlighting to be in:", MAIN_EMOJI)
            + "\n\n"
            + bidirectional_pad("1. None", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("2. C", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("3. Python", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("4. Java", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("5. HTML", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("6. CSS", MAIN_EMOJI)
            + "\n"
            + bidirectional_pad("7. PHP", MAIN_EMOJI)
        )
        
        match lang:
            case '1':
                syntax_lang = ""
                return syntax_lang
            case '2':
                syntax_lang = "```C"
                return syntax_lang
            case '3':
                syntax_lang = "```Python"
                return syntax_lang
            case '4':
                syntax_lang = "```Java"
                return syntax_lang
            case '5':
                syntax_lang = "```HTML"
                return syntax_lang
            case '6':
                syntax_lang = "```CSS"
                return syntax_lang
            case '7':
                syntax_lang = "```PHP"
                return syntax_lang
            case _:
                print("\n" + bidirectional_pad("Invalid colour choice", MAIN_EMOJI))
            
            
def replacer(line, key, target, target2):
    '''Function that replaces given markdown highlighter syntax with Obsidian Highlightr syntax. 
    Must alternate due to opening and closing tags.
    '''
    counter = 0

    while line.find(key) != -1:
        if counter % 2 == 0:
            line = line.replace(key, target, 1)
            counter += 1

        if counter % 2 == 1:
            line = line.replace(key, target2, 1)
            counter += 1
    
    result = [line, counter]
    return result

def syntax_replacer(line, key, target, counter):
    '''Function that replaces given markdown highlighter syntax with Obsidian Highlightr syntax. 
    Must alternate due to opening and closing tags.
    '''
    print(line)
    if counter % 2 == 0:
        line = line.replace(key, target, 1)
            
    return line
    
    
def slayer(lines) -> List[str]:
    """
    Intake a file object and a list of elements making of the contents of a previously read file.
    The user is promted to select which colour they want highlighted.
    Line by line, it replaces the first "==" or "^^" it finds with the opening tag of the highlight colour and
    the second "=="/"^^" is replaced by the closing tag of the highlight colour.
    """

    #Function to select highlight colour
    highlight_colour = colour_select()
    
    equal_count = 0
    hat_count = 0
    syntax_lang_count = 0
    
    new_text = []
    
    syntax_lang_flag = False
    
    for line in lines:
        line = str(line)
        
                
        equal_replace_arr = replacer(line, "==", '<mark style="background:'+ highlight_colour +';">', '</mark>')
        line = equal_replace_arr[0]
        equal_count += equal_replace_arr[1]
        
        hat_replace_arr = replacer(line, "^^", '<mark style="background:'+ highlight_colour +';">', '</mark>')
        line = hat_replace_arr[0]
        hat_count += hat_replace_arr[1]
                
        if line.find("```") != -1 and syntax_lang_flag == False:
            syntax_lang = syntax_lang_select(line)
            syntax_lang_flag = True
        
        
        if line.find("```") != -1 and syntax_lang_flag == True:
            line = syntax_replacer(line, "```", syntax_lang, syntax_lang_count)
            syntax_lang_count += 1
            
        
        new_text.append(line)
        
    print(bidirectional_pad(f"{(equal_count + hat_count) / 2} hightlights have been reformatted!", MAIN_EMOJI))
    return new_text


def write_new_file(data: str):
    filename = input(
        bidirectional_pad(
            "Please enter the name of the new text file that will be summoned",
            MAIN_EMOJI,
        )
    )
    while os.path.isfile(filename):
        filename = input("\nFile already exists. Pick a different one.\n")
    with open(filename, "w", encoding="utf-8") as newfile:
        new_data = slayer(data)
        newfile.writelines(new_data)


def main():
    print(bidirectional_pad("WELCOME TO R2O", MAIN_EMOJI))
    while (menu := menu_select()) != "4":
        match menu:
            case "1":
                # intakes name of file to be read
                filename = input(
                    bidirectional_pad(
                        "Please enter the name of the text file you wish to cleanse of its sins",
                        MAIN_EMOJI,
                    )
                )
                # repetition in case 2
                lines = intake_name(filename)
                write_new_file(lines)

            case "2":
                # intakes text to be read
                # repetition in case 2
                lines = str(
                    input(
                        "\n\U0001F525 Please paste the text you wish to vanquish links from into the terminal (Right Click) \U0001F525\n"
                    )
                )
                write_new_file(lines)

            case "3":
                # appends new file to current file
                filename = input(
                    bidirectional_pad(
                        "Please enter the name of the text file you wish to cleanse of its sins and join in union with another cleansed file",
                        MAIN_EMOJI,
                    )
                )

                lines = intake_name(filename)

            case "4":
                print(bidirectional_pad("Fare thee well, Hero", MAIN_EMOJI))
                break

            case _:
                print(bidirectional_pad("Not a valid menu option", MAIN_EMOJI))


if __name__ == "__main__":
    main()

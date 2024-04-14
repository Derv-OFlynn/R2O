# Welcome to R2O. Please read README.md for more information

import os
import sys
from typing import List

MAIN_EMOJI = "\U0001F5CA" * ("--no-emojis" not in sys.argv)


def bidirectional_pad(text: str, pad: str, num: int = 1) -> str:
    return (pad * num) + text + (pad * num)

def colour_select() -> str:
    highlight_colour = ''
    red = '#FFB8EBA6'
    orange = '#FFB886CA6'
    yellow = '#FFF3A3A6'
    green = '#69E772'
    blue = '#69E7E4'
    purple = '#D2B3FFA6'

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


def slayer(lines) -> List[str]:
    """
    Intake a file object and a list of elements making of the contents of a previously read file.
    The user is promted to select which colour they want highlighted.
    Line by line, it replaces the first "==" if finds with the opening tag of the highlight colour and
    the second "==" is replaced by the closing tag of the highlight colour.
    """

    #Function to select highlight colour
    highlight_colour = colour_select()
    
    equal_count = 0
    new_text = []
    for line in lines:
        line = str(line)
        
        while line.find("==") != -1:
            if equal_count % 2 == 0:
                line = line.replace("==", '<mark style="background:'+ highlight_colour +';">', 1)
                equal_count += 1
            
            if equal_count % 2 == 1:
                line = line.replace("==", '</mark>', 1)
                equal_count += 1
        
        new_text.append(line)
        
    print(bidirectional_pad(f"{equal_count / 2} hightlights have been reformatted!", MAIN_EMOJI))
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

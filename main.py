import argparse

def main():
    """
    Entry point of the wc tool.
    
    Parses the command line arguments and counts the number of lines, words, and characters in a file.
    Prints the result based on the provided arguments.
    """
    parser = argparse.ArgumentParser(description="my wc tool")
    parser.add_argument('filename', type=str, help="The name of file that needs to be parsed")
    parser.add_argument('-l', '--lines', action='store_true', help="Count the number of lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count the number of words")
    parser.add_argument('-c', '--characters', action='store_true', help="Count the number of characters")

    args = parser.parse_args()
    filename = args.filename

    l, w, c = count(filename)
    result = {}

    if args.lines:
        result["lines"] = l
    if args.words:
        result["words"] = w
    if args.characters:
        result["characters"] = c

    if not (args.lines and args.words or args.characters):
        result = {"lines": l, "words": w, "characters": c}

    print(result)

def count(filename: str):
    num_lines, num_words, num_chars = 0,0,0
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            for line in lines:
                words = line.split()
                num_words+=len(words)
                for word in words:
                    num_chars+=len(word)

    except FileNotFoundError:
        print("File not found")

    except:
        print("There was an issue opening the file")

    return num_lines, num_words, num_chars

main()
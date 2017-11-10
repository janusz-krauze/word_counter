
import argparse

def count_lines(line):
    n_lines = 1
    return(n_lines)
    
def count_words(line):
    n_words = 0
    while "  " in line:
        line = line.replace("  "," ")
    words = line.strip().split(" ")
    if words != ['']:
        n_words += len(words)
    return(n_words)
    
def count_chars(line):
    n_chars = len(line) + 1
    return(n_chars)

def parse_args(params):
    parser = argparse.ArgumentParser(description='Count lines, words and characters.')
    parser.add_argument('file_path', type=str, help='name of the file to be counted')
    parser.add_argument('-l', dest= "lines", action="store_true", help='count lines')
    parser.add_argument('-c', dest= "characters", action="store_true", help='count chars')
    parser.add_argument('-w', dest= "words", action="store_true", help='count words')

    args = parser.parse_args(params)
    return(args)

def open_file(file_path):
    try:
        data_file = open(file_path, 'r')
        return(True, data_file)
    except OSError:
        return(False, 'File not found')

if __name__ == '__main__':
    args = parse_args('-l -w -c test_text.txt'.split())
    data_file = open_file(args.file_path)
    if data_file[0] == True:
        lines = 0
        words = 0
        chars = 0
        for data_line in data_file[1]:
            if args.lines:
                lines += count_lines(data_line)
            if args.words:
                words += count_words(data_line)
            if args.characters:
                chars += count_chars(data_line)
        if args.lines:
            print("Number of lines: " + str(lines))
        if args.words:
            print("Number of words: " + str(words))
        if args.characters:
            print("Number of characters: " + str(chars))
    else:
        print(data_file[1])

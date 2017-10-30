
import argparse

def count_lines(file_path):
    data_file = open(file_path, 'r')
    n_lines = 0
    for line in data_file:
        n_lines += 1
    data_file.close()
    return(n_lines)
    
def count_words(file_path):
    data_file = open(file_path, 'r')
    n_words = 0
    for line in data_file:
        while "  " in line:
            line = line.replace("  "," ")
        words = line.strip().split(" ")
        if words != ['']:
            n_words += len(words)
    data_file.close()
    return(n_words)
    
def count_chars(file_path):
    data_file = open(file_path, 'r')
    n_chars = 0
    for line in data_file:
        n_chars += len(line) + 1
    data_file.close()
    return(n_chars)

parser = argparse.ArgumentParser(description='Count lines, words and characters.')
parser.add_argument('file_path', type=str, help='name of the file to be counted')

args = parser.parse_args()

n_lines = count_lines(args.file_path)
n_words = count_words(args.file_path)
n_chars = count_chars(args.file_path)

print("Number of lines:", str(n_lines))
print("Number of words:", str(n_words))
print("Number of characters:", str(n_chars))


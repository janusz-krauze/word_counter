
import argparse

parser = argparse.ArgumentParser(description='Count lines, words and characters.')
parser.add_argument('file_path', type=str, help='name of the file to be counted')

args = parser.parse_args()

n_lines = 0
n_words = 0
n_chars = 0

data_file = open(args.file_path, 'r')

for line in data_file:
    n_chars += len(line) + 1
    while "  " in line:
        line = line.replace("  "," ")
    words = line.strip().split(" ")
    if words != ['']:
        n_words += len(words)
    n_lines += 1
    
data_file.close()    

print("Number of lines:", str(n_lines))
print("Number of words:", str(n_words))
print("Number of characters:", str(n_chars))


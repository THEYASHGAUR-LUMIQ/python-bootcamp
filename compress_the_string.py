# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def compress_the_string(string):
    res = itertools.groupby(string)
    for k, g in res:
        print((len(list(g)), int(k)), end=' ')

if __name__ == '__main__':
    string = input()
    compress_the_string(string)

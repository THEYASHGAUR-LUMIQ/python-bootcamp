def merge_the_tools(string, k):
    n = len(string)
    
    # Split string s into n/k substrings each of length k
    for i in range(0, n, k):
        substring = string[i:i+k]
        t = ""
        # Create string t by removing duplicates
        for char in substring:
            if char not in t:
                t += char
        print(t)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
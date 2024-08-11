# using __name__ variable
if __name__ == "__main__":
    
    # Taking the input from the user
    n, m = input().strip().split(' ')
    
    # storing the input as list
    n, m = [int(n), int(m)]
    arr = []
    
    # looping throug
    for arr_i in range(n):
         
       # taking the data from the user
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    
    # taking the input from user
    k = int(input().strip())
    
    # using the sorted function to sort
    sorted_arr = sorted(arr, key = lambda x : x[k])
    
    # using for loop to print the sorted values
    for row in sorted_arr:
        print(' '.join(str(y) for y in row))

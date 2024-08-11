t = int(input())

for _ in range(t):
    num, cubes = int(input()), list(map(int,input().split()))
    yes_no = "Yes"
    
    while len(cubes) > 1:
        if cubes[0] >= cubes[-1]:
            larger_num = cubes[0]
            cubes.pop(0)     
        else:
            larger_num = cubes[-1]
            cubes.pop(-1)  
        if larger_num < cubes[0] or larger_num < cubes[-1]:
            yes_no = 'No'
            break
            
    print(yes_no)

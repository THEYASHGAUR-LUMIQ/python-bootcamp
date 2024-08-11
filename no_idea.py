# Input reading
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Initialize happiness
happiness = 0

# Calculate happiness
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

# Output the final happiness
print(happiness)

import itertools

def find_probability(arr, k):
    # generate all possible combinations
    all_combinations = list(itertools.combinations(arr, k))
    # find total number of combinations
    total_combinations = len(all_combinations)
    # find number of combinations that satisfy the condition
    satisfied_combinations = len([x for x in all_combinations if 'a' in x])
    # find probability
    probability = satisfied_combinations / total_combinations
    # print probability
    print(round(probability, 4))
    
    

if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    k = int(input())

    find_probability(arr, k)

from datetime import datetime
import os

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Define the time format used in the input
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    # Parse the two timestamps using the given format
    time1 = datetime.strptime(t1, time_format)
    time2 = datetime.strptime(t2, time_format)
    
    # Calculate the absolute difference in seconds
    difference = abs(int((time1 - time2).total_seconds()))
    
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())  # Read number of test cases

    for _ in range(t):
        t1 = input().strip()  # Read first timestamp
        t2 = input().strip()  # Read second timestamp

        delta = time_delta(t1, t2)  # Compute the difference

        fptr.write(str(delta) + '\n')  # Write the result to the output file

    fptr.close()

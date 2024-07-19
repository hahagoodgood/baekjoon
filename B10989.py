import sys

def sort_small_memory():
    input_num = int(sys.stdin.readline().rstrip())
    arr = [0]*1001
    for i in range(input_num):
        num = int(sys.stdin.readline().rstrip())
        arr[num] += 1
    for i in range(1,1001):
        for j in range(arr[i]):
            sys.stdout.write(str(i)+'\n')

sort_small_memory()
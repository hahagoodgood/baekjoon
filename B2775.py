# a = list(range(1, 4))
# print(a)
# for i in range(1, 4):
#     print()
import sys
#inupt T
T = int(sys.stdin.readline())

test_cases = []
#input k, n
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    test_cases.append((k, n))

#loop the floor to calculate the number of people in each room
for test_case in test_cases:
    upper_floor = []
    current_floor = list(range(1, test_case[1]+1))
    for _ in range(test_case[0]):
        for i in range(test_case[1]):upper_floor.append(sum(current_floor[:i+1]))
        current_floor = upper_floor.copy()
        upper_floor = []

    # output
    sys.stdout.write(str(current_floor[-1])+"\n")
    sys.stdout.flush()

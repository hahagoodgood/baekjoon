import sys

def main():
    # input
    T = int(sys.stdin.readline())
    result = []
    for _ in range(T):
        # Initialize
        cnt = 0
        a, b, c= map(int, sys.stdin.readline().split())

        #Repeat 'a', 'b', 'c' to determine if the condition is satisfied
        for x in range(1,a+1):
            for y in (range(1,b+1)):
                for z in range(1,c+1):
                    if x%y == y%z == z%x:
                        cnt += 1
        result.append(cnt)
    # output
    for t in range(T): sys.stdout.write(f"{result[t]}\n")
if __name__ == '__main__':
    main()
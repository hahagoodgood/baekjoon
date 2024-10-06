#input, print의 속도를 빠르게 하기 위한 모듈
import sys

number = int(sys.stdin.readline().rstrip())
stack = []

for i in range(number):
    #명령어 입력
    answer = sys.stdin.readline().rstrip()
    # 명령어와 변수 분리
    list_answer = answer.split()

    match list_answer[0]:
        case "push":
            X = int(list_answer[-1])
            stack = stack + [X]
        case "pop":
            if len(stack) == 0:
                sys.stdout.write(str(-1) + '\n')
            else:
                result = stack[-1]
                stack = stack[:-1]
                sys.stdout.write(str(result) + '\n')
        case "size":
            sys.stdout.write(str(len(stack))+'\n')
        case "empty":
            if len(stack) == 0:
                sys.stdout.write(str(1) + '\n')
            else:
                sys.stdout.write(str(0) + '\n')
        case "top":
            if len(stack) == 0:
                sys.stdout.write(str(-1) + '\n')
            else:
                sys.stdout.write(str(stack[-1]) + '\n')
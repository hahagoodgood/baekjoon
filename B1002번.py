n = int(input()) 
x = list()
# print(x)
for i in range(n):
    x1, y1, r1, x2, y2, r2=map(int, input().split())
    pow_r = pow(r1+r2,2)
    len_dot = pow(x1-x2, 2)+pow(y1-y2, 2)
    # 0인 경우 
    # 떨어짐, 내원
    # 1개인 경우
    # 내접, 외접
    # 2개인경우
    # -1
    # 같음
    if pow_r < len_dot :
        x.append(0)
    elif pow_r == len_dot:
        x.append(1)
    else :
        if pow(r1-r2,2) > len_dot:
            x.append(0)
        elif pow(r1-r2,2) == len_dot:
            x.append(1)
        else :
            x.append(2)

for x_i in x :
    print(x_i)
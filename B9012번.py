# url:https://www.acmicpc.net/problem/9012

# vps인지 아닌지 확인
def is_vps(ps : str):
    '''
        parn_score : 여는 괄호일때 + 닫는 괄호일때 -

    '''
    parn_score =  0
    for i in ps:
        if parn_score >= 0:
            if i == '(':
                parn_score += 1
            elif i == ')':
                parn_score -= 1
        else : break

    if parn_score == 0:
        return True
    else :
        return False

T = int(input())
a = []

for i in range(T):
    a.append(input())
for i in range(T):
    if is_vps(a[i]):
        print("YES")
    else:
        print("NO")

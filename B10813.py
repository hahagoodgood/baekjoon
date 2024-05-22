# 1
n, m, *temp = map(int,input().split())
#basket = [i for i in range(1, n+1)]
basket = list(range(1, n+1))
for i in range(m):
    i, j, *temp = map(int,input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
print(*basket)

#2
n, m, *temp = map(int, input().split())
basket = list(range(1, n+1))
for _ in range(m):
    i, j, *temp = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
print(*basket)
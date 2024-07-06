def get_patten(a):
    last_num = a % 10
    patten = []
    current = last_num
    while current not in patten:
        patten.append(current)
        current = (current * last_num)%10
    return patten


T = int(input())
results = []
for i in range(T):
    a, b = map(int, input().split())
    patten = get_patten(a)
    if patten[0] == 0:
        results.append(10)
    else:
        results.append(patten[b%len(patten)-1])
    
for item in results:
    print(item)

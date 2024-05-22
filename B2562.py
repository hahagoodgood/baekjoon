#1

""" a = []
for i in range(9): a.append(int(input()))

Max = max(a)
index = a.index(Max)
print(Max)
print(index+1)
 """

#2
a = [int(input()) for i in range(9)]
print(f'{max(a)}\n{a.index(max(a))+1}')
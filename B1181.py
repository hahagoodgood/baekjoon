N = int(input())
str_list = [input() for _ in range(N)]
str_list.sort()
str_list.sort(key=len)
# print("#######################")
temp = ''
for item in str_list:
    if item != temp :
        print(item)
        temp = item

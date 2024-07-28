import sys

def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    else : 
       arr = quick_sort_step1(arr)
       pointItem = arr[0]
       NewArr = []
       temp = []
       for item in arr :
           if pointItem[0] == item[0] :
              temp.append(item)
           else :
               temp = quick_sort_step2(temp)
                ______여기까지_____________

def quick_sort_step1(arr):
    if len(arr) <= 1 :
        return arr
    else :
        pivot = arr[len(arr)//2]
        littleArr, equalArr, bigArr = [], [], []
        for item in arr :
            if item[0] < pivot[0]:
                littleArr.append(item)
            elif item[0] > pivot[0]:
                bigArr.append(item)
            else:
                equalArr.append(item)
    return quick_sort_step1(littleArr) + equalArr + quick_sort(bigArr)

def quick_sort_step2(arr):
    if len(arr) <= 1 :
        return arr
    else :
        pivot = arr[len(arr)//2]
        littleArr, equalArr, bigArr = [], [], []
        for item in arr :
            if item[1] < pivot[1]:
                littleArr.append(item)
            elif item[1] > pivot[1]:
                bigArr.append(item)
            else:
                equalArr.append(item)
    return quick_sort_step1(littleArr) + equalArr + quick_sort(bigArr)


N = int(sys.stdin.readline().rstrip())
schedule = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(N)]

print(N)
print(schedule)

print(quick_sort_step1(schedule))

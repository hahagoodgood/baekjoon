import sys

# 끝 시간을 기준으로 정렬
# def quick_sort_step1(arr):
#     if len(arr) <= 1 :
#         return arr
#     else :
#         pivot = arr[len(arr)//2]
#         littleArr, equalArr, bigArr = [], [], []
#         for item in arr :
#             if item[1] < pivot[1]:
#                 littleArr.append(item)
#             elif item[1] > pivot[1]:
#                 bigArr.append(item)
#             else:
#                 equalArr.append(item)
#     return quick_sort_step1(littleArr) + equalArr + quick_sort_step1(bigArr)

# # 끝 시간이 같은 것은 시작 시간을 기준으로 정렬
# def quick_sort_step2(arr):

#     def quick_sort_step3(arr):
#         if len(arr) <= 1 :
#             return arr
#         else :
#             pivot = arr[len(arr)//2]
#             littleArr, equalArr, bigArr = [], [], []
#             for item in arr :
#                 if item[0] < pivot[0]:
#                     littleArr.append(item)
#                 elif item[0] > pivot[0]:
#                     bigArr.append(item)
#                 else:
#                     equalArr.append(item)
#         return quick_sort_step3(littleArr) + equalArr + quick_sort_step3(bigArr)

#     temp_arr = []
#     new_arr = []      
#     for item in arr :
#         if len(temp_arr) == 0 or temp_arr[0][1] == item[1]:
#             temp_arr.append(item)
#         else : 
#             temp_arr = quick_sort_step3(temp_arr)
#             new_arr = new_arr + temp_arr
#             temp_arr = [item]
#     temp_arr = quick_sort_step3(temp_arr)
#     new_arr = new_arr + temp_arr
#     return new_arr

#그리드 알고리즘 이용하여 회의의 수를 계산한다. 
def cnt_max_mt(arr):
    cnt = 0
    end_time = 0
    for start, end in arr :
        if start >= end_time :
            end_time = end
            cnt += 1
            
    return cnt
            

N = int(sys.stdin.readline().rstrip())
schedule = [list(map(int, sys.stdin.readline().rstrip().split()))for _ in range(N)]

schedule.sort(key = lambda x: (x[1], x[0]))

# print(schedule)
sys.stdout.write(str(cnt_max_mt(schedule)) + '\n')
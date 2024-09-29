# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
from google.protobuf.internal.wire_format import INT64_MAX, INT32_MAX

# n = int(input())
# nmt = 1
# dmt = 1
# cnt = 1
# while 1:
#     if cnt == n: break
#     if (nmt+ dmt)%2 == 0:
#         while nmt != 1:
#             nmt -= 1
#             dmt += 1
#             cnt += 1
#             if cnt == n : break
#         if cnt == n: break
#         dmt += 1
#         cnt += 1
#         if cnt == n : break
#     else :
#         while dmt != 1:
#             nmt += 1
#             dmt -= 1
#             cnt += 1
#             if cnt == n : break
#         if cnt == n: break
#         nmt += 1
#         cnt += 1
#         if cnt == n : break
#
# print(str(nmt)+'/'+str(dmt))

while 1:
cnt = int(input())
lvl = sum  = 1
# for i in range(INT32_MAX):
#     sum += i
#     if sum >= cnt:
#         lvl = i
#         break
while lvl < 2*cnt/lvl-1:
    lvl += 1

n = cnt-(lvl-1)*lvl//2
if lvl%2 == 0:
    print(str(n)+'/'+str(lvl-n+1))
else:
    print(str(lvl-n+1) + '/' + str(n))
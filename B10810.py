# 1

# n, m = map(int,input().split())
#     # map(함수, 반복가능한 객체(iterable))형식으로 사용되며 함수에 
#     # 반복가능한 객체를 하나씩 대입하여 결과를 map객체로 출력한다
#     # input().split()으로 입력받은 문자열을 공백으로 쪼게어 리스트를 반환한다.
#     # 결국 int(str1)과 같은 함수를 반복하여 각각 n과 m에 입력된다.
# a = [0 for i in range(n)]
# for i in range(m):
#     i,j,k = map(int,input().split())
#     for i in range(i-1,j):
#         a[i] = k
# for i in range(n):
#     print(a[i], end=" ")

# 2
    
n, m, *a = map(int,input().split())
    # *a는 위에서 입력된 문자열 중 나머지를 저장하는 변수다
b=[0]*n
    # n 크기의 리스트를 모두 0으로 선언한다.
for idx in range(m):
    i, j, k =  map(int, input().split())
    b[i-1:j] = [k]*(j-i+1)
    # for 문으로 반복하지 않아도 b의 범위에서 K값을 넣어준다
print(*b)
    #*는 언패킹(unpacking) 여러 값을 변수에 할당하는 작업 iterable한 객체에서 요소를 추출하여 변수에 할당
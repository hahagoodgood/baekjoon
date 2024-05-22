""" N = 멀티텝 구멍의 횟수
K = 전기 용품 총 사용횟수
Ksch = 전기용품 스케줄 """

N, K = map(int,input().split())
kSch = list(map(int,input().split()))
# a = map(int,input().split())
# kSch = list(a)

mul = [0]*N

removeCnt = 0
#최적화 교체알고리즘
for idx in range(K):
    #mul안에 이미 제품을 사용 중일 때
    if kSch[idx] in mul:
        print(mul)
        continue
    #mul안에 0이 있을 때(멀티텝이 비어있을 때)
    elif 0 in mul:
        mul[mul.index(0)] = kSch[idx]
    else:
        #bsetIdx는 최적의 제거제품의 mul인덱스
        outChek = 0
        bestIdx = 0
        for chek in mul:
            if outChek == 0:
                if chek not in kSch[idx:K]:
                    bestIdx = mul.index(chek)
                    outChek = 1
                else:
                    KIdx = max(kSch.index(chek,idx), kSch.index(mul[bestIdx],idx))
                    bestIdx = mul.index(kSch[KIdx])
        mul[bestIdx]=kSch[idx]
        removeCnt += 1
    print(mul)

print(removeCnt)


#동적 계획법
# def remove(kSch):
#     for elecPd
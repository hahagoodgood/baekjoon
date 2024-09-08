# 계산값이 중복되는지 확인하며 중복되지 않았을때 배열에 추가
def result_append(result:int, results:list[int]):
    if len(results) <= 0:
        results.append(result)
    else:
        for i in results:
            if i == result:
                break
            elif results.index(i) == (len(results) - 1):
                results.append(result)
                break

# set함수의 존재를 모르는 상태에서 코드 작성
# 숫자 10개를 입력받는다
def main():
    a, results = [int(input()) for _ in range(10)], []
    for i in a:
        result =  i%42
        result_append(result, results)

    print(len(results))
def use_set():
    print(len(set([int(input()) for _ in range(10)])))

# main()
use_set()
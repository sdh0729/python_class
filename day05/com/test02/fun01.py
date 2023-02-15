# 고차함수: 매개인자를 함수를 갖는 함수
# map(func, *iterables)
# filter(function or None, iterable)--> filter object

if __name__ == '__main__':
    #l= [1,2,3,4]
    print(list(map(lambda x : x**2, range(1,10)))) #요소를 인덱스 순으로 입력을 받아 연산한 결과를 전체 목록 객체리턴
    print(list(filter(lambda x : x%2 == 0, range(1, 10)))) #짝수만 추출
# 내장함수를 이용한 매개인자를 활용해 보자
# sorterd(iterable, / , * key=None, reverse=False

'''
max(...)
   max(iterable, *[, default=obj, key=func]) ->value
   max(arg1, arg2, *args, *[,key=func]) ->value
min(...)
   min(iterable, *[, default=obj, key=func]) ->value
   min(arg1, arg2, *args, *[,key=func]) ->value
'''

if __name__ == '__main__':
    print(sorted([11,24,3,4,], reverse=True))
    print(sorted(['오늘은','불금','3','4','신난당' ], reverse=True))
    print(sorted(['오늘은', '불금', '3', '4', '신난당'], reverse=False))

    print("==================[sorted 키 값 지정]==============")
    print(sorted(['오늘은9999999','불금','3','4','신난당'], key=len, reverse=False))
    print(len('오늘은9999999'))

    print("==================[sorted 키 값 람다 지정]==============")
    print(sorted(['오늘은9999999', '불금', '38', '47', '신난당'], key=lambda x: x[1]))
    print(  (lambda x: x[1])('오늘은9999999'))


    print("==================[max 함수 키 값 람다 지정]==============")
    print(max([3,4,5,2,1,6,7,8], key = lambda x : x if x<6 else 0))
    print(max([3, 4, 5, 2, 1, 6, 7, 8], key=str))
    print(max([3, 4, 5, 2, 1, 6, 7, 8], key=int))







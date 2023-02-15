import calc

if __name__ == '__main__':
    print('모듈 경로 확인: ', calc)
    print('목록 확인: ', dir(calc))
    print(calc.__file__)
    print('모듈의 name = ', calc.__name__)
    print(calc.__package__)

    a=100
    b=50

    print(f'{a} + {b} = {calc.getHap(a,b)}')
    print(f'{a} - {b} = {calc.getSub(a, b)}')
    print(f'{a} * {b} = {calc.getMul(a, b)}')
    print(f'{a} / {b} = {calc.getDiv(a, b)}')

hap = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a,b : a/b


if __name__ == '__main__':

    a=100
    b=50
    print(f'{a} + {b} = {hap(a, b)}')
    print(f'{a} - {b} = {sub(a, b)}')
    print(f'{a} * {b} = {mul(a, b)}')
    print(f'{a} / {b} = {div(a, b)}')



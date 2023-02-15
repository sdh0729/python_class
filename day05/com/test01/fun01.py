def m_test(a,b):
    print(f'{a}  {b}')


def getTest(a, b):
    return a+b

my_getTest = lambda a,b=1 : a+b

if __name__ == '__main__':
    print(my_getTest(1))

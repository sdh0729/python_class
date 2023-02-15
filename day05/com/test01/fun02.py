odd_even = lambda x: 'even' if x % 2 == 0 else 'odd'


def oddeven(a):
    if a%2 == 0:
        return 'even'
    else :
        return 'odd'
if __name__ == '__main__':
    print(odd_even(4))
    oddeven(5)
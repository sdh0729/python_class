

def getA():
    return 100;
def getB():
    return [1,2,3,4,5];
def getC():
    return '삼성 멀티 캠퍼스';
def getD():
    return 97.9;
def getE():
    return (1,2,3,4,5);



if __name__ == '__main__':
    int_a = getA()
    print(int_a) #100
    print(getA()) #100
    float_b =getB()
    print(float_b) #[1,2,3,4,5]
    float_b = getC()
    print(float_b) #삼성 멀티 캠퍼스
    float_b = getD()
    print(float_b) # 97.9
    float_b = getE()
    print(float_b) # (1,2,3,4,5)

print(type(getA()))
print(type(getB()))
print(type(getC()))
print(type(getD()))
print(type(getE()))

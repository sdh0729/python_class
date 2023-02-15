def getTot(kor,eng,mat):
    res = kor + eng + mat
    return res

def getAvg(tot):
    res = tot/3
    return res

def getGrad(avg):
    if avg >=90:
        return 'A'
    elif avg < 90 and avg >= 80:
        return 'B'
    elif avg <80 and avg >= 70:
        return 'c'
    else:
        return 'F'

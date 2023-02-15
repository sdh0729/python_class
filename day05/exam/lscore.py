getTot = lambda x,y,z: x+y+z
getAvg = lambda x: x/3
getGrad = lambda x: 'A'if x >= 90 else ("B" if x >= 80 else "C" if x>=70 else "F")

name = input('input name: ')
kor = int(input('input kor: '))
eng = int(input('input eng: '))
mat = int(input('input mat: '))
Tot = getTot(kor,eng,mat)
avg = getAvg(Tot)
grad = getGrad(avg)
print(f'이름: {name}')
print(f'국어, 영어, 수학: {kor}, {eng}, {mat}')
print(f'총점, 평균, 학점: {Tot}, {avg}, {grad}')

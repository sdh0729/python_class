import score

name = input('input name: ')
kor = int(input('input kor: '))
eng = int(input('input eng: '))
mat = int(input('input mat: '))

Tot = score.getTot(kor,eng,mat)
avg = score.getAvg(Tot)
grad = score.getGrad(avg)

print(f'이름: {name}')
print(f'국어, 영어, 수학: {kor}, {eng}, {mat}')
print(f'총점, 평균, 학점: {Tot}, {avg}, {grad}')






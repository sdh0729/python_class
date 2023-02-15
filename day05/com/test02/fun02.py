# 파일 입출력
import io
import locale
# with ~as

def My_Write(file,content):
    f = open(file, mode= 'w')
    f.write(content)
    f.close()
def My_Read(file):
    f = open(file, mode= 'r')
    r=f.read()
    print(r)
    f.close()
if __name__ == '__main__':
    res = open('a.txt',mode='r')
    My_Write('b.txt', 'asdadasda')
    My_Read(('b.txt'))
    print('인코딩 확인 : ' ,locale.getpreferredencoding())


'''
    res03 = open('c.gif', mode='wb')
    print(res03, type(res03))

    res04 = open('d.jpg', mode='b+w')
    print(res04, type(res04))
'''

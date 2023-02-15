import random
import time
from tqdm import tqdm
from time import sleep

text=""
for char in tqdm(["a","b","c","d"]):
    sleep(0.25)
    text=text + char
def dataInput():
    data= input('data list(ex:a,b,c) : ' )
    return data.split(',')
def shake(list):
    random.shuffle(list)
    return list
list1= dataInput()
list2= dataInput()
shake(list1)
shake(list2)
print('shake for 3 seconds...')
time.sleep(3)
print('congratulations~~~')
for i in range(len(list1)):
    print(list1[i], '<---------->', list2[i])

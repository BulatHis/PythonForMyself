from datetime import datetime
import numpy
import pandas as pd

rtrt = list(range(1, 3))
rtrt2 = tuple(range(1, 3))

res = set(rtrt).issubset(set(rtrt2))

print(res)

print(-23 % 11)

dg = numpy.array([1, 3, 4])
gh = list[1, 3, 4]

print(id(dg))
print(id(gh))


def myDecorator(func):
    def inner():
        print(f'i gat it {res}')
        func()
        print('i made it %s' % res)

    return inner


@myDecorator
def DoSmf():
    print('yea {}'.format(res))


adff = list(range(5, 14, 4))
print(adff)

DoSmf()


class Car:

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed


def lol():
    print('sdfa')


dictr = (1, 2, 3)

print(list(map(lambda x: x * 2, dictr)))

car = Car(123, 321)

print(car.speed)

dictr = [1, 2, 3]
dictr2 = [4, 5, 6]

resss = all(elem in dictr for elem in dictr2)

print(resss)

abc = [tuple(dictr), tuple(dictr2)]

print(abc)

list = []
for i, j in zip(dictr, dictr2):
    list.append((i, j))

print(list)

print(dictr + dictr2)
dictr.extend(dictr2)
print(dictr)

qwe = {'c': 11, 'v': 1, 'a': 12, }

print(sorted(qwe.keys()))

stringf = "123a4532a1245"

''.join(stringf.split())

print(''.join(stringf.split("a")))

print(stringf.isalnum())


streg = 'dsaf'

print(hex(8))
import math


class myClass(object):

    def factorial(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    print(factorial(6))

    print(locals())


print(math.log(9, 3))

myList = list(range(1, 11))

print(list(filter(lambda x: x % 2 == 0, myList)))

myList.append(3)

print(myList)

# myList.remove(3)

del myList[0]
myList.extend(myList)

myList.insert(0, 1)

print(myList.sort(reverse=True))

print(myList)

newList = list(range(4))

newList.remove(1)
try:
    newList.remove(1)
except ValueError:
    print('all 1s are removed')

print(newList)

print(newList.__sizeof__())


def get_user():
    name = 'sad'
    age = 23
    return name, age


user = get_user()
print(type(user[0]))

mydic = {'Boby': 12, }
mydic["Dime"] = 12

mydic2 = dict(mydic)

mydic2['lol'] = 10
mydic2['Dime'] = 10

print(mydic2.update(mydic))



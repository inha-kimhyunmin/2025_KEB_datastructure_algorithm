import time


def time_decorator(func):
    def init(*args):
        s = time.time()
        r = func(*args)
        t = time.time()
        print(f"걸린 시간 : {t - s}")
        return r

    return init


def dectooct(number):
    if number > 0:
        return dectooct(number // 8) + f"{number % 8}"
    else:
        return ""


@time_decorator
def dectooct2(number):
    a = list()
    while (number > 0):
        a.append(number % 8)
        number = number // 8

    a.reverse()

    return ''.join(map(str, a))


num = int(input("Input Number : "))

# print(oct(num))

s = time.time()
print(dectooct(num))
r = time.time()
print(f"걸린 시간 : {r - s} \n")

print(dectooct2(num))

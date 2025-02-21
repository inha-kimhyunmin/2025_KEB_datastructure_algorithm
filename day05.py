import time
import random


def time_decorator(func):
    def wrapper(*arg):
        s = time.time()
        r = func(*arg)
        e = time.time()
        print(f"걸린 시간 : {e - s}s")
        return r

    return wrapper


@time_decorator
def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


@time_decorator
def my_sort(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[j] < l[i]:
                l[i], l[j] = l[j], l[i]
    return l


@time_decorator
def bubble_sort_improve(list):
    for i in range(len(list) - 1):
        no_swap = True
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                no_swap = False
        if no_swap:
            return list
    return list


@time_decorator
def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i - 1
        while j > 0 and list[j - 1] > value:
            list[j] = list[j - 1]
            j = j - 1
        list[j] = value
    return list


def quick_sort(list):  # 이 코드를 사용하면 중복을 허용하여 리스트를 만들었을 때 오류가 발생함
    n = len(list)

    if n <= 1:
        return list

    pivot = list[n // 2]
    left, right = list(), list()

    for num in list:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort_improvement(list):
    n = len(list)

    if n <= 1:
        return list

    pivot = list[n // 2]
    left = [x for x in list if x < pivot]
    mid = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]

    return quick_sort_improvement(left) + mid + quick_sort_improvement(right)

# groups = random.sample(range(1, 50000), 5000)
groups = [random.randint(1, 100000) for _ in range(10000)]
groups2 = groups[:]
groups3 = groups[:]
groups4 = groups[:]
groups5 = groups[:]
print(groups, "\n")
print(bubble_sort(groups))
print(bubble_sort_improve(groups2))
print(my_sort(groups3))
print(insertion_sort(groups4))

s = time.time()
print(quick_sort_improvement(groups5))
r = time.time()
print(f"걸린 시간 : {r - s}s")
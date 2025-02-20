def fibo_repetition(number: int) -> int:
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
    return a

memo = [None for _ in range(100)]
def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    if number < 2:
        result = number
    else:
        result = fibo_memoization(number-1) + fibo_memoization(number-2)
        memo[number] = result
    return result


print(fibo_repetition(40))
print(fibo_repetition(40))
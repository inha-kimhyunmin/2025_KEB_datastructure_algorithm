# dynamic programming
memo = dict()


def fibonacci_recursion(n) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)


def fibonacci_dp(n):
    """
    n번째 피보나치 수를 구하는 코드
    피보나치 함수 with 다이나믹 프로그래밍
    :param n: int
    :return: int
    """
    if n in memo: #key값이 memo안에 있는 경우
        return memo[n] #n값에 해당하는 value 리턴
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)
        return memo[n]


print(fibonacci_dp(30))
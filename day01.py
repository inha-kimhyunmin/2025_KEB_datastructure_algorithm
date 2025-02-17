def iseven(n):
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: boolean
    """
    return not(bool(n % 2))

def iseven2(n):
    """
    짝수 판정 함수 2번재
    :param n: 판정할 정수
    :return: boolean
    """
    return not(bool(n & 1))

def isodd(n):
    return bool(n & 1)


for i in range(1,20):
    print(f"{i}는 짝수인가? : {iseven(i)}, {iseven2(i)}")
    print(f"{i}는 홀수인가? : {isodd(i)}\n")
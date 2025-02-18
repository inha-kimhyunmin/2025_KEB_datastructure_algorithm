def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        # if char not in table:
        if char in table.values():  # "([{<"
            stack.append(char)
        elif char in table.keys():  # ")]}>"
            if not stack or table[char] != stack.pop(): #닫는게 있는데 여는게 없어 스택이 비어있거나, 닫는거랑 짝이 안맞으면
                return False
    return len(stack) == 0 #뭔가 남아있으면 짝이 안맞는거임 -> false


if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))

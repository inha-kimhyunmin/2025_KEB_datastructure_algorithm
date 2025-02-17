def print_poly(f_x, t_x) -> str:
    poly_expression = "f(x) = "

    for i in range(len(f_x)):
        coefficient = f_x[i]
        term = t_x[i]

        if coefficient > 0:
            if i > 0:
                poly_expression = poly_expression + "+"
            if i < len(f_x) - 1:
              poly_expression = poly_expression + f'{coefficient}x^{term} '
            else:
                poly_expression = poly_expression + f'{coefficient}'
        elif coefficient < 0:
            if i < len(f_x) - 1:
                poly_expression = poly_expression + f'{coefficient}x^{term} '
            else:
                poly_expression = poly_expression + f'{coefficient}'

    return poly_expression


def calculation_poly(x_value, f_x, t_x) -> int:
    return_value = 0

    for i in range(len(f_x)):
        coefficient = f_x[i]
        term = t_x[i]
        return_value += coefficient * pow(x_value, term)
    return return_value


fx = [2, 3, 4, -9]  # 계수
tx = [20, 7, 2, 0]  # 지수

if __name__ == "__main__":
    print(print_poly(fx, tx))
    print(calculation_poly(int(input("x 값 : ")), fx, tx))

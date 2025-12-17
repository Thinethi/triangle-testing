def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Triangle sides must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle")
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

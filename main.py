a = float(input("Введите коофицент для x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + (discriminant) ** 0.5) / (2 * a)
    x2 = (-b - (discriminant) ** 0.5) / (2 * a)
    print(f"The solutions are {x1} and {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"The solution is {x}")
else:
    real_part = -b / (2 * a)
    imaginary_part = ((abs(discriminant)) ** 0.5) / (2 * a) real_part = -b / (2*a)
    print(f"The solutions are {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
print("ax^2 + bx + c = 0")
while True:
    try:
        a = float(input("Enter a:"))
        b = float(input("Enter b:"))
        c = float(input("Enter c:"))
        dis = b**2 - 4*a*c
        if dis == 0:
            x = -b/(2*a)
            print("Equation has 2 identical roots x =", x)
        elif dis < 0:
            raise Exception ("The equation has no real roots because the discriminant is less than 0")
        else:
            x1 = (-b + dis**0.5)/(2*a)
            x2 = (-b - dis**0.5)/(2*a)
            print("x1 =", round(float(x1), 3), "x2 =", round(float(x2), 3))
        break
    except ValueError as e:
        print(e)
        print(ValueError)
        print('Enter number!')
    except ZeroDivisionError as ex:
        print(ex)
        print(ZeroDivisionError)

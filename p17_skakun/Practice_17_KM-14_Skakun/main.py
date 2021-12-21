from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, lg, ln


def get_cube_root(n):
    if n < 0:
        cube_root = root3(-n)
    else:
        cube_root = root3(n)
    return cube_root


def num_found(funct):
    if funct == 'exp' or funct == 'root3':
        while True:
            try:
                n = float(input('insert the number:'))
                break
            except:
                print('Enter the number correctly!')
        return n
    elif funct == 'root2' or funct == 'lg' or funct == 'ln':
        while True:
            try:
                n = float(input('Please enter a positive number:'))
                if n > 0:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        return n
    elif funct == 'fact':
        while True:
            try:
                n = int(input('Please enter a positive number:'))
                if n > 0:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        return n
    elif funct == 'log':
        while True:
            try:
                n = float(input('Please enter the base of the logarithm: '))
                base = float(input('Please enter an argument of the logarithm: '))
                if n > 0 and base > 0 and base != 1:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        return n, base


def main():
    while True:
        try:
            func = int(input(
                'Enter\n1 if you want to exponentiation the number;\n2 if you want to take the root of a number;\n3 if '
                'you want to find the factorial of a number;\n4 if you want to find the logarithm:'))
            if func == 1 or func == 2 or func == 3 or func == 4:
                break
            else:
                print('Enter the number correctly!')
        except:
            print('Enter the number correctly!')
    if func == 1:
        while True:
            try:
                exp = int(input(
                    'Enter\n1 if you want to find the square of a number\n2 if you want to calculate the cube of a '
                    'number:'))
                if exp == 1 or exp == 2:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        if exp == 1:
            num = num_found('exp')
            print('Number squared:', exp2(num))
        else:
            num = num_found('exp')
            print('Cube:', exp3(num))
    elif func == 2:
        while True:
            try:
                root = int(input('Enter\n2 to find the square root\n3 to find the cubic root:'))
                if root == 2 or root == 3:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        if root == 2:
            num = num_found('root2')
            print('Square root:', root2(num))
        else:
            num = num_found('root3')
            print('Cubic root:', get_cube_root(num))
    elif func == 3:
        num = num_found('fact')
        print('Factorial:', fact(num))
    else:
        while True:
            try:
                logar = int(input('Enter\n1 to find the logarithm;\n2 to find the decimal logarithm\n3 to find the '
                                  'natural logarithm:'))
                if logar == 2 or logar == 3 or logar == 1:
                    break
                else:
                    print('Enter the number correctly!')
            except:
                print('Enter the number correctly!')
        if logar == 1:
            num, base = num_found('log')
            print('logarithm: ', log(num, base))
        elif logar == 2:
            num = num_found('lg')
            print('Decimal logarithm: ', lg(num))
        else:
            num = num_found('ln')
            print('Natural logarithm:', ln(num))


if __name__ == '__main__':
    main()

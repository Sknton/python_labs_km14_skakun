while True:
    try:
        degree = int(input('Enter the degree of the polynomial (non-negative integer):'))
        if degree > 0:
            break
        else:
            print('Enter a non-negative number!')
    except:
        print('Enter the number correctly!')

def newton(degree):
    current_degree = 0
    degree_lst = [1]
    while current_degree <= degree:
        string = ''
        for i in degree_lst:
            string = string + ' ' + str(i)
        yield string
        current_degree += 1
        copy_lst = []
        for i in degree_lst:
            copy_lst.append(i)
        for i in range(len(copy_lst)):
            if i == len(degree_lst)-1 and len(degree_lst) >= 2:
                degree_lst[i] = copy_lst[i-1] + copy_lst[i]
                degree_lst.append(1)
            elif i == len(degree_lst)-1 and len(degree_lst) < 2:
                degree_lst.append(1)
            elif i == 0:
                degree_lst[0] = 1
            else:
                degree_lst[i] = copy_lst[i] + copy_lst[i-1]
        


for i in newton(degree):
    print(i)
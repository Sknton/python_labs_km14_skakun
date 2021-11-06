import numpy as np
import itertools
import math

while True:
    try:
        size_of_matr = int(input("Select matrix size (only positive integer):"))
        if size_of_matr < 0:
            print("You entered incorrectly.Size must be greater than 0 Try again!")
        else:
            break
    except:
        print("You entered incorrectly. Try again!")
def random_matrix(size_of_matr):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size = (size_of_matr, size_of_matr))
    print(matrix)
    return matrix
rang = list(range(0, size_of_matr))
def permutation_func(matr):
    """
    The function permutes all possible variants 
    of numbers from 1 to n (n is the size of the matrix)
    """
    permut = list(itertools.permutations(rang, size_of_matr))
    list_of_all_arg = []
    for index_2 in range(0, math.factorial(size_of_matr)):
        permut_x = list(permut[index_2])
        product_of_arg = []
        for index_1 in range(0, size_of_matr):
            ind = permut_x[index_1]
            a_xx = int([matr[index_1][ind]][0])
            product_of_arg.append(a_xx)           
        list_of_all_arg.append(product_of_arg)
    return list_of_all_arg
def product(pairs_for_the_prod):
    """The function finds the product of all pairs a_xx."""
    list_of_prod_a = []
    for i in range(0, math.factorial(size_of_matr)):
        prod_a = 1
        for a in rang:
            prod_a = prod_a*pairs_for_the_prod[i][a]
        list_of_prod_a.append(prod_a)
    permut = list(itertools.permutations(rang, size_of_matr))
    for ind in permut:
        x = 0
        for i in range(size_of_matr):
            for j in range(i+1, size_of_matr):
                if ind[i] > ind[j] :
                    x += 1
            if x%2 == 0: 
                sign = prod_a*1 
            else: 
                sign = prod_a*(-1)
            for k in range(0, math.factorial(size_of_matr)):
                list_of_prod_a[k] = list_of_prod_a[k]*sign
    return list_of_prod_a
def sum(list_of_prod_a):
    sum_=0
    for i in range(0, math.factorial(size_of_matr)):
        sum_ = sum_ + list_of_prod_a[i]
    return sum_





print(sum(product(permutation_func(random_matrix(size_of_matr)))))



def cons(head, tail = []):
    list_new = [head]
    for i in tail:
        list_new.append(i)
    return list_new

# ПЕРЕВІРКА

l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')


def sum(lst):
    if len(lst) == 0:
        return 0
    else:
        lst_rem = lst.pop(0)
        res = lst_rem + sum(lst)
        return res
# ПЕРЕВІРКА
#print(sum(l))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')
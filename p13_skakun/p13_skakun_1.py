lett = 'abcdefghijklmnopqrstuvwxyz'
list_of_let = list(lett)
text = ''
with open('gadsby.txt', 'r') as f:
    for line in f:
        text = text + (line.lower())
    summ = 0
    lst_of_count = []
    for i in list_of_let:
        summ = summ + text.count(i)
        lst_of_count.append(text.count(i))
    lst_of_prec = []
    for i in lst_of_count:
        lst_of_prec.append(round(i/summ*100, 3))
    lst_of_ind = []
    for i in range(len(list_of_let)):
        lst_of_ind.append(lst_of_prec.index(sorted(lst_of_prec, reverse = True )[i]))
    for i in lst_of_ind:
        print('letter', list_of_let[i], '=', lst_of_prec[i], '%')
    lst_of_five_ind =[]
    for i in range(0, 5):
        lst_of_five_ind.append(lst_of_prec.index(sorted(lst_of_prec, reverse = True )[i]))
    for i in range(-5, 0):
        lst_of_five_ind.append(lst_of_prec.index(sorted(lst_of_prec, reverse = True )[i]))
    print('five most used letters and five least used letters:')
    for i in lst_of_five_ind:
        print('letter', list_of_let[i], '=', lst_of_prec[i], '%')
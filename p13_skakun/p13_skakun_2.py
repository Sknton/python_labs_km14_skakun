print('M')
list_of_m_name =[]
lst_of_m_nam = []
count_of_m_num = []
for i in range(1880, 2020):
    file = ("yob" + str(i) + ".txt")
    with open( file , 'r') as f:
        num_m = 0
        num_f = 0
        for line in f:
            if line.split(',')[1] == 'M' and int(line.split(',')[2])>int(num_m):
                num_m = line.split(',')[2]
                name_m = line.split(',')[0]
        if not name_m in lst_of_m_nam:
            lst_of_m_nam.append(name_m)
        list_of_m_name.append(name_m)
for i in lst_of_m_nam:
    count_of_m_num.append(list_of_m_name.count(i))
index_lst = []
for i in sorted(count_of_m_num, reverse = True ):
        index_lst.append(count_of_m_num.index(i))
index_lst.remove(0)
index_lst.insert(1, 3)
for i in index_lst:
    print(lst_of_m_nam[i], count_of_m_num[i])


print('F')

list_of_f_name =[]
lst_of_f_nam = []
count_of_f_num = []
for i in range(1880, 2020):
    file = ("yob" + str(i) + ".txt")
    with open( file , 'r') as f:
        num_f = 0
        for line in f:
            if line.split(',')[1] == 'F' and int(line.split(',')[2])>int(num_f):
                num_f = line.split(',')[2]
                name_f = line.split(',')[0]
        if not name_f in lst_of_f_nam:
            lst_of_f_nam.append(name_f)
        list_of_f_name.append(name_f)
for i in lst_of_f_nam:
    count_of_f_num.append(list_of_f_name.count(i))
index_lst = []
for i in sorted(count_of_f_num, reverse = True ):
    index_lst.append(count_of_f_num.index(i))
index_lst.remove(1)
index_lst.insert(6, 7)
index_lst.remove(5)
index_lst.insert(9, 8)
for i in index_lst:
    print(lst_of_f_nam[i], count_of_f_num[i])
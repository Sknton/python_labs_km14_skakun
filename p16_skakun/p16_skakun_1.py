while True:
    try:
        num_page_in_book = int(input('Enter the number of pages in the book (it must be a multiple of 16 and not more than 1280):'))
        if num_page_in_book > 0 and num_page_in_book % 16 == 0 and num_page_in_book <= 1280:
            break
        else:
            print('Enter the number correctly!')
    except:
        print('Enter the number correctly!')

def one_lst(boole = True):
    def wrap(func):
        def wrapper(num_page_in_book):
            if boole:
                list_of_all_notebook_new = []
                if type(func(num_page_in_book)) == list:
                    for notebook in func(num_page_in_book):
                        notebook_lst = []
                        num_page = 0
                        for i in range(0, 4):
                            lst = []
                            for i in range(num_page, num_page + 4):
                                lst.append(notebook[i])
                            notebook_lst.append(lst)
                            num_page += 4
                        list_of_all_notebook_new.append(notebook_lst)
                    print('Notebooks:')
                    for i in list_of_all_notebook_new:
                        print (i)
                    print('Number of notebooks in the book:', len(func(num_page_in_book)))
                else:
                    for list_of_book in func(num_page_in_book):
                        for notebook in list_of_book:
                            notebook_lst = []
                            num_page = 0
                            for i in range(0, 4):
                                lst = []
                                for i in range(num_page, num_page + 4):
                                    lst.append(notebook[i])
                                notebook_lst.append(lst)
                                num_page += 4
                            list_of_all_notebook_new.append(notebook_lst)
                        print('Notebooks:')
                        for i in list_of_all_notebook_new:
                            print (i)
                        for list_of_book in func(num_page_in_book):
                            print('Number of notebooks in the book:', len(list_of_book))
                return list_of_all_notebook_new
            else:
                print('Notebooks:')
                if type(func(num_page_in_book)) == list:
                    for i in func(num_page_in_book):
                        print(i)
                    print('Number of notebooks in the book:', len(func(num_page_in_book)))
                for list_of_book in func(num_page_in_book):
                    for i in list_of_book:
                        print (i)
                    print('Number of notebooks in the book:', len(list_of_book))
                return list_of_book
        return wrapper
    return wrap

@one_lst(True)
def pagination(num_page_in_book):
    list_of_all_notebook = []
    num_page1 = 16
    num_page2 = 1
    num_page3 = 2
    num_page4 = 15
    for notebook in range(0, int(num_page_in_book/16)):
        notebook_list = []
        num_page1_cop = num_page1
        num_page2_cop = num_page2
        num_page3_cop = num_page3
        num_page4_cop = num_page4
        for page in range(0, 4):
            lst_of_page = [num_page1_cop, num_page2_cop, num_page3_cop, num_page4_cop]
            notebook_list.extend(lst_of_page)
            num_page1_cop -= 2
            num_page2_cop += 2
            num_page3_cop += 2
            num_page4_cop -= 2
        list_of_all_notebook.append(notebook_list)
        num_page1 += 16
        num_page2 += 16
        num_page3 += 16
        num_page4 += 16
    return list_of_all_notebook


# @one_lst()
# def gener(num_page_in_book):
#     list_of_all_notebook = []
#     def gener_notebooks(n):
#         for n in range(0, int(num_page_in_book/16)):
#             num_page1 = 16 + 16*n
#             num_page2 = 1 + 16*n
#             num_page3 = 2 + 16*n
#             num_page4 = 15 + 16*n
#             notebook_list = []
#             for page in range(0, 4):
#                 lst_of_page = [num_page1, num_page2, num_page3, num_page4]
#                 notebook_list.extend(lst_of_page)
#                 num_page1 -= 2
#                 num_page2 += 2
#                 num_page3 += 2
#                 num_page4 -= 2
#             yield notebook_list
#     for n in gener_notebooks(0):
#         list_of_all_notebook.append(n)
#     yield list_of_all_notebook



#print(gener(num_page_in_book))
print(pagination(num_page_in_book))


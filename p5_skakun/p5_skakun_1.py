salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
length = len(salary_list)
index_list = []
new_salary_list = []
for i in range(length):
    new_salary = (round(salary_list[i]*1.3, 2))
    new_salary_list.append(new_salary)
    index = float(new_salary_list[i]) - float(salary_list[i])
    index_list.append(round(index, 2))
print("Salary table:")
for i in range(length):
    print(salary_list[i], new_salary_list[i], index_list[i] )

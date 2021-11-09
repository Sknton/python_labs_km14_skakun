salary_list = [7.3, 8.5, 11, 12.7, 15.2, 21.12, 27.35]
length = len(salary_list)
new_salary_list = list(map(lambda a: round(a*1.3, 2), salary_list))
index_list = list(map(lambda a, b: round(a - b, 2), new_salary_list, salary_list ))
print("Salary table:")
for i in range(length):
    print(salary_list[i], new_salary_list[i], index_list[i] )
import numpy as np

years = np.arange(1900, 2020+3, 1)
while True:
    year = (input("Enter the year(1900 to 2022):"))
    month = (input("Enter the month(1 to 12):"))
    if len(list(year)) == 4 and len(list(month)) == 1 or len(list(month)) == 2 and int(year) >= 1900 and int(year) <= 2022 and int(month) >= 1 and int(month) <= 12:
        try:
            year = int(year)
            month = int(month)
            break
        except:
            print("You entered incorrectly. Please try again!")
    else:
        print("You entered incorre. Please try again!")
def leap_year_detector(years):
    leap_years = list(filter(lambda year: year % 400 == 0, years))
    years_that_remain1 = []
    for i in years:
        if i in leap_years:
            continue
        else:
            years_that_remain1.append(i)
    no_leap_years = list(filter(lambda year: year % 100 == 0, years_that_remain1))
    years_that_remain3 = []
    for i in years_that_remain1:
        if i in no_leap_years:
            continue
        else:
            years_that_remain3.append(i)
    leap_years_4 = list(filter(lambda year: year % 4 == 0, years_that_remain3))
    years_that_remain4 = []
    for i in years_that_remain3:
        if i in leap_years_4:
            continue
        else:
            years_that_remain4.append(i)
    leap_years.extend(leap_years_4)
    no_leap_years.extend(years_that_remain4)
    return(leap_years, no_leap_years)

def number_of_days_in_a_month(years, func, year, month):
    tuple_of_years = func(years)
    months_days_31 = [1, 3, 5, 7, 8, 10, 12]
    months_days_30 = [4, 6, 9, 11]
    months_days_28_or_29 = [2]
    if year in tuple_of_years[1] and month in months_days_31:
        print("Month number", month, "in", year, "has 31 days")
    elif year in tuple_of_years[1] and month in months_days_30:
        print("Month number", month, "in", year, "has 30 days")
    elif year in tuple_of_years[1] and month in months_days_28_or_29:
        print("Month number", month, "in", year, "has 29 days")
    elif year in tuple_of_years[2] and month in months_days_30:
        print("Month number", month, "in", year, "has 30 days")
    elif year in tuple_of_years[2] and month in months_days_31:
        print("Month number", month, "in", year, "has 31 days")
    elif year in tuple_of_years[2] and month in months_days_30:
        print("Month number", month, "in", year, "has 28 days")

number_of_days_in_a_month(years, leap_year_detector, year, month )
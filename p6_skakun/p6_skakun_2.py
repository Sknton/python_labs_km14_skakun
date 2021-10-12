province = {'A' : 'Newfoundland',
'B':'Nova Scotia',
'C' : 'Prince Edward Island',
'E' : 'New Brunswick',
'G' : 'Quebec',
'H' : 'Quebec',
'J' : 'Quebec',
'K' : 'Ontario',
'L' : 'Ontario',
'M' : 'Ontario',
'N' : 'Ontario',
'P' : 'Ontario',
'R' : 'Manitoba',
'S' : 'Saskatchewan',
'T' : 'Alberta',
'V' : 'British Columbia',
'X' : 'Nunavut or Northwest Territories',
'Y' : 'Yukon'}
while True:
    postcode = input("Please, enter postal code:")
    postcode_list = list(postcode.upper())
    if len(postcode) == 3 and postcode_list[0].isalpha() and postcode_list[1].isdigit() and postcode_list[2].isalpha() and postcode_list[0] in province:
        print("You have entered the correct index!")
        break
    else:
        print("You entered an invalid postcode")
        print("To try again, press 1")
        while True:
            ans = input()
            if int(ans) == 1:
                break
            else:
                print("Invalid answer. Enter again")
if postcode_list[0] in province and postcode_list[1] == 0:
    print("Сountryside in the province", province[postcode_list[0]])
else:
    print("City in the province", province[postcode_list[0]])
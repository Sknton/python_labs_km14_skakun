phrase1 = input("Enter first phrase (only letters):")
phrase2 = input("Enter second phrase (only letters):")
list_of_letters1 = {' '}
list_of_letters2 = {' '}
list_from_phrase1 = list(phrase1.lower())
list_from_phrase2 = list(phrase2.lower())
list_of_letters1.update(list_from_phrase1)
list_of_letters2.update(list_from_phrase2)
print("First phrase letters:", list(phrase1.lower()))
print("Second phrase letters:", list(phrase2.lower()))
if list_of_letters1 & list_of_letters2 == list_of_letters2:
    print("You can make a second phrase from the letters of the first")
else:
    print("You cannot make a second phrase from the letters of the first")
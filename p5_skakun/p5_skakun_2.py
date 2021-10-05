while True:
    try:
        num_words = int(input("The number of words you want to enter:"))
        break
    except ValueError:
        print("Invalid format. Enter an integer value.")
words = []
for i in range(0, num_words):
    a = input("Enter a word:")
    words.append(a)
length = len(words)
for i in range(length):
    if i != length - 2 and i != length - 1:
        print(words[i], end = ", ")
    elif i == length - 2:
        print(words[i], end = " and ")
    else:
        print(words[i], end = ".")
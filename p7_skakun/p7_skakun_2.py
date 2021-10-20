while True:    
    try:
        r = int(input("Enter the value of red (Integer from 0 to 255): "))
        g = int(input("Enter the value of green (Integer from 0 to 255): "))
        b = int(input("Enter the value of blue (Integer from 0 to 255): "))
    except ValueError:
        print("Invalid format. Enter the value in numbers.")
    if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
        print("You entered the wrong number!")
    else:
        break
r_int_part = int(r / 16)
r_fractional_part = r / 16 - int(r / 16)
if r_int_part == 10:
    r_16_1 = 'A'
elif r_int_part == 11:
    r_16_1 = 'B'
elif r_int_part == 12:
    r_16_1 = 'C'
elif r_int_part == 13:
    r_16_1 = 'D'
elif r_int_part == 14:
    r_16_1 = 'E'
elif r_int_part == 15:
    r_16_1 = 'F'
else:
    r_16_1 = str(r_int_part)
r_frac_16 = r_fractional_part * 16
if r_frac_16 == 10:
    r_16_2 = 'A'
elif r_frac_16 == 11:
    r_16_2 = 'B'
elif r_frac_16 == 12:
    r_16_2 = 'C'
elif r_frac_16 == 13:
    r_16_2 = 'D'
elif r_frac_16 == 14:
    r_16_2 = 'E'
elif r_frac_16 == 15:
    r_16_2 = 'F'
else:
    r_16_2 = str(int(r_frac_16))
r_16 = r_16_1 + r_16_2
g_int_part = int(g / 16)
g_fractional_part = g / 16 - int(g / 16)
if g_int_part == 10:
    g_16_1 = 'A'
elif g_int_part == 11:
    g_16_1 = 'B'
elif g_int_part == 12:
    g_16_1 = 'C'
elif g_int_part == 13:
    g_16_1 = 'D'
elif g_int_part == 14:
    g_16_1 = 'E'
elif g_int_part == 15:
    g_16_1 = 'F'
else:
    g_16_1 = str(g_int_part)
g_frac_16 = g_fractional_part * 16
if g_frac_16 == 10:
    g_16_2 = 'A'
elif g_frac_16 == 11:
    g_16_2 = 'B'
elif g_frac_16 == 12:
    g_16_2 = 'C'
elif g_frac_16 == 13:
    g_16_2 = 'D'
elif g_frac_16 == 14:
    g_16_2 = 'E'
elif g_frac_16 == 15:
    g_16_2 = 'F'
else:
    g_16_2 = str(int(g_frac_16))
g_16 = g_16_1 + g_16_2
b_int_part = int(b / 16)
b_fractional_part = b / 16 - int(b / 16)
if b_int_part == 10:
    b_16_1 = 'A'
elif b_int_part == 11:
    b_16_1 = 'B'
elif b_int_part == 12:
    b_16_1 = 'C'
elif b_int_part == 13:
    b_16_1 = 'D'
elif b_int_part == 14:
    b_16_1 = 'E'
elif b_int_part == 15:
    b_16_1 = 'F'
else:
    b_16_1 = str(b_int_part)
b_frac_16 = b_fractional_part * 16
if b_frac_16 == 10:
    b_16_2 = 'A'
elif b_frac_16 == 11:
    b_16_2 = 'B'
elif b_frac_16 == 12:
    b_16_2 = 'C'
elif b_frac_16 == 13:
    b_16_2 = 'D'
elif b_frac_16 == 14:
    b_16_2 = 'E'
elif b_frac_16 == 15:
    b_16_2 = 'F'
else:
    b_16_2 = str(int(b_frac_16))
b_16 = b_16_1 + b_16_2
print ("Hexadecimal representation of color: #" + r_16.zfill(2) + g_16.zfill(2) + b_16.zfill(2) )
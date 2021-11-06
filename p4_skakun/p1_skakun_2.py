try:
    speed = int(input('Enter wind speed (km/h):'))
    if speed > 0 and speed < 137:
        print('Potential damage minor!')
    elif speed >= 137 and speed < 177:
        print('Potential damage moderate!')
    elif speed >= 177 and speed < 217:
        print('Potential damage considerable!')
    elif speed >= 217 and speed < 266:
        print('Potential damage severe!')
    elif speed >= 266 and speed < 322:
        print('Potential damage devastating!')
    elif speed > 322:
        print('Potential damage incredible!')
    else:
        print('You enter incorrectly!')
except:
    print('You enter incorrectly!!!')

for i in range(1000, 9999):
    my_string = str(i)

    ilkIkiBas = int(my_string[0]) + int(my_string[1])
    sonIkiBas = int(my_string[2]) + int(my_string[3])

    if ilkIkiBas == sonIkiBas:
        print(i)
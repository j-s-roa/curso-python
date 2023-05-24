def es_bisiesto():
    year = int(input("Ingresa el año: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('es biciesto')
                return True

            else:
                print('No es biciesto')
                return False
        else:
            print('es biciesto')
            return True

    else:
        print('No es biciesto')
        return False

print(es_bisiesto())
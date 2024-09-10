# Geg. : Temperatur in Grad Celsius C
# Geg. : Temperatur in Grad Kelvin K
# K = C + 273.15

def choose_unit():
    print("\nWelche Temperatur möchtest du Umrechnen?")
    E = input("\nCelsius zu Kelvin = 1\nKelvin zu Celsius = 2\nCelsius zu Fahrenheit = 3\
              \nFahrenheit zu Celsius = 4\nKelvin zu Fahrenheit = 5\nFahrenheit zu Kelvin = 6\n")
    if E == '1':
        get_temperature_C_K()
    elif E == '2':
       get_temperature_K_C()
    elif E == '3':
        get_temperature_C_F()
    elif E == '4':
        get_temperature_F_C()
    elif E == '5':
        get_temperature_K_F()
    elif E == '6':
        get_temperature_F_K() 


def get_temperature_F_K():
        while True:
            F = input("Gib die Temperatur in Grad Fahrenheit ein: ")
            if F == isinstance(float):
                K = (F - 32) * 5/9 + 273.15
                print("Das sind " + str(K) + " Kelvin")
            else:
                print("Das ist keine gültige Angabe für eine Temperatur")
        

def get_temperature_K_F():
    while True:
        K = input("Gib die Temperatur in Grad Kelvin ein: ")
        try:
            K = float(K)
            F = (K - 273.15) * 9/5 + 32 
            print("Das sind " + str(F) + " Fahrenheit")
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur")


def get_temperature_F_C():
    while True:
        F = input("Gib die Temperatur in Grad Fahrenheit ein: ")
        try:
            F = float(F)
            return F
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur")


def get_temperature_C_F():
    while True:
        C = input("Gib die Temperatur in Grad Celsius ein: ")
        try:
            C = float(C)
            return C
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur")


def get_temperature_K_C():
    while True:
        K = input("Gib die Temperatur in Grad Kelvin ein: ")
        try: 
            K = float(K)
            return K
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur")


def get_temperature_C_K():
    while True:
        C = input("Gib die Temperatur in Grad Celsius ein: ")
        try:
            C = float(C)
            return C
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur")


def convert_to_kelvin(F):
    K = F + 273.15
    return K


def convert_to_celsius(K):
    C = K - 273.15
    return C


def convert_to_kelvin(C):
    K = C + 273.15
    return K




if __name__ == "__main__":
    

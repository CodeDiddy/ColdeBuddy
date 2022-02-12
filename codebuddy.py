# Maak een functie die de code voor het maken van een variabele genereert en weergeeft. 
# Aan de functie kan de gebruiker meegeven van welk datatype de variabele is en wat je in de variabele stopt. 
# Implementeer minstens de volgende soorten data: string, number, boolean.

def inhoud_variabele(soort_variabele):
    """
    Input: type variabele
    gebruiker kan naam variabele invullen
    gebruiker kan variabele vullen
    functie controleert of inhoud overeenkomt met het type variabele
    Output: een tuple met de soort variabele, naam van de variabele en de inhoud van de variabele.
    """
    while True:
        naam = input("Welke naam wil je meegeven aan je variabele? (begin je variabele met een kleine letter of een underscore _): \n").strip().replace(' ', '_')
        if naam[0] not in '_abcdefghijklmnopqrstuvwxyz':
            print("Dat is geen geldige naam, probeer opnieuw~")
            continue
        inhoud = input(f"Wat wil je in de variabele opslaan? ({soort_variabele}): \n")
        if soort_variabele == 'number':
            try:
                float(inhoud)
                return (soort_variabele, naam, inhoud)
            except:
                print("Dat is geen 'number', probeer opnieuw! \n")
        elif soort_variabele == 'boolean':
            if (inhoud.lower() == 'true') | (inhoud.lower() == 'false'):
                return (soort_variabele, naam, inhoud.capitalize())
            else:
                print("Dat is geen 'boolean', probeer opnieuw! \n")
        else:
            return (soort_variabele, naam, inhoud)
        

def maak_variabele():
    """
    Input: -
    Gebruiker wordt gevraagd om een type variabele aan te maken
    Functie controleerd of het een geldig type is
    Output: type variabele
    """
    flag = True
    geldige_variabelen = ['string', 'number', 'boolean']

    while flag:
        soort = input("Welke soort variabele wil je opgeven? (string, number, boolean): \n").lower()
        if soort in geldige_variabelen:
            flag = False
            return soort
        else:
            print(f"{soort} is geen geldige soort variabele")


# Maak een functie die de code voor een simpele for-loop voor je genereert en toont. 
# Aan de functie kan de gebruiker meegeven hoeveel iteraties de loop doet. 
# De body (wat tijdens de loop wordt uitgevoerd) van de for-loop mag je nog leeg laten.
        
def maak_loop():
    while True:
        aantal = input('Hoevaak wil je de loop herhalen?\n')
        try:
            int(aantal)
            return f"for i in range({aantal}):\n    <vul hier je code>"
        except:
            "Vul aub een heel getal in!"

def print_menu():
    print('v om een variabele aan te maken')
    print('l om een loop te maken')
    print('q om het programma te stoppen')
    keuze = input('Maak uw keuze: ')
    return keuze

def menu():
    variabelen = []
    loops = []
    while True:
        keuze = print_menu()
        if keuze == 'q':
            if len(variabelen) > 0:
                print('\nJe hebt de volgende variabelen aangemaakt:')
                for variabele in variabelen:
                    print(f"Type {variabele[0]}:\n {variabele[1]} {variabele[2]}")
            if len(loops) > 0:
                print('\nJe hebt de volgende loops aangemaakt:')
                for loop in loops:
                    print(loop)
                    print(' ')

            print('\nBedankt en tot ziens!')
            exit()
        if keuze.lower() == 'v':
            v = inhoud_variabele(maak_variabele())
            variabelen.append(v)
            print(' ')
            print(v)
            print(' ')
        elif keuze.lower() == 'l':
            l = maak_loop()
            loops.append(l)
            print(' ')
            print(l)
            print(' ')
        else:
            print('Dat is geen geldige keuze, probeer opnieuw!')

menu()

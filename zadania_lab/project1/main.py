# zadanie 1 i zadanie 2:
def polacz(litera, nazwisko):
    litera = str(litera)
    nazwisko = str(nazwisko)
    wynik = litera[0].upper() + "." + nazwisko[0].upper() + nazwisko[1:]
    return wynik


# zadanie 3:
def wiek(poczatek, koniec, lata):
    if not str(poczatek).isdigit() or not str(koniec).isdigit() or not str(lata).isdigit():
        print("zle dane wiek()")
        return "zle dane"
    rok = int(str(poczatek) + str(koniec))
    wynik = rok - int(lata)
    return wynik


# zadanie 4:
def magia(imie, nazwisko, funkcja):
    return funkcja(imie, nazwisko)


# zadanie 5:
def dzielenie(pierwsza, druga):
    if pierwsza > 0 and druga > 0:
        return pierwsza / druga


# zadanie 6:
def liczenie():
    wynik = 0
    while wynik < 100:
        temp = input(f"prosze podaj liczbe, aktualna suma: {wynik}>")
        if temp.lstrip("-").isdigit():
            wynik += int(temp)
        else:
            print("zle dane")
    print(f"ostateczna suma to: {wynik}")


# zadanie 7:
def lista_do_krotki(lista):
    return tuple(lista)


# zadanie 8:
def lista_w_petli():
    lista = []
    while len(lista) < 4:
        x = input(f"dodaj cos do listy, masz jeszcze: {4 - len(lista)} wolnych miejsc\n>>")
        lista.append(x)
    return tuple(lista)


# zadanie 9:
def dzien(n: int) -> str:
    dni = {
        1: "Poniedzialek",
        2: "Wtorek",
        3: "Sroda",
        4: "Czwartek",
        5: "Piatek",
        6: "Sobota",
        7: "Niedziela"
    }
    return dni[n]


# zadanie 10:
def palindrom(tekst: str) -> bool:
    return tekst == tekst[::-1]

def buble(tablica):
    dl = len(tablica) - 1
    ilosc = 0
    for y in range(dl):
        zmiana = False
        for x in range(dl):
            ilosc += 1
            if tablica[x] < tablica[x+1]:
                temp = tablica[x]
                tablica[x] = tablica[x+1]
                tablica[x+1] = temp
                zmiana = True
        if zmiana is False:
            break
    print("\ntablica babelkowania: " + str(tablica))
    print("ilosc operacji babelkowania: " + str(ilosc))


def selection(tablica):
    dl = len(tablica)
    ilosc = 0
    for y in range(dl):
        min_index = y
        for x in range(min_index, dl):
            ilosc += 1
            if tablica[min_index] < tablica[x]:
                temp = tablica[x]
                tablica[x] = tablica[min_index]
                tablica[min_index] = temp
    print("\ntablica wybierania: " + str(tablica))
    print("ilosc operacji wybierania: " + str(ilosc))


def insertion(tablica):
    dl = len(tablica)
    ilosc = 0
    for i in range(1, dl):
        key = tablica[i]
        j = i - 1
        while j >= 0 and tablica[j] < key:
            ilosc += 1
            tablica[j + 1] = tablica[j]
            j = j-1
            tablica[j + 1] = key
    print("\ntablica wstawiania: " + str(tablica))
    print("ilosc operacji wstawiania: " + str(ilosc))


def sortowanie(tablica):
    temp = tablica.copy()
    buble(tablica)
    tablica = temp.copy()
    selection(tablica)
    tablica = temp.copy()
    insertion(tablica)
    print("\n\n")


sortowanie([6, 1, 7, 3, 4, 9, 2, 5, 8, 0])
sortowanie([8, 5, 4, 2, 1, 7, 9, 6, 0, 3])
sortowanie([3, 4, 0, 7, 1, 5, 2, 8, 9, 6])
sortowanie([3, 4, 1, 2, 5, 0, 9, 8, 6, 7])
sortowanie([3, 5, 8, 7, 1, 6, 9, 4, 0, 2])
sortowanie([0, 7, 9, 4, 8, 6, 5, 3, 2, 1])
sortowanie([9, 2, 1, 5, 8, 0, 6, 4, 3, 7])
sortowanie([4, 5, 2, 7, 0, 9, 1, 3, 6, 8])
sortowanie([0, 8, 2, 7, 6, 3, 9, 1, 5, 4])
sortowanie([2, 0, 7, 3, 4, 5, 8, 6, 9, 1])
sortowanie([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

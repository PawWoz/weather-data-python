import csv
import matplotlib.pyplot as plt


class DanePogodowe:
    def __init__(self, stacja, data_pomiaru, temperatura, predkosc_wiatru,
                 wilgotnosc_wzgledna, suma_opadu):
        self.stacja = stacja
        self.data_pomiaru = data_pomiaru
        self.temperatura = temperatura
        self.predkosc_wiatru = predkosc_wiatru
        self.wilgotnosc_wzgledna = wilgotnosc_wzgledna
        self.suma_opadu = suma_opadu

def czytaj_dane(nazwa_pliku):
    dane_pogodowe = []
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as file:
            czytnik = csv.reader(file, delimiter=',')
            next(czytnik)  # Pominięcie pierwszego wiersza
            for wiersz in czytnik:
                # tworzenie obiektu dla kazdego wiersza
                dane = DanePogodowe(wiersz[0], wiersz[1], wiersz[2], wiersz[3], wiersz[4], wiersz[5])
                dane_pogodowe.append(dane)
    except FileNotFoundError:
        print(f'Plik {nazwa_pliku} nie został znaleziony')
    return dane_pogodowe

def srednia_temperatura(dane_pogodowe):
    temperatury = [float(dane.temperatura) for dane in dane_pogodowe if dane.temperatura != '']
    if len(temperatury) == 0:
        return 0
    return sum(temperatury) / len(temperatury)

def max_predkosc_wiatru(dane_pogodowe):
    predkosci_wiatru = [int(dane.predkosc_wiatru) for dane in dane_pogodowe if dane.predkosc_wiatru != '']
    if len(predkosci_wiatru) == 0:
        return 0
    return max(predkosci_wiatru)

def min_opad_deszczu(dane_pogodowe):
    opad_deszczu = [float(dane.suma_opadu) for dane in dane_pogodowe if dane.suma_opadu != '']
    if len(opad_deszczu) == 0:
        return 0
    return min(opad_deszczu)

def wykres_wilgotnosci(dane_pogodowe):
    wilgotnosci = [float(dane.wilgotnosc_wzgledna) for dane in dane_pogodowe if dane.wilgotnosc_wzgledna != '']
    if len(wilgotnosci) == 0:
        return
    plt.plot(wilgotnosci)
    plt.title('Wilgotność')
    plt.xlabel('Pomiar na przestrzeni czasu')
    plt.ylabel('Wilgotność (%)')
    plt.show()


def zapisz_dane(nazwa_pliku, srednia_temperatura, max_predkosc_wiatru, min_opad_deszczu):
    try:
        with open(nazwa_pliku, 'w') as file:
            file.write(f'Średnia temperatura: {srednia_temperatura:}\n')
            file.write(f'Max prędkość wiatru: {max_predkosc_wiatru}\n')
            file.write(f'Min opady deszczu: {min_opad_deszczu}\n')
    except IOError:
        print(f'Błąd zapisu danych {nazwa_pliku}')


if __name__ == '__main__':
    dane_pogodowe = czytaj_dane('dane_pogoda.txt')
    if len(dane_pogodowe) > 0:
        srednia_temp = srednia_temperatura(dane_pogodowe)
        max_wiatr = max_predkosc_wiatru(dane_pogodowe)
        min_opad = min_opad_deszczu(dane_pogodowe)
        wykres_wilgotnosci(dane_pogodowe)
        zapisz_dane('wyniki.txt', srednia_temp, max_wiatr, min_opad)
    else:
        print('Brak danych do analizy')


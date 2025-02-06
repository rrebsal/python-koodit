#1
vuodenajat = {
    12: "talvi", 1: "talvi", 2: "talvi",
    3: "kevät", 4: "kevät", 5: "kevät",
    6: "kesä", 7: "kesä", 8: "kesä",
    9: "syksy", 10: "syksy", 11: "syksy"
}

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan {vuodenajat[kuukausi]}.")
else:
    print("Virheellinen syöte. Anna numero välillä 1-12.")

#2
nimi = set()

while True:
    inpnimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if inpnimi in nimi:
        print("Nimi on jo listalla")
    else:
        print("Uusi nimi lisätty listaan.")
        nimi.add(inpnimi)

print("\nSyötetyt nimet:")
for nimi in inpnimi:
    print(nimi)

#3
lentokentat = {}

while True:
    print("\nValitse toiminto:")
    print("1 - Lisää uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")

    valinta = input("Anna valinta (1-3): ").strip()

    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
        nimi = input("Anna lentoaseman nimi: ").strip()
        lentokentat[icao] = nimi
        print(f"Lentoasema {nimi} (ICAO: {icao}) lisätty.")

    elif valinta == "2":
        icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper()
        if icao in lentokentat:
            print(f"Lentoasema: {lentokentat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")

    elif valinta == "3":
        print("Ohjelma lopetettu.")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")
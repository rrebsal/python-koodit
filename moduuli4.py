#1
i = 1
while i <= 1000:
    if i % 3 == 0:
        print(i)
    i += 1

#2
while True:
    tuumat = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä.")

#4
import random

vastaus = random.randint(1, 10)
print("Arvaa luku 1-10 ja katso saitko sen oikein.")

while True:
        arvaus = int(input("Anna arvauksesi: "))
        if arvaus < vastaus:
            print("Liian pieni arvaus.")
        elif arvaus > vastaus:
            print("Liian suuri arvaus.")
        else:
            print("Oikein. Numero oli", vastaus)
            break

#5
itunnus = "python"
isalasana = "rules"

yritykset = 0
maxyritykset = 5

while yritykset < maxyritykset:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == itunnus and salasana == isalasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

if yritykset == maxyritykset:
    print("Pääsy evätty.")
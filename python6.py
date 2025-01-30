import random
#1
def noppa():
    return random.randint(1,6)

while True:
    tulos = noppa()
    print(f"Nopan luku: {tulos}")
    if tulos== 6:
        break

#2
def noppaa(tahkot):
    return random.randint(1, tahkot)

tahkot = int(input("Anna nopan tahkojen lukumäärä: "))

while True:
    tulos = noppaa(tahkot)
    print(f"Nopan luku: {tulos}")
    if tulos == tahkot:
        break

#3
def gallona_to_litra(gallon):
    return gallon * 3.785

while True:
    gallon = float(input("Anna bensiinin määrä (galloina, negatiivinen luku lopettaa softan.): "))

    if gallon < 0:
        print("Loppu.")
        break

    litrat = gallona_to_litra(gallon)
    print(f"{gallon} gallonaa on {litrat:.3f} litraa")

#4
def summa(lista):
    return sum(lista)

numerot = [3, 7, 2, 9, 5]
tulos = summa(numerot)
print(f"Listan {numerot} summa on {tulos}")
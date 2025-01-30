#1
import random

def roll_dice(dice):
    for _ in range(dice):
        print(random.randint(1, 6))

dice = int(input("Kuinka monta noppaa haluat heittää?: "))
roll_dice(dice)

#2
numero = []

while True:
    numinp = input("Anna numero (tai paina Enter lopettaaksesi): ")
    if numinp == "":
        break
    try:
        numero.append(int(numinp))
    except ValueError:
        print("Anna kelvollinen numero.")

numero.sort(reverse=True)
top_viisi = numero[:5]

print("Viisi suurinta numeroa ovat:", top_viisi)

#3
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True

num = int(input("Anna numero (Koodi kertoo onko numero alkuluku vai ei): "))

if prime(num):
    print(f"{num} on alkuluku.")
else:
    print(f"{num} ei ole alkuluku.")

#4
kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)

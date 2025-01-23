#1
kayttaja = input('Anna nimesi: ')
print("Terve, " + kayttaja + "!")
#2
sade = float(input('Anna ympyrän säde: '))
print("Ympyrän pinta-ala on: ", sade ** 2 * 3.14)
#3
kanta = float(input('Anna suorakulmion kanta: '))
korkeus = float(input('Anna suorakulmion korkeus: '))
print("Suorakulmion piiri on: ", kanta * 2 + korkeus * 2)
print("Suorakulmion pinta-ala on: ", kanta * korkeus)
#4
numero1 = float(input('Anna numero: '))
numero2 = float(input('Anna toinen numero: '))
numero3 = float(input('Anna kolmas numero: '))
print("Lukujen summa: ", numero1 + numero2 + numero3)
print(f"Lukujen kesiarvo: {(numero1 + numero2 + numero3) / 3:.2f}")
print("Lukujen tulo: ", numero1 * numero2 * numero3)
#5
leivi = float(input('Anna leiviskät: '))
naula = float(input('Anna naula: '))
luoti = float(input('Anna luoti: '))

leiviw = 20
naulaw = 32
luotiw =13.3

kokonaisgrammat = (leivi * naulaw * luotiw * leiviw) + (naula * naulaw * luotiw) + (luoti * luotiw)

kilogrammat = kokonaisgrammat // 1000
grammat = kokonaisgrammat % 1000

print(f"Massa nykymittojen mukaan: {int(kilogrammat)} kilogrammaa ja {grammat:.2f} grammaa.")
#6
import random

kolme = ""
for _ in range(3):
    kolme += str(random.randint(0, 9))

nelja = ""
for _ in range(4):
    nelja += str(random.randint(1, 6))

print("Kolmenumeroinen koodi:", kolme)
print("Nelinumeroinen koodi:", nelja)






#1
kuhapituus = float(input("Anna kuhan pituus senttimetreinä: "))
if kuhapituus>=37:
    print("Voit pitää kuhan.")
else:
    print("Heitä kuha takaisin järveen. Kuhan pitäisi olla vielä ", 37 - kuhapituus, " senttiä pitkä.")

#2
hytti = input("Anna hyttiluokkasi (LUX, A, B, C):" ).upper()
if hytti=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hytti=="A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hytti=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hytti=="C":
    print("C on ikkunaton hytti autokannen yläpuolella.")
else:
    print("Virheellinen hyttiluokka")

#3
sukupuoli = input("Anna sukupuolesi (M/F): ").upper()
hemoglobiini = int(input("Anna hemoglobiiniarvosi (g/l): "))
if sukupuoli == "F":
        if hemoglobiini < 117:
            print("Hemoglobiiniarvosi on alhainen.")
        elif 117 <= hemoglobiini <= 175:
            print("Hemoglobiiniarvosi on normaali.")
        else:
            print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "M":
        if hemoglobiini < 134:
            print("Hemoglobiiniarvosi on alhainen.")
        elif 134 <= hemoglobiini <= 195:
            print("Hemoglobiiniarvosi on normaali.")
        else:
            print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli. Anna 'M' tai 'F'.")

#4
vuosi = int(input("Anna vuosiluku: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")

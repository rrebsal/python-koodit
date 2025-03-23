class Auto:
    def __init__(self, register, peakspeed, currentspeed, travelled):
        self.register = register
        self.peakspeed = int(peakspeed)
        self.currentspeed = int(currentspeed)
        self.travelled = int(travelled)

    def kiihdyta(self, muutos):
        self.currentspeed += muutos

        if self.currentspeed > self.peakspeed:
            self.currentspeed = self.peakspeed

        if self.currentspeed < 0:
            self.currentspeed = 0

        print(f"Auton nopeus: {self.currentspeed} km/h")

    def kulje(self, tunti):
        matka = self.currentspeed * tunti
        self.travelled += matka
        print(f"Auto on kulkenut: {matka} km, yhteensä {self.travelled} km.")

auto = Auto("ABC-123", 142, 0, 2000)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

auto.kiihdyta(-200)
auto.kulje(1.5)
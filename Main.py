class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda")

class Avtomobil(Transport):
    def harakatlanish(self):
        print("Avtomobil 80 km/soat tezlikda harakatlanmoqda")

class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped 20 km/soat tezlikda harakatlanmoqda")

class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd 120 km/soat tezlikda harakatlanmoqda")

transportlar = [
    Avtomobil(),
    Velosiped(),
    Poyezd()
]

for t in transportlar:
    t.harakatlanish()

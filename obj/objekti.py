class Cilveks:
    def __init__(self, vards, vecums, dzimums):
        self.age = vecums
        self.name = vards
        self.sex = dzimums
        self.nauda = 0

    def dzimsanas_diena(self):
        self.age += 1
    
    def mainit_vardu(self, jaunais_vards):
        self.name = jaunais_vards
    
    def pastastit_par_sevi(self):
        if self.sex == "s":
            dz = "sieviete"
        elif self.sex == "v":
            dz = "vīrietis"
        else:
            dz = self.sex
        print("Mani sauc {}, man ir {} gadi, es esmu {}, man kabatā ir {}$".format(self.name, self.age, dz, self.nauda))

    def nopelnit(self, nauda):
        self.nauda += nauda

    def uztaisit_spamu(self, failu_mape):
        faila_nosaukums = failu_mape + "spams" + self.name + str(self.age)
        sveiki_galotne = "a" if self.sex == "s" else "is"
        laimests_galotne = "usi" if self.sex == "s" else "is"
        if self.sex == "s":
            faila_teksts = "Sveika, {}! Tu esi laimējusi {}€!".format(self.name, self.age * 50)
        elif self.sex == "v":
            faila_teksts = "Sveiks, {}! Tu esi laimējis {}€!".format(self.name, self.age * 50)
        else:
            faila_teksts = "Sveiks/Sveika, {}! Tu esi laimējis/laimējusi {}€!".format(self.name, self.age * 50)
        with open(faila_nosaukums, "w", encoding="utf-8") as fails:
            fails.write(faila_teksts)
        self.nopelnit(self.age * 50)
        self.pastastit_par_sevi()

turpinat = "x"
cilveki = []
while turpinat == "x":
    vards = input("Ievadiet cilvēka vārdu!: ")
    vecums = int(input("Ievadiet vecumu!: "))
    dzimums = input("Ievadiet dzimumu (s/v)!:")
    cilveki.append(Cilveks(vards, vecums, dzimums))
    turpinat = input("Ja vēlies pievienot vēl vienu cilvēku, nospied 'x' !")

for viens in cilveki:
    viens.pastastit_par_sevi()

for persona in cilveki:
    persona.uztaisit_spamu("obj/spams/")
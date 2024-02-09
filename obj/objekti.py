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
        sveiki_galotne = "a"
        laimests_galotne = "usi"
        faila_teksts = "Sveik{}(-a/-s/-i), {}! Tu esi laimēj{}(-usi/-is/-is) {}€!".format(sveiki_galotne, self.name, laimests_galotne, self.age*35)
        with open(faila_nosaukums, "w", encoding="utf-8") as fails:
            fails.write(faila_teksts)
        self.nopelnit(30)
        self.pastastit_par_sevi()
        



persona1 = Cilveks("Marta", 32, "cilveks")
persona1.pastastit_par_sevi()
persona1.dzimsanas_diena()
persona1.pastastit_par_sevi()
persona1.nopelnit(30)
persona1.pastastit_par_sevi()
persona1.uztaisit_spamu("obj/spams/")

# turpinat = "t"
# cilveki = []
# while turpinat == "t":
#     vards = input("Ievadiet cilvēka vārdu!: ")
#     vecums = int(input("Ievadiet vecumu!: "))
#     dzimums = input("Ievadiet dzimumu (s/v)!:")
#     cilveki.append( Cilveks(vards, vecums, dzimums) )
#     turpinat = input("Ja vēlies pievienot vēl vienu cilvēku, nospied 't' !")

# for viens in cilveki:
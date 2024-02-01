def ierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "w", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def pierakstit(teksts, faila_nosaukums):
    fails = open(faila_nosaukums, "a", encoding='utf-8')
    fails.write(teksts)
    fails.close()

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
        rindas = fails.readlines()
    return rindas

def izveidot_vestuli(vards, vecums, dzimums, fails):
    sveika_vai_sveiks = "Sveika, " if dzimums == "s" else "Sveiks, "
    galotne = "a" if dzimums == "s" else "š"
    naudas_summa = vecums * 10
    teksts = f"{sveika_vai_sveiks}{vards}! Jūs esat laimējusi {naudas_summa} dolārus!\n"
    ierakstit(teksts, fails)

vardi = ["Anna", "Maija", "Jānis", "Kaspars"]
uzvardi = ["Bērziņa", "Paija", "Ozols", "Kasprets"]
vecumi = [23, 150, 89, 11]
dzimumi = ["s", "s", "v", "v"]

ierakstit("", "faili/cilveki.txt")

for i in range(len(vardi)):
    if dzimumi[i] == "s":
        rakstamais = "sieviete"
    else:
        rakstamais = "vīrietis"
    teksts = f"{vardi[i]} {uzvardi[i]} - {vecumi[i]}, {rakstamais}\n"
    pierakstit(teksts, "faili/cilveki.txt")

visi = nolasit("faili/cilveki.txt")

for idx, cilveks in enumerate(visi):
    info = cilveks.split(" ")
    vards = info[0]
    vecums = int(info[2])
    dzimums = info[4].strip()

    fails = f"faili/vestule{idx + 1}.txt"
    izveidot_vestuli(vards, vecums, dzimums, fails)
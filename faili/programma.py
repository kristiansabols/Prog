def ierakstit(teksts, faila_nosaukums):
    with open(faila_nosaukums, "w", encoding='utf-8') as fails:
        fails.write(teksts)

def pierakstit(teksts, faila_nosaukums):
    with open(faila_nosaukums, "a", encoding='utf-8') as fails:
        fails.write(teksts)

def nolasit(faila_nosaukums):
    with open(faila_nosaukums, "r", encoding="utf-8") as fails:
        rindas = fails.readlines()
    return rindas

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
    teksts = "{} {} - {}, {}\n".format(vardi[i], uzvardi[i], vecumi[i], rakstamais)
    pierakstit(teksts, "faili/cilveki.txt")

visi = nolasit("faili/cilveki.txt")
vecumi = []
for cilveks in visi:
    info = cilveks.split(" ")
    vecums = int(info[3].rstrip(","))
    vecumi.append(vecums)

print(vecumi)

# Marta - vards.txt
vards1 = ["Marta"]
uzvards1 = ["Britāla"]
vecums2 = [32]
dzimums1 = ["s"]

teksts = ""
for i in range(len(vards1)):
    if dzimums1[i] == "s":
        rakstamais = "sieviete"
    teksts += "{} {} - {}, {}\n".format(vards1[i], uzvards1[i], vecums2[i], rakstamais)

ierakstit(teksts, "faili/vards.txt")

with open("faili/vards.txt", 'r', encoding='utf-8') as f:
    visi = f.read()
print(visi)

# Jūs esat laimējusi  - cilveks0.txt
for i in range(len(vards1)):
    if dzimums1[i] == "s":
        rakstamais = "sieviete"
    teksts = "Sveiki, {} {}! Jūs esat laimējusi {} dolārus!\n".format(vards1[i], uzvards1[i], vecums2[i] * 100)
    ierakstit(teksts, "faili/cilveks0.txt")

with open("faili/cilveks0.txt", 'r', encoding='utf-8') as f:
    visi = f.read()
print(visi)

# teksts.txt
ierakstit("Sveiki, visi!", "faili/teksts.txt")
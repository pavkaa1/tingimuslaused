arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))
arv3 = int(input("Kolmas arv: "))

# Kontrollin, kas esimene arv on suurim
if arv1 >= arv2 and arv1 >= arv3:
    suurim = arv1

# Kontrollin, kas teine arv on suurim
elif arv2 >= arv1 and arv2 >= arv3:
    suurim = arv2

# Kui kumbki eelnev tingimus ei kehti on suurim kolmas arv
else:
    suurim = arv3

# Väljastame suurima arvu
print("Suurim arv on", suurim, ".")
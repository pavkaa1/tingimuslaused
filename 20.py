# Küsin kasutajalt kolme külje pikkused
kylg1 = int(input("Esimene külg: "))
kylg2 = int(input("Teine külg: "))
kylg3 = int(input("Kolmas külg: "))

# Kontrollin kas kahe külje summa on suurem kui kolmas külg
if kylg1 + kylg2 > kylg3 and kylg1 + kylg3 > kylg2 and kylg2 + kylg3 > kylg1:
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")
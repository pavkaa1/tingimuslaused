temperatuur = int(input("Sisesta temperatuur: "))

# Kontrollime, kas temperatuur on 18–24 kraadi.
if temperatuur >= 18 and temperatuur <= 24:
    print("Temperatuur on normaalne.")
else:
    print("Hoiatus!")
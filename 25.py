arv1 = float(input("Esimene arv: "))
tehe = input("Tehe: ")
arv2 = float(input("Teine arv: "))

if tehe == "+":
    tulemus = arv1 + arv2
    print("Tulemus:", tulemus)

elif tehe == "-":
    tulemus = arv1 - arv2
    print("Tulemus:", tulemus)

elif tehe == "*":
    tulemus = arv1 * arv2
    print("Tulemus:", tulemus)

elif tehe == "/":
    if arv2 != 0:
        tulemus = arv1 / arv2
        print("Tulemus:", tulemus)
    else:
        print("Nulliga jagada ei saa.")

else:
    print("Tundmatu tehe.")
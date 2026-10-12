nimi = "Pavel"
punktisumma = 89
puudumised = 1
tood_esitatud = "jah"

if punktisumma >= 90:
    hinne = 5
elif punktisumma >= 75:
    hinne = 4
elif punktisumma >= 50:
    hinne = 3
elif punktisumma >= 20:
    hinne = 2
else:
    hinne = 1

print("Õpilane:", nimi)
print("Hinne:", hinne)

if puudumised > 10:
    print("Hoiatus: liiga palju puudumisi.")
else:
    print("Puudumiste arv on lubatud.")

if tood_esitatud == "jah":
    print("Kõik tööd on esitatud.")
else:
    print("Kõik tööd ei ole esitatud.")

if hinne >= 3 and puudumised <= 10 and tood_esitatud == "jah":
    print("Aine on läbitud.")
else:
    print("Aine ei ole läbitud.")

if hinne == 1 or hinne == 2:
    print("Hinne on alla kolme.")

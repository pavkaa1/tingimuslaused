cpu = int(input("CPU kasutus (%): "))
memory = int(input("Mälu kasutus (%): "))
disk = int(input("Ketta kasutus (%): "))

if cpu > 90 or memory > 90 or disk > 90:
    status = "KRIITILINE"
elif cpu > 75 or memory > 75 or disk > 75:
    status = "HOIATUS"
else:
    status = "OK"

print("Serveri olek:", status)
# Küsin kasutajalt aasta
aasta = int(input("Sisesta aasta: "))

# Kontrollin, kas aasta jagub 400-ga
if aasta % 400 == 0:
    print("Liigaasta.")

# Kontrollin, kas aasta jagub 100-ga
elif aasta % 100 == 0:
    print("Ei ole liigaasta.")

# Kontrollin, kas aasta jagub 4-ga
elif aasta % 4 == 0:
    print("Liigaasta.")

# Kui ükski tingimus ei kehti
else:
    print("Ei ole liigaasta.")
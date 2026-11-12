# Küsin kasutajanime
kasutajanimi = input("Sisesta kasutajanimi: ")

# Kontrollin, kas kasutajanimi on õige
if kasutajanimi == "admin":

    # Kui kasutajanimi on õige, küsime parooli
    parool = input("Sisesta parool: ")

    # Kontrollin, kas parool on õige
    if parool == "python123":
        print("Tere tulemast!")
    else:
        print("Vale parool.")

# Kui kasutajanimi on vale
else:
    print("Tundmatu kasutaja.")
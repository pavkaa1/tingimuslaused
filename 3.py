age = 20
has_ticket = True

# and – JA: mõlemad tingimused peavad olema tõesed
print(age >= 18 and has_ticket)  # True

# or – VÕI: vähemalt üks tingimus peab olema tõene
print(age < 18 or has_ticket)  # True

# not – EI: muudab True väärtuse False-iks ja vastupidi
print(age >= 18 and not has_ticket)  # False

# not muudab tingimuse vastupidiseks
print(not (age < 18))  # True
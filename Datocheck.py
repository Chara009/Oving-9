def datocheck(liste, dato):
    f = liste.readline()
    gruppe = {}
    i = 0
    while f != "":
        f = f.rstrip("\n")
        f = f.split(";")
        datonow = f[2]
        if dato == datonow:
            gruppe[i] = Avtale(f[0], f[1], f[2], f[3])
            i += 1
        f = liste.readline()
    return gruppe
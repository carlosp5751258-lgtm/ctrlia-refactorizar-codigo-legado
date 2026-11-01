# facturas.py: escrito en 2014, nadie lo toca
def total(lineas, cliente):
    t = 0
    for l in lineas:
        if l[2] == None:
            l[2] = 1
        t = t + l[1] * l[2]
    if cliente == "VIP":
        t = t - t * 10 / 100
    if t > 1000:
        t = t - 50
    return round(t, 2)

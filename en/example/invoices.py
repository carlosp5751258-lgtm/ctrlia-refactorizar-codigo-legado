# invoices.py: written in 2014, nobody touches it
def total(lines, customer):
    t = 0
    for l in lines:
        if l[2] == None:
            l[2] = 1
        t = t + l[1] * l[2]
    if customer == "VIP":
        t = t - t * 10 / 100
    if t > 1000:
        t = t - 50
    return round(t, 2)

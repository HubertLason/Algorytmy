n = int(input("Podaj n:"))

if n > 0:
    ile_u = 0
    i = 0

    while i < n:
        ai = int(input("Podaj ai:"))
        if ai < 0:
            ile_u += 1
        i = i + 1
    print(ile_u)
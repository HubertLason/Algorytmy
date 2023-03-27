def Hanoi(n, pierwszy, docelowy, roboczy):
    if (n==1):
        print( pierwszy, "->", docelowy)
        return
    Hanoi(n-1, pierwszy, roboczy, docelowy)
    print(pierwszy, "->", docelowy)
    Hanoi(n-1, roboczy, docelowy, pierwszy)

Hanoi(3, 'A', 'B', 'C')

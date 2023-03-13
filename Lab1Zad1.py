import math

a = float(input("Podaj a:"))
b = float(input("Podaj b:"))
c = float(input("Podaj c:"))

if a != 0:
    delta = (b * b) - (4 * a * c)
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(x1)
        print(x2)
    elif delta == 0:
        x1 = -b / (2 * a)
        print(x1)
    else:
        print("Brak rozwiazan rzeczywistych")
else:
    print("To nie jest rownanie kwadratowe")

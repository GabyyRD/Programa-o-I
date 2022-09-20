def tripla():
    a = int(input())
    b = int(input())
    c = int(input())
    if a**2 == b**2 + c**2:
        print("Tripla pitagorica")
    if b**2 == a**2 + c**2:
        print("Tripla pitagorica")
    if c**2 == a**2 + b**2:
        print("Tripla pitagorica")

tripla()
print("********Calculate factorial*******")

while True:
    sayi = input("Number: (q for exit)")
    fact=1

    if(sayi=="q"):
        print("Exit...")
        break
    else:
        sayi=int(sayi)
        for i in range(2,sayi+1):
            fact=fact*i

        print("Fact: ",fact)







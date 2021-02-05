
a = int(input("Birinci Sayı: "))
b = int(input("İkinci Sayı: "))
c = int(input("Üçüncü Sayı: "))


if(a>b and a>c):
    print("Max sayı: {}".format(a))
elif(b>a and b>c):
    print("Max sayı: {}".format(b))
elif(c>b and c>a):
    print("Max sayı: {}".format(c))
else:
    print("Again")
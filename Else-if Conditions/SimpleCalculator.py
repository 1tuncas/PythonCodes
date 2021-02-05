print(""" ***********
Hesap Makinesi 
İşlemler
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme   """)

a = int(input("First number: "))
b = int(input("Second number: "))

operation = input("Yapmak istediğin işlem?")

if operation == "1":
    print("Sonuç: {}".format(a+b))
elif operation == "2":
    print("Sonuç: {}".format(a - b))
elif operation == "3":
    print("Sonuç: {}".format(a * b))
elif operation=="4":
    print("Sonuç: {}".format(a / b))
else:
    print("Again")


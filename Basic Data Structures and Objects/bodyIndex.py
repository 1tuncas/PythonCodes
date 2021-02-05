
weight = int(input("Kilo(kg): "))
height = int(input("Boy(cm): "))

height = height/100
index = weight/(height**2)
print("Body Index: {}".format(index))
a = int(input("Katsayı 1: "))
b = int(input("Katsayı 2: "))
c = int(input("Katsayı 3: "))



delta = b**2 - 4*a*c

root1 = (-b-delta**0.5)/(2*a)
root2 = (-b + delta ** 0.5) / (2 * a)

roots = [root1,root2]

print("Kök 1: {}\n"
      "Kök 2: {}".format(roots[0],roots[1]))
print("Oyuncu kaydetme programı")

ad = input("Player name: ")
soy= input("Player surname: ")
takim = input("Player team: ")

bilgiler = [ad,soy,takim]

print("Oyuncu adı: {}\n"
      "Oyuncu soyadı: {}\n"
      "Oyuncu takımı:{}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler kaydedildi")

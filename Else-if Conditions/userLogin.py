print("Kullanıcı Girişi"
      "*********")

userName = "Kobra"
pWord = "Murat"

userNameLog = input("UserName: ")
pWordLog = input("Password: ")

if userName==userNameLog and pWord==pWordLog:
    print("Başarılı")
elif userName!=userNameLog or pWord!=pWordLog:
    print("Kullanıcı adı veya parola yanlış")
else:
    print("Again")


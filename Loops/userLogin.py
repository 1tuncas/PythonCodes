print("**************** User Log in ***************")

sys_userName= "kobra"
sys_pWord = "123456"
girisHakki = 3

while True:
    userName = input("Kullanıcı Adı: ")
    pWord = input("Şifre: ")

    if (sys_userName != userName or sys_pWord != pWord):
        print("Kullanıcı adı veya parola yanlış")
        girisHakki-=1
    elif(sys_userName==userName and sys_pWord==pWord):
        print("Giriş Başarılı")
        break
    else:
        print("Geçersiz giriş")
    if(girisHakki == 0):
        print("iriş hakkı bitti")
        break




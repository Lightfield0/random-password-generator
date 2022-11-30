import random
import string

def rastgele_sifre_uret(uzunluk):
    sayac=0
    while sayac<uzunluk:

        harfler =  string.ascii_letters + string.digits
        sonuc = ''.join(random.choice(harfler) for i in range(uzunluk))
        sayac+=1
        f= open("kayit.txt", "a")
        print(sonuc,file=f)
rastgele_sifre_uret(20)
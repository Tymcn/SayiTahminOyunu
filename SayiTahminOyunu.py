import random
import time

tutulanSayi=random.randint(1,100)
hak=5
puan=100

print(f"""
1 İLE 100 ARASINDA TUTULAN BİR SAYI VAR BAKALIM KAÇ TAHMİNDE BULACAKSIN ???? \n
TOPLAM {hak} HAKKIN VARDIR. \n
TOPLAM {puan}  PUNANIN VARDIR. \n 
HER YANLIŞ CEVAP İÇİN 1 HAK VE 20 PUANIN AZALIR.

""")

while True:
    try:
        tahminEdilenSayi=int(input("TAHMİNİNİZİ GİRİNİZ: "))

        if tahminEdilenSayi<tutulanSayi:
            print("*** KONTROL EDİLİYOR ***")
            time.sleep(1)
            hak=hak-1
            puan=puan-20

            print(f"TUTULAN SAYI TAHMİNİNDEN DAHA BÜYÜKTÜR MAALESEF.1 HAKKIN VE 20 PUANIN GİTTİ KALAN HAK: {hak} KALAN PUAN: {puan}")
            if hak == 0:
                print(f"*** *** MAALESEF HAKKIN KALMADI  -- OYUN BİTTİ :(  !!! -- TUTULAN SAYI {tutulanSayi} ***")
                time.sleep(1)
                break


        elif tahminEdilenSayi>tutulanSayi:
            print("*** KONTROL EDİLİYOR ***")
            time.sleep(1)
            hak = hak - 1
            puan = puan - 20
            print(f"TUTULAN SAYI TAHMİNİNDEN DAHA KÜÇÜKTÜR MAALESEF.1 HAKKIN VE 20 PUANIN GİTTİ KALAN HAK: {hak} KALAN PUAN: {puan}")

            if hak==0:
                print(f"*** MAALESEF HAKKIN KALMADI  -- OYUN BİTTİ :(  !!! -- TUTULAN SAYI {tutulanSayi} ***")
                time.sleep(1)
                break



        elif tahminEdilenSayi==tutulanSayi:
            print("*** KONTROL EDİLİYOR ***")
            time.sleep(1)
            print(f"TEBRİKLER YİĞİDİM NASIL BULDUN ÖYLE MAŞAALLAH {hak} HAKKIN KALDI. PUAN: {puan} kaldı")


    except:
        print("LÜTFEN 1 İLE 100 ARASINDA SAYI GİR RAKAM GİR BOŞ BIRAKMA YAZI YAZMA !!!")


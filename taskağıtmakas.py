import random

def main():

  secimler = ["Taş", "Kağıt", "Makas"]


  puanlar = {
    "Taş": {"Kağıt": -1, "Makas": 1},
    "Kağıt": {"Taş": 1, "Makas": -1},
    "Makas": {"Taş": -1, "Kağıt": 1}
  }


  def menu():
    print("-" * 20)
    print("Taş Kağıt Makas Oyunu")
    print("-" * 20)
    print("1. Oyunu Oyna")
    print("2. Kuralları Göster")
    print("3. Çıkış")
    print("-" * 20)
    while True:
      try:
        secim = int(input("Seçiminizi girin: "))
        if 1 <= secim <= 3:
          return secim
        else:
          print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")
      except ValueError:
        print("Lütfen bir sayı giriniz.")

  # Oyun kuralları
  def kurallar():
    print("-" * 20)
    print("Oyun Kuralları")
    print("-" * 20)
    print("Taş, makası kırarak yener.")
    print("Kağıt, taşı sararak yener.")
    print("Makas, kağıdı keserek yener.")
    print("-" * 20)

  # Oyun fonksiyonu
  def oyun():

    oyuncu_skoru = 0
    bilgisayar_skoru = 0


    tur_sayisi = 0

    while tur_sayisi < 3:
      # Kullanıcıdan seçim alma
      while True:
        try:
          kullanici_secimi = int(input("Seçiminizi girin (0-Taş, 1-Kağıt, 2-Makas): "))
          if 0 <= kullanici_secimi <= 2:
            break
          else:
            print("Geçersiz seçim. Lütfen 0, 1 veya 2 giriniz.")
        except ValueError:
          print("Lütfen bir sayı giriniz.")

   
      bilgisayar_secimi = random.randint(0, 2)

      
      kazanan = puanlar[secimler[kullanici_secimi]][secimler[bilgisayar_secimi]]
      if kazanan == 1:
        print("Kazandınız!")
        oyuncu_skoru += 1
      elif kazanan == -1:
        print("Bilgisayar kazandı!")
        bilgisayar_skoru += 1
      else:
        print("Beraberlik!")

    
      tur_sayisi += 1


    if oyuncu_skoru > bilgisayar_skoru:
      print("Tebrikler! Oyunu kazandınız.")
    elif bilgisayar_skoru > oyuncu_skoru:
      print("Maalesef oyunu kaybettiniz.")
    else:
      print("Oyun berabere bitti.")
#by kamil umut araz   instagram: k.umutarazz
 
    print("-" * 20)
    print("Oyuncu skoru:", oyuncu_skoru)
    print("Bilgisayar skoru:", bilgisayar_skoru)
    print("-" * 20)


  while True:
    secim = menu()
    if secim == 1:
      oyun()
    elif secim == 2:
      kurallar()
    elif secim == 3:
      break

if __name__ == "__main__":
  main()

def not_ekle():
    with open("Notlarım.txt", "a") as f:
        notum = input("Yeni notunuz nedir?\t")
        f.write(notum + "\n")
        print("Notun kaydedildi.")

def notları_goster():
    try:
        with open("Notlarım.txt", "r") as f:
            print("\n--- NOTLAR ---")
            print(f.read())
    except FileNotFoundError:
        print("Henüz hiç notun yok.")

def notu_sil():
    with open("Notlarım.txt", "w") as f:
        f.truncate()
    print("Tüm notlar silindi.")


#Menü
while True:
    secim = input("\nNe yapmak istiyorsun? (y: yeni not, g: göster, s: sil, q: çık): ")
    if secim == "y":
        not_ekle()
    elif secim == "g":
        notları_goster()
    elif secim == "s":
        notu_sil()
    elif secim == "q":
        print("Notlardan çıkılıyor")
        break
    else:
        print("Geçerli bir seçim yapmadınız. \n(y: yeni not, g: göster, s: sil, q: çık)")
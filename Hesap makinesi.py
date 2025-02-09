while True:
    ilksayi = input("İlk sayıyı giriniz (Çıkmak için 'q' giriniz):\n")
    if ilksayi.lower() == 'q':
        print("Çıkış yapılıyor...")
        break

    try:
        ilksayi = float(ilksayi)
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue

    islem = input("Lütfen işlemi yazınız (+, -, *, /):\n")

    ikincisayi = input("İkinci sayıyı giriniz:\n")
    try:
        ikincisayi = float(ikincisayi)
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        continue

    if islem == "+":
        sonuc = ilksayi + ikincisayi
    elif islem == "-":
        sonuc = ilksayi - ikincisayi
    elif islem == "*":
        sonuc = ilksayi * ikincisayi
    elif islem == "/":
        if ikincisayi == 0:
            print("Tanımsız! Lütfen bölme işleminde ikincisayi'ya 0 yazmayınız!")
            continue
        sonuc = ilksayi / ikincisayi
    else:
        print("Geçersiz işlem! Lütfen +, -, *, / kullanın.")
        continue

    print("-" * 30)
    print("Sonuç:", sonuc)
    print("-" * 30)


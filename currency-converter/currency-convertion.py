import requests
from pprint import pprint  # Ma'lumotlarni chiroyli formatda chiqarish uchun
from config import URL  # URL manzilini config.py faylidan olish

  # NBU dan Json formatdagi malumotlar olindi 
r = requests.get(URL)
kurslar = r.json()

    # Valyuta kursini topuvchi funksiya yaratildi
def valuta(kod):
    for valyuta in kurslar: 
        if valyuta["code"] == kod:
            return float(valyuta['cb_price'])      # Valyuta kursini qaytaradi
    return None                                     # Agar topilmasa, None qaytaradi

# Foydalanuvchidan ma'lumot kiritishni so'rash
summa = float(input("Miqdorni kiriting: "))
at_valuta = input("Qaysi valyutadan convert qilmoqchisiz : ").upper()
to_valuta = input("Qaysi valyutaga convert qilmoqchisiz : ").upper()

# Funksiya call qilindi hamda valyuta kuslari olindi 
kursni = valuta(at_valuta)
kursga = valuta(to_valuta)

# Hisoblash 
if kursni and kursga:                            # Agar valuyuta kurslari True qiymat qaytarsa 
    natija = (summa / kursni) * kursga            # Uni kursini hisoblayamiz 
    print(f"{summa} {at_valuta} = {natija:.2f} {to_valuta}")    # Natija chiqarildi 
else:
    print("Kiritilgan valyuta kodi noto'g'ri!")   
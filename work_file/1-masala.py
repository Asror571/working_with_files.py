with  open("friends_num.txt",'w') as friend_num:    # file ochildi yozish maqsadida 

    while True:
        name = input("Ismni kiriitng :")          # Kantakni sismini so'raydi agar '-' kiritsa dastur o'chadi
        if name == '-':
            break   
        phone = input("Telefon raqamni kiriting bu ko'rinishda(+998 88 958 11 08) :")   # Telefon raqam olindi 
        friend_num.write(f"{ name }   { phone }\n")        # Write yordaminda fayl yozildi 
    print("Siz kiritgan kantaklar saqlandi")              

with open("friends_num.txt",'r') as friend_num:       # o'qish maqsadida ochildi 
    kantaklar = friend_num.read()       # Barchasi o'qildi 

for kantak in kantaklar:             # Va chiqariladi 
    print(kantak)
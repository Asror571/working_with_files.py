from colorama import Fore,Style,Back
with open('shopping_list.txt','w') as shopping :      # yozish maqsadida file ochildi 
    while True:                
        print(Fore.YELLOW+"Assalomu alaykum tugatish uchun ' - ' ni kiriting ")       # Foydalanuvchi - ni kiritganda dastur o'chishi aytildi 
        product = input(Fore.MAGENTA+"Maxsulotlrni kiriting :")
        if product == '-':                             # Agar foydalanuvchi - son kiriitadigan bo'lsa dastur o'chadi
            break
        shopping.write(f" {   product   }\n ")             # Maxsulot file ga yozildi 
with open('shopping_list.txt','r') as shopping:
    maxsulotlar = shopping.read()                     # FIle ochildi va o'qildi 
    print(maxsulotlar)
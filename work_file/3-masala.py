with open("grades.txt", "w") as grades:     # O'qish uchun fayl ochildi
    while True:
        print("Assalomu alaykum, agar siz '-' kiritadigan bo'lsangiz, dastur o'chadi.")     # - kiritsa dastur o'chadi 
        student = input("Talabani ismini kiriting: ")
        if student == '-':   
            break
        grade = float(input(f"{student} ning bahosini kiriting: "))   # Talabaning bahosi  olinadi
        grades.write(f"{student} {grade}\n")     # Baho va Talabalarning ismi yozliladi


with open("grades.txt", "r") as grades_file:     # O'qish maqsadida  file ochildi 
    student_grade = grades_file.readlines()            
    grades = []                                    # Baholarni saqlash uchun
    for line in student_grade:                      #Loop yordamida baholarni saqalaymiz                  
        student, grade = line.strip().split(" ")  
        grades.append(float(grade))  

    if grades:
        middle = sum(grades) / len(grades)     # Hisoblash 

        print("\nBaholar ro'yxati:")    
        for line in student_grade:              # Natijani chiqarish
            print(line.strip())  
        print(f"O'rtacha baho: {middle:.2f}")
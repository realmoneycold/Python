# 1 exam question'
# number = input("Raqam kiriting: ")
# in_not_order = number[::-1] 
# print(in_not_order)

#2
#Matndagi belgilar farqili bo'lsa Yes deb chiqsin, Agar bir xillik bo'lsa NO
# matn = input("Matn kiriting: ")
# if len(set(matn)) < len(matn):
#     print("No")  
# else:
#     print("Yes")

# 3
# tub sonlarni chiqaring
# a = int(input("A raqamni kiriting: "))
# b = int(input("B raqamni kiriting: "))
# for i in range(a,b+1):
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 !=0:
#          print(i)

# 4
# numbers = [2, 5, 8,11]
# ayiruvchi_son = numbers[1] - numbers[0]
# is_arithmetic = True
# for i in range(1, len(numbers) - 1):
#     if numbers[i + 1] - numbers[i] != ayiruvchi_son or numbers[i] <= numbers[i - 1]:
#         is_arithmetic = False
#         break
# if is_arithmetic:
#     print("Yes")  
# else:
#     print("No")  
        

# 5
# qator = 5  
# for i in range(qator):
#     print(' ' * (qator - i - 1), end='')  
#     print('*' * (2 * i + 1)) 

# 2-qism
# Todo 

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname='todo',  
        user='postgres',  
        password='20071214',  
        host='localhost',
        port='5432'
    )

def add_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO TODO(username, password) VALUES(%s, %s)""", (username, password))
    conn.commit()
    cur.close()
    conn.close()

def user_exists(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TODO WHERE username = %s", (username,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user is not None

def validate_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM TODO WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user is not None

def add_task(username, task):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO Tasks (username, task) VALUES (%s, %s)""", (username, task))
    conn.commit()
    cur.close()
    conn.close()

def get_tasks(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT task FROM Tasks WHERE username = %s", (username,))
    tasks = cur.fetchall()  
    cur.close()
    conn.close()
    return [task[0] for task in tasks]  

def delete_task(username, task):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM Tasks WHERE username = %s AND task = %s""", (username, task))
    conn.commit()
    cur.close()
    conn.close()

def Asosiy_menu():
    while True:
        print("""
===ASOSIY MENYU===
          1. Ro'yxatdan o'tish
          2. Kirish
          3. Chiqish""")
        input_choice = input("Tanlang(1-3): ")
        if input_choice == "1":
            username_for_register = input("Username kiriting: ")
            if user_exists(username_for_register):
                print("Bu username allaqon mavjud!")
            else:
                parol_for_register = input("Parol kiriting: ")
                add_user(username_for_register, parol_for_register)
                print("Akkount muvaffaqiyatli yaratildi!")
        elif input_choice == "2":
            username = input("Usernameingizni kiriting: ")
            password = input("Parolingizni kiriting: ")
            if validate_user(username, password):
                print("Kirish muvaffaqiyatli!")
                TodoMenyusi(username)
            else:
                print("Hato username yoki parol!")  
        elif input_choice == "3":
            print("Akkountdan muvaffaqiyatli chiqildi!")
            break
        else:
            print("Bunday tanlov mavjud emas.")

def TodoMenyusi(username):
    while True:
        print("""
1. Ro'yxatni ko'rish
2. Yangi vazifa qo'shish
3. Vazifa o'chirish
4. Chiqish""")
        menyu_input = input("Tanlovingizni kiriting(1-4): ")
        if menyu_input == "1":
            tasks = get_tasks(username)
            if tasks:
                print("Sizning vazifalaringiz:")
                for task in tasks:
                    print(f"- {task}")
            else:
                print("Sizda hech qanday vazifa yo'q.")
        elif menyu_input == "2":
            new_todo = input("Yangi vazifani kiriting: ")
            add_task(username, new_todo)
            print("Yangi vazifa qo'shildi!")
        elif menyu_input == "3":
            delete_input = input("O'chirmoqchi bo'lgan vazifani kiriting: ")
            delete_task(username, delete_input)
            print("Vazifa muvaffaqiyatli o'chirildi!")
        elif menyu_input == "4":
            print("Dasturdan muvaffaqiyatli chiqdingiz!")
            break
        else:
            print("Bunday tanlov mavjud emas.")

Asosiy_menu()

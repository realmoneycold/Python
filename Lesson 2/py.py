import random
import psycopg2

users = {
    "Users": ""
}

def get_connection():
    x = psycopg2.connect(
        dbname='users',
        user='postgres',
        password='20071214',
        host='localhost',
        port='5432'
    )
    return x

def create_users_randomly():
    firstnames = ['Radmir', 'Umid', 'Dilshod', 'Sanjar', 'Qahramon', 'Sabrina', 'Malika', 'Sarvinoz', 'Umida', 'Otabek', 'Firsavs', 'Hasan', 'Nurahmed', 'Jamol', 'Sarvara']
    names = ['Erkinov', 'Ravshanov', 'Jahongirov', 'Xalimov', 'Mikhliev', 'Savrvarov', 'Abdullayev']
    addresses = ['Termiz shahar', 'Muzrabot tumani', 'Boysun', 'Sherobod', 'Xalqabod', 'Uzum', 'Denov', 'Chilonzor']
    
    user_amount = int(input("Nechta user qo'shishni xoxlaysiz?: "))
    
    for i in range(user_amount):
        ages = str(random.randint(7, 40))
        first_name = random.choice(firstnames)
        na_me = random.choice(names)
        addre_ss = random.choice(addresses)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO USERS(firstname, name, age, address) VALUES(%s, %s, %s, %s)""", (first_name, na_me, ages, addre_ss))
        conn.commit()
        conn.close()

    print(f"{user_amount} ta userlar muvafaqiyatli qo'shildi!")

    Asosiy_menu()

user_list = []

def add_laptops_manually(firstname, name, age, address):
    user = {
        'firstname': firstname,
        'name': name,
        'age': age,
        'address': address
    }
    user_list.append(user)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO USERS(firstname, name, age, address) VALUES(%s, %s, %s, %s)
    """, (firstname, name, age, address))
    conn.commit()  
    conn.close() 

def users_list():
    print("===USERLAR RO'XYATI===")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    for user in users:
        print(f"{user[0]} | {user[1]} | {user[2]} | {user[3]} | {user[4]} ")
    conn.close()
    Asosiy_menu()

def delete_user():
    choice = int(input("Nechta user o'chirmoqchisiz?: "))
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    user_amount = len(users)
    if choice <= user_amount:
        counter = 0
        for i in users:
            cur.execute("DELETE FROM users WHERE id=%s", (i[0],))
            conn.commit()
            counter += 1
            if choice == counter:
                break
        print(f"Bazadan {choice}-ta users muvafaqiyatli o'chirildi!")
    else:
        print(f"Bazadan {choice} ta userlar mavjud emas. Jami: {user_amount} ta user bor")
    conn.close()
    Asosiy_menu()

def Asosiy_menu():
    while True:
        print(""" === ASOSIY MENYU ===
1. Foydalanuvchi qo'shish
2. Random foydalanuvchi qo'shish
3. Foydalanuvchi ro'yxati
4. Foydalanuvchi o'chirish
5. Foydalanuvchi tahrirlash
6. Dasturni to'xtatish""")
        
        choice_input = input("Tanlov(1-6): ")
        if choice_input == "1":
            firstname = input("Ismingizni kiriting: ")
            name = input("Familiyangizni kiriting: ")
            age = input("Yoshingizni kiriting: ")
            address = input("Yashash manzilingizni kiriting: ")
            add_laptops_manually(firstname, name, age, address)
            print("Malumot muvafaqiyatli qo'shildi!")

        elif choice_input == "2":
            create_users_randomly()

        elif choice_input == "3":
            users_list()
        elif choice_input == "4":
            delete_user()
        elif choice_input == "5":
            print("Tahrirlash vaqtinchalik mavjud emas")
        elif choice_input == "6":
            print("Dastur to'xtatildi")
            exit()
        else:
            print("Bunday tanlov mavjud emas!")

Asosiy_menu()
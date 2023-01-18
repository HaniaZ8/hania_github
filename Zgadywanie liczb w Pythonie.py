def get_number_from_user():
    user_input = False
    try:
        user_input = int(input("Podaj numer: "))
        return user_input
    except: 
        print("Nie wprowadzono liczby")
        return None


def ask_user_equation():
    import random
    a = random.randint(1,15)
    c = random.randint(16,30)
    print(f"{a} + ... = {c}")
    b = get_number_from_user()
    num = c - a
    if b == num:
        return 1
    else:
        return 0
    
import time
start_time = time.time()
current_time = time.time()
time_limit = 30
score = 0
while (current_time - start_time) < time_limit:
    current_time = time.time()
    sc = ask_user_equation()
    score += sc
print("Wynik: ", score)
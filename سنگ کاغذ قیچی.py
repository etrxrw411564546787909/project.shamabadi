import random

def play_game():
    point_user = 0
    point_pc = 0

    while True:
        print("بازی سنگ کاغذ قیچی")
        inp = input("انتخاب خود را وارد کنید (سنگ، کاغذ، قیچی) یا 'خروج' برای پایان بازی: ").strip()

        # بررسی خروج
        if inp == "خروج":
            print("بازی به پایان رسید.")
            break

        # انتخاب سیستم به صورت رندوم
        a = random.randint(0, 2)
        if a == 0:
            a = "سنگ"
        elif a == 1:
            a = "کاغذ"
        else:
            a = "قیچی"

        # بررسی حالت مساوی
        if inp == a:
            print("مساوی! هیچ کس برنده نیست.")
        elif (inp == "سنگ" and a == "قیچی") or (inp == "قیچی" and a == "کاغذ") or (inp == "کاغذ" and a == "سنگ"):
            point_user += 1
            print("تو برنده شدی!")
        elif (inp == "قیچی" and a == "سنگ") or (inp == "کاغذ" and a == "قیچی") or (inp == "سنگ" and a == "کاغذ"):
            point_pc += 1
            print("کامپیوتر برنده شد...")

        # نمایش انتخاب کاربر و سیستم
        print(f"انتخاب شما: {inp}")
        print(f"انتخاب کامپیوتر: {a}")
        # چاپ کردن نمره سیستم و کاربر
        print(f"نمره شما: {point_user}")
        print(f"نمره کامپیوتر: {point_pc}\n")

# اجرای بازی
play_game()


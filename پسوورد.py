def check_password():
    # رمز عبور صحیح
    password = 12345
    max_talash = 3  # حداکثر تعداد تلاش‌ها
    tedad_talash = 0  # شمارش تعداد تلاش‌ها

    print("به سیستم ورود خوش آمدید!")

    while tedad_talash < max_talash:
        try:
            # دریافت ورودی رمز عبور از کاربر
            user_input = int(input("لطفاً رمز عبور را وارد کنید: "))  # ورودی کاربر
            
            # بررسی رمز عبور
            if user_input == password:
                print("رمز درست است. خوش آمدید!")
                return  # خروج از تابع در صورت درست بودن رمز
            
            # در صورت اشتباه بودن رمز
            tedad_talash += 1  # افزایش شمارش تلاش‌ها
            print(f"رمز اشتباه است. {max_talash - tedad_talash} تلاش باقی مانده.")
        
        except ValueError: 
            print("خطا: لطفاً یک عدد صحیح وارد کنید.")  # پیام خطا برای ورودی نامعتبر

    print("شما بیش از حد تلاش کرده‌اید. برنامه قفل شد.")  # پیام قفل شدن برنامه
check_password()
#اجرای تابع اصلی

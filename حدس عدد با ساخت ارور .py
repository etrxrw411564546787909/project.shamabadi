

print("من یک عددی رو تو ذهنم دارم.بین 1 تا 20  حدس بزن که اون چیه ؟ (: ")
import random

def play_game():
    a, b = 1, 20
    rand = random.randint(a, b)
    attempts = 0  # شمارش تعداد حدس‌ها

    print("من یک عددی رو تو ذهنم دارم. حدس بزن که اون چیه؟ (بین ۱ تا ۲۰)")

    while True:
        try:
            number = int(input("عدد مورد نظر را وارد کنید: "))  # دریافت ورودی از کاربر
            attempts += 1  # افزایش شمارش حدس‌ها

            if number < a or number > b:  # بررسی اینکه عدد در محدوده باشد
                raise ValueError(f"عدد باید بین {a} و {b} باشد.")  # ایجاد خطای سفارشی
            
            if number == rand:
                print(f"..افرین! تو برنده شدی!/n تعداد حدس‌ها: {attempts} ")
                break  # خروج از حلقه در صورت درست حدس زدن
            
            if number > rand:
                print("اشتباه گفتی عزیزم !! یه مقدار بیا پایین‌تر.")
            
            if number < rand:
                print("اشتباه گفتی عزیزم!! یه مقدار بیا بالا‌تر.")
        
        except ValueError as ve:  # مدیریت خطای ورودی نامعتبر و خارج از محدوده
            print(ve)  # چاپ پیام خطای سفارشی
        except Exception as e:  # مدیریت خطای عمومی
            print(f"یک خطای غیرمنتظره رخ داد: {e}")

def main():
    while True:
        play_game()  # بازی را شروع می‌کند
        play_again = input("آیا می‌خواهید دوباره بازی کنید؟ (بله/خیر): ").strip().lower()
        if play_again != 'بله':
            print("خداحافظ! امیدوارم دوباره بازی کنید.")
            break  # خروج از حلقه اصلی و پایان برنامه

if __name__ == "__main__":
    main()  # اجرای تابع اصلی


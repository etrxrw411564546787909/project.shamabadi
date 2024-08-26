# نمایش عنوان بازی
print("***************************بازی تشخیص عدد اول************************ ")

# حلقه بی‌پایان برای دریافت ورودی از کاربر
while True:
    # دریافت عدد دلخواه از کاربر
    number = int(input("یک عدد بنویسید: "))

    # بررسی اینکه آیا عدد وارد شده کمتر یا برابر با 1 است
    if number <= 1: 
        prime = "عدد اول نیست"  # عددهای کمتر از 2 عدد اول نیستند

    # بررسی اینکه آیا عدد برابر با 2 است
    elif number == 2:
        prime = "عدد اول است"  # 2 تنها عدد اول زوج است
    
    # بررسی اعداد بزرگتر از 2
    elif number >= 3:
        # فرض می‌کنیم که عدد اول است تا زمانی که خلاف آن ثابت شود
        prime = "عدد اول است"
        
        # حلقه برای بررسی تقسیم‌پذیری عدد با اعداد از 2 تا عدد-1
        for i in range(2, number):
            if number % i == 0:
                prime = "عدد اول نیست"  # اگر عدد بر i بخش‌پذیر باشد، عدد اول نیست
                break  # خروج از حلقه در صورت یافتن یک مقسوم علیه

    # چاپ نتیجه نهایی
    print(prime, "")

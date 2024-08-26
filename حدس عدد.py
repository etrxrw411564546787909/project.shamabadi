import random  # وارد کردن ماژول random برای تولید اعداد تصادفی

# تعریف محدوده اعداد
a, b = 1, 20  # عدد پایین (1) و عدد بالا (20)

# تولید یک عدد تصادفی بین a و b
rand = random.randint(a, b)

# خوشامدگویی به کاربر
print("من یک عددی رو بین 1 تا 20  تو ذهنم دارم، حدس بزن که اون چیه؟ (:")

# حلقه بی‌نهایت برای ادامه بازی تا زمانی که کاربر عدد صحیح را حدس بزند
while True:
    # درخواست ورودی از کاربر
    number = int(input("عدد مورد نظر را وارد کنید: "))
    
    # بررسی اینکه آیا کاربر عدد را به درستی حدس زده است
    if number == rand:
        print("//.....................افرین تو برنده شدی........................// ")
        break  # خروج از حلقه در صورت حدس صحیح
    
    # بررسی اینکه آیا عدد وارد شده بزرگتر از عدد تصادفی است
    if number > rand:
        print(".اشتباه گفتی عزیزم !! یه مقدار بیا پایین‌تر")
    
    # بررسی اینکه آیا عدد وارد شده کوچکتر از عدد تصادفی است
    if number < rand:
        print("اشتباه گفتی عزیزم!! یه مقدار بیا بالا‌تر")

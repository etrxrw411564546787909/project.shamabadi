import random 

# تعریف کاراکترها به عنوان یک رشته
x = "abcdefghijklmnopqrstuvwxyz 0987654321ABCDEFGHIKLMNOPQRSTUVWXYZ!@#$%^&*"

# درخواست طول رمز از کاربر
number = int(input("میخواهید رمز چند رقمی باشد: "))

# بررسی اینکه طول ورودی بزرگتر از تعداد کاراکترها نباشد
if number > len(x):
    print("طول رمز باید کمتر یا مساوی با", len(x), "باشد.")
else:
    # تولید رمز تصادفی
    randompass = "".join(random.sample(x, number))
    # چاپ رمز تولید شده
    print('پسوورد:', randompass)
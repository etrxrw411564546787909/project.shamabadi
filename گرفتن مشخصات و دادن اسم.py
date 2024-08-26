# تعریف مشخصات افراد در یک دیکشنری
people = {
    " مرتضی": {
        "ghad": 170,
        "vazn": 60,
        "color": "مشکی"
    },
    "علی": {
        "ghad": 100,
        "vazn": 30,
        "color": "آبی"
    },
    "فاطمه": {
        "ghad": 180,
        "vazn": 50,
        "color": "سبز"
    }
}

print("مشخصاتشو بده تا اسمشو بگم...")

# دریافت مشخصات فرد مورد نظر از کاربر
ghad = int(input("قد فرد مورد نظر را وارد کنید: "))
vazn = int(input("وزن فرد مورد نظر را وارد کنید: "))
color = input("رنگ چشم فرد مورد نظر را وارد کنید: ")

# متغیر برای ذخیره نام
name = None

# بررسی مشخصات وارد شده با مشخصات افراد
for person_name, attributes in people.items():
    if (ghad == attributes["ghad"] and 
        vazn == attributes["vazn"] and 
        color == attributes["color"]):
        name = person_name
        break  # اگر نام پیدا شد، از حلقه خارج می‌شویم

# نمایش نتیجه
if name:
    print(f"اسم تو {name} است.")
else:
    print("مشخصاتتو اشتباه گفتی ):")
    
print("حال کردی (:")

    
    
    
    
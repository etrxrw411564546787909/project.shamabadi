

def Success(Getting_Up_Early=0, Interest=0, Diligence=0, Interest_in_Learning=0, Study=0, Sport=0, Coffee_food=0, Sleep=0): 
    """
    محاسبه موفقیت بر اساس عوامل مختلف.
    """
    # بررسی  ورودی‌ها    
    for value in [Getting_Up_Early, Interest, Diligence, Interest_in_Learning, Study, Sport, Coffee_food, Sleep]:
        if not (0 <= value <= 5):
            raise ValueError("تمام ورودی‌ها باید بین 0 تا 5 باشند.")

    # محاسبه نمره موفقیت
    x = (Getting_Up_Early + 2*Interest + 3*Diligence + 4*Interest_in_Learning + 
         2*Study + 2*Sport + 4*Coffee_food + 2*Sleep) / 20   

    # ارائه نتیجه
    if x >= 0.8:
        return "شما در مسیر موفقیت هستید!"
    elif x >= 0.6:
        return "شما در حال پیشرفت هستید."
    elif x >= 0.4:
        return "شما نیاز به تلاش بیشتری دارید."
    else:
        return "شما باید تغییراتی در عادات خود ایجاد کنید."
inputs = [float(input(f"{label} (0 تا 5): ")) for label in 
          ["میزان بیدار شدن زودهنگام", "علاقه", "سخت‌کوشی", 
           "علاقه به یادگیری", "میزان مطالعه", "میزان ورزش", 
           "مصرف قهوه و غذاهای مقوی", "خواب کافی"]]

# فراخوانی تابع و نمایش نتیجه
result = Success(*inputs)
print(result)



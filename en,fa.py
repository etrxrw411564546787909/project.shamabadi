def check_en_fa(text):
    # تعریف حروف زبان‌ها
    en = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    fa = {'ی', 'ه', 'و', 'ن', 'م', 'ل', 'گ', 'ک', 'ق', 'ف', 'غ', 'ع', 'ظ', 'ط', 'ض', 'ص', 'ش', 'س', 'ژ', 'ز', 'ر', 'ذ', 'د', 'خ', 'ح', 'چ', 'ج', 'ث', 'ت', 'پ', 'ب', 'آ', 'ا'}
    
    check_en = any(c in en for c in text.lower())  # بررسی حروف انگلیسی
    check_fa = any(c in fa for c in text)          # بررسی حروف فارسی

    if check_en and not check_fa:
        print("زبان متن شما انگلیسی است.")
    elif check_fa and not check_en:
        print("زبان متن شما فارسی است.")
    elif check_en and check_fa:
        print("متن شما شامل هر دو زبان است.")
    else:
        print("زبان متن شما مشخص نیست.")

    # شمارش حروف هر زبان
    tedad_matn = {'en': 0, 'fa': 0}

    for c in text:
        if c in en:
            tedad_matn['en'] += 1
        elif c in fa:
            tedad_matn['fa'] += 1

    print(f"شمارش حروف:\nانگلیسی: {tedad_matn['en']}\nفارسی: {tedad_matn['fa']}")

# گرفتن متن از کاربر
text = input("میتونی یک متن وارد کنی تا من بهت بگم که زبان اون متن چیه: ")
check_en_fa(text)

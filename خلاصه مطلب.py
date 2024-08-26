# خوش آمدگویی به کاربر
print("به ربات خلاصه کردن متن خوش آمدید ...(:")
print("(:")
print("شما می‌توانید مشخصات خود را به صورت مفصل توضیح دهید و من آن را به صورت خلاصه‌ترین حالت به شما تحویل دهم.")

# مجموعه‌های خالی برای ذخیره مشخصات
name_person = set()
first_name_person = set()
city_person = set()
daneshkah_person = set()
lang_person = set()

# مجموعه‌های مشخصات
name = {'مرتضی', 'مهدی', 'جواد', 'علی', 'رضا'}
first_name = {'شم ابادی', 'محمدی', 'جلالی نسب', 'حسنی', 'احمدی'}
city = {'قم', 'تهران', 'مشهد', 'کرمان', 'شیراز'}
daneshkah = {'شریف', 'تهران', 'آزاد', 'رازی', 'کردستان'}
lang = {'html', 'css', 'js', 'python', 'c++'}

# دریافت ورودی از کاربر
text = input("مشخصات خود را وارد کنید: ")

# تابعی برای استخراج مشخصات از متن
def extract_info(text, valid_set):
    extracted = set()  # مجموعه‌ای برای ذخیره مقادیر استخراج شده
    for word in text.split():  # تقسیم متن به کلمات
        if word in valid_set:  # بررسی اینکه آیا کلمه در مجموعه معتبر وجود دارد
            extracted.add(word)  # اضافه کردن کلمه به مجموعه استخراج شده
    return extracted

# استخراج مشخصات مختلف
name_person = extract_info(text, name)
first_name_person = extract_info(text, first_name)
city_person = extract_info(text, city)
daneshkah_person = extract_info(text, daneshkah)
lang_person = extract_info(text, lang)

# نمایش نتایج
print(f"name = {name_person}")
print(f"first_name = {first_name_person}")
print(f"city = {city_person}")
print(f"daneshkah = {daneshkah_person}")
print(f"lang = {lang_person}")

# خداحافظی
print("به امید دیدار...")

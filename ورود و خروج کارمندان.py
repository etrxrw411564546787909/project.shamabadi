import datetime

# نمایش عنوان برنامه
print("سیستم کنترل ورود و خروج کارمندان")
print("کارمند محترم جهت خروج از سیستم عدد 0 را تایپ کنید")

# لیست‌ها برای ذخیره نام کارمندان و زمان ورود و خروج
karmand_entry = []
time_entry = []
karmand_exit = []
time_exit = []

# حلقه برای ورود کارمندان
while True:
    name = input("کارمند محترم لطفا نام خود را وارد کنید برای ورود: ")
    if name == "0":
        break  # خروج از حلقه در صورت وارد کردن 0

    # ثبت زمان ورود
    current_time = datetime.datetime.now()
    time_entry.append(current_time.strftime("%H:%M:%S"))  # فرمت زمان به ساعت:دقیقه:ثانیه
    karmand_entry.append(name)  # ذخیره نام کارمند

# حلقه برای خروج کارمندان
while True:
    name = input("کارمند محترم لطفا نام خود را وارد کنید برای خروج: ")
    if name == "0":
        break  # خروج از حلقه در صورت وارد کردن 0

    # ثبت زمان خروج
    current_time = datetime.datetime.now()
    time_exit.append(current_time.strftime("%H:%M:%S"))  # فرمت زمان به ساعت:دقیقه:ثانیه
    karmand_exit.append(name)  # ذخیره نام کارمند

# بررسی و نمایش اطلاعات ورود و خروج
if len(karmand_entry) == len(time_entry):
    for i in range(len(karmand_entry)):
        print(f"{karmand_entry[i]} ، وارد شد در ساعت {time_entry[i]}")
        if i < len(karmand_exit):
            print(f"{karmand_exit[i]} ، خارج شد در ساعت {time_exit[i]}")
        else:
            print(f"{karmand_entry[i]} ، هنوز خارج نشده است.")
else:
    # بررسی کارمندان که وارد شده‌اند اما خارج نشده‌اند
    set_entry = set(karmand_entry)
    set_exit = set(karmand_exit)

    if len(karmand_entry) > len(karmand_exit):
        not_exited = set_entry.difference(set_exit)
        for name in not_exited:
            index = karmand_entry.index(name)
            print(f"کارمند {name} در ساعت {time_entry[index]} وارد شده است و خارج نشده است.")
    elif len(karmand_entry) < len(karmand_exit):
        not_entered = set_exit.difference(set_entry)
        for name in not_entered:
            index = karmand_exit.index(name)
            print(f"کارمند {name} در ساعت {time_exit[index]} خارج شده است و هنوز وارد نشده است.")

# محاسبه زمان کل حضور کارمندان
for i in range(len(karmand_entry)):
    if i < len(karmand_exit):
        entry_time = datetime.datetime.strptime(time_entry[i], "%H:%M:%S")
        exit_time = datetime.datetime.strptime(time_exit[i], "%H:%M:%S")
        duration = exit_time - entry_time
        print(f"{karmand_entry[i]} در مجموع {duration} در اداره بوده است.")
    else:
        print(f"{karmand_entry[i]} هنوز خارج نشده است.")

print("به امید دیدار..")

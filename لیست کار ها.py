def add_task(tasks):
    task = input("کار جدید را وارد کنید: ")
    tasks.append(task)
    print(f"کار '{task}' به لیست اضافه شد.")

def view_tasks(tasks):
    if tasks:
        print("\nکارهای شما:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("لیست کارها خالی است.")

def remove_task(tasks):
    if tasks:
        try:
            task_index = int(input("شماره کار برای حذف را وارد کنید: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"کار '{removed_task}' حذف شد.")
            else:
                print("شماره کار نامعتبر است.")
        except ValueError:
            print("لطفاً یک شماره معتبر وارد کنید.")
    else:
        print("لیست کارها خالی است.")

def main():
    tasks = []  # لیست کارها

    while True:
        print("\n--- مدیریت لیست کارها ---")
        print("1. افزودن کار")
        print("2. مشاهده کارها")
        print("3. حذف کار")
        print("4. خروج")
        
        entekhab = input("انتخاب خود را وارد کنید: ")

        if entekhab == '1':
            add_task(tasks)
        elif entekhab == '2':
            view_tasks(tasks)
        elif entekhab == '3':
            remove_task(tasks)
        elif entekhab == '4':
            print("خداحافظ!")
            break
        else:
            print("انتخاب نامعتبر است.")

# اجرای برنامه
if __name__ == "__main__":
    main()

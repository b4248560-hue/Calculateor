import datetime
import tkinter as tk

# 1. إعداد النافذة الرئيسية للتطبيق
window = tk.Tk()
window.geometry("620x600")
window.title("Age Calculator App")

# 2. إنشاء مربعات العناوين (Labels)
name = tk.Label(text="Name")
name.grid(column=0, row=1)

year = tk.Label(text="Year")
year.grid(column=0, row=2)

month = tk.Label(text="Month")
month.grid(column=0, row=3)

date = tk.Label(text="Day")
date.grid(column=0, row=4)

# 3. إنشاء حقول الإدخال للحصول على البيانات من المستخدم (Entries)
nameEntry = tk.Entry()
nameEntry.grid(column=1, row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1, row=2)

monthEntry = tk.Entry()
monthEntry.grid(column=1, row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1, row=4)


# 4. تعريف كلاس Person لحساب العمر بناءً على تاريخ الميلاد
class Person:

  def __init__(self, name, birthdate):
    self.name = name
    self.birthdate = birthdate

  def age(self):
    today = datetime.date.today()
    age = today.year - self.birthdate.year
    return age


# 5. تعريف دالة getInput للحصول على مدخلات المستخدم وعرض النتيجة
def getInput():
  name = nameEntry.get()
  users = Person(
      name,
      datetime.date(
          int(yearEntry.get()), int(monthEntry.get()), int(dateEntry.get())
      ),
  )

  textArea = tk.Text(master=window, height=10, width=25)
  textArea.grid(column=1, row=6)

  answer = "Heyy {users}!!! You are {age} years old!!! ".format(
      users=name, age=users.age()
  )
  textArea.insert(tk.END, answer)


# 6. إنشاء زر حساب العمر وربطه بالدالة
button = tk.Button(window, text="Calculate Age", command=getInput, bg="pink")
button.grid(column=1, row=5)

# 7. تشغيل النافذة بشكل دائم
window.mainloop()

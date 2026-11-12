from tkinter import Label, Tk
import time

# 1. إعداد النافذة وعنوانها وحجمها
clk_window = Tk()
clk_window.title("ساعة رقمية")
clk_window.geometry("450x200")
clk_window.resizable(1, 1)
clk_window.config(bg="yellow")

# 2. تحديد نوع الخط، لون الخلفية، ولون الخط
text_font = ("Boulder", 45, "bold")
date_font = ("Arial", 16, "bold")
background = "yellow"
foreground = "red"

# 3. عرض مربع العنوان (Label) للساعة
label = Label(
    clk_window,
    font=text_font,
    bg=background,
    fg=foreground,
)
label.pack(anchor="center", pady=20)

# 4. عرض مربع إضافي للتاريخ (تنفيذاً لنشاط الكتاب)
date_label = Label(
    clk_window, font=date_font, bg=background, fg="#333333"
)
date_label.pack(anchor="center")


# 5. الوظيفة الرئيسية لتحديث الساعة والتاريخ باستمرار
def digital_clock():
  # تحديث الوقت (ساعات، دقائق، ثواني)
  time_live = time.strftime("%H:%M:%S")
  label.config(text=time_live)

  # تحديث التاريخ (اليوم، الشهر، السنة) - تنفيذاً للنشاط
  date_live = time.strftime("%b %d %Y")
  date_label.config(text=date_live)

  # استدعاء الدالة مرة أخرى بعد 200 مللي ثانية
  label.after(200, digital_clock)


# استدعاء دالة digital_clock() ونرى النتيجة
digital_clock()

# تشغيل النافذة وثباتها (نهاية البرنامج)
clk_window.mainloop()

import tkinter as tk

# Solar Hijri 1405 months and days
months_1405 = [
    ("حمل", 31),
    ("ثور", 31),
    ("جوزا", 31),
    ("سرطان", 31),
    ("اسد", 31),
    ("سنبله", 30),
    ("میزان", 30),
    ("عقرب", 30),
    ("قوس", 30),
    ("جدی", 30),
    ("دلو", 30),
    ("حوت", 29)
]

# Create main window
root = tk.Tk()
root.title("هجري شمسي جنتری - کال ۱۴۰۵")

main_frame = tk.Frame(root, bg="white")
main_frame.pack(padx=10, pady=10)

# Generate calendar boxes
for i, (month_name, days) in enumerate(months_1405):
    frame = tk.Frame(main_frame, bd=2, relief="ridge", padx=10, pady=10)
    frame.grid(row=i // 3, column=i % 3, padx=8, pady=8)

    # Month title
    title = tk.Label(frame, text=f"{month_name} ۱۴۰۵", font=("Arial", 14, "bold"))
    title.pack()

    # Create calendar text
    text = "ش ی د س چ پ ج\n"
    day_count = 1

    # Start every month on Saturday for simplicity
    # (You can change this if you want real weekday alignment)
    week = [" "] * 7

    for d in range(days):
        week[d % 7] = str(d + 1).rjust(2)
        if (d + 1) % 7 == 0:
            text += " ".join(week) + "\n"
            week = [" "] * 7

    if any(day != " " for day in week):
        text += " ".join(week) + "\n"

    cal_label = tk.Label(frame, text=text, font=("Courier", 10), justify="left")
    cal_label.pack()

root.mainloop()

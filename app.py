import tkinter as tk

root = tk.Tk()
root.title("دفتر اندیکاتور اداری")
root.geometry("900x600")

title = tk.Label(
    root,
    text="دفتر اندیکاتور اداری",
    font=("Tahoma", 18, "bold")
)
title.pack(pady=20)

label = tk.Label(
    root,
    text="نویسنده و طراح: جعفر عبدی",
    font=("Tahoma", 11)
)
label.pack(pady=10)

root.mainloop()

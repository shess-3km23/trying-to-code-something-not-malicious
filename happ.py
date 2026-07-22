import customtkinter as ctk
import subprocess


ctk.set_appearance_mode("green")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x100")
app.title("happy")

def happy():
    print(f"Happy !")

btn = ctk.CTkButton(app, text="happy", command=happy)
btn.pack(padx=20, pady=35)

app.mainloop()
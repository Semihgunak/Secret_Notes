import tkinter as tk
import base64
from tkinter import ttk
from tkinter import messagebox

gui = tk.Tk()
gui.geometry('400x600')
gui.title("Secret Notes")
gui.config(padx=30,pady=30)

def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def encrypt_and_save():
    input_data =Text_main.get("1.0", "end-1c")
    password = password_entry.get()
    encrypted_data = encode(password, input_data)
    file = open('index.txt', 'a+')
    file.write('\n' + title_enter.get()+ '\n',)
    file.write(encrypted_data)
    file.close()
    Text_main.delete("1.0", "end")
    title_enter.delete(0,"end")
    password_entry.delete(0, "end")
    messagebox.showinfo("Success", "Data encrypted and saved successfully.")

def decrypt():
    input_data = Text_main.get("1.0", "end-1c")
    password = password_entry.get()

    decoded_data = decode(password, input_data)
    Text_main.delete("1.0", "end")
    Text_main.insert("1.0", decoded_data)
    messagebox.showinfo("Success", "Data decrypt successfully.")

canvas = tk.Canvas(height=200, width=200)
logo = tk.PhotoImage(file="../topsecret.png")
canvas.create_image(100,100,image=logo)
canvas.pack()
etiket1=tk.Label(text="Enter Your Title")
etiket1.pack()
title_enter=tk.Entry(width=40)
title_enter.pack()
etiket2=tk.Label(text="Enter Your Secret")
etiket2.pack()
Text_main = tk.Text(width=40, height=10)
Text_main.pack()
label= tk.Label(text="Enter Master Key")
label.pack()
password_entry=tk.Entry(width=30)
password_entry.pack()
butonWrite = tk.Button(gui)
butonWrite.config(text = 'Save and Encrypt', command = encrypt_and_save)
butonWrite.pack()

button= tk.Button()
button.config(text = 'Decrypt', command = decrypt)
button.pack()

gui.mainloop()
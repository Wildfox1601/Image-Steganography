import tkinter as tk
from tkinter import filedialog, messagebox
import encryption
import decryption

def select_image():
    filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if filepath:
        entry_filepath.delete(0, tk.END)
        entry_filepath.insert(0, filepath)

def encrypt_image():
    filepath = entry_filepath.get()
    msg = entry_message.get()
    password = entry_password.get()
    if not filepath or not msg or not password:
        messagebox.showerror("Error", "All fields are required!")
        return
    encryption.encrypt(filepath, msg)
    messagebox.showinfo("Success", "Encrypted image saved as encryptedImage.jpg")

def decrypt_image():
    filepath = entry_filepath.get()
    msg_length = len(entry_message.get())
    password = entry_password.get()
    pas = entry_passcode.get()
    if password != pas:
        messagebox.showerror("Error", "Incorrect passcode!")
        return
    message = decryption.decrypt(filepath, msg_length)
    messagebox.showinfo("Decryption", f"Decrypted message: {message}")

root = tk.Tk()
root.title("Image Steganography")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(pady=10)

label_filepath = tk.Label(frame, text="Select Image:")
label_filepath.grid(row=0, column=0)
entry_filepath = tk.Entry(frame, width=30)
entry_filepath.grid(row=0, column=1)
btn_browse = tk.Button(frame, text="Browse", command=select_image)
btn_browse.grid(row=0, column=2)

label_message = tk.Label(frame, text="Enter Secret Message:")
label_message.grid(row=1, column=0)
entry_message = tk.Entry(frame, width=30)
entry_message.grid(row=1, column=1)

label_password = tk.Label(frame, text="Enter Passcode:")
label_password.grid(row=2, column=0)
entry_password = tk.Entry(frame, width=30, show="*")
entry_password.grid(row=2, column=1)

btn_encrypt = tk.Button(frame, text="Encrypt Image", command=encrypt_image)
btn_encrypt.grid(row=3, column=0, columnspan=2, pady=5)

label_passcode = tk.Label(frame, text="Enter Passcode for Decryption:")
label_passcode.grid(row=4, column=0)
entry_passcode = tk.Entry(frame, width=30, show="*")
entry_passcode.grid(row=4, column=1)

btn_decrypt = tk.Button(frame, text="Decrypt Image", command=decrypt_image)
btn_decrypt.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()

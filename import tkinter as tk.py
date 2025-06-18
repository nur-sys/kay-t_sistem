import tkinter as tk
from tkinter import messagebox
import csv
import os

csv_file = "ogrenci_kayitlari.csv"

def dosyadan_oku():
    if not os.path.exists(csv_file):
        return []
    with open(csv_file, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def dosyaya_yaz(students):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Ad", "Numara", "Bölüm"])
        writer.writeheader()
        for s in students:
            writer.writerow(s)

def kaydet():
    ad = entry_ad.get()
    numara = entry_no.get()
    bolum = entry_bolum.get()

    if not ad or not numara or not bolum:
        messagebox.showwarning("Eksik bilgi", "Tüm alanları doldurunuz!")
        return

    students.append({"Ad": ad, "Numara": numara, "Bölüm": bolum})
    dosyaya_yaz(students)
    guncelle_liste()
    entry_ad.delete(0, tk.END)
    entry_no.delete(0, tk.END)
    entry_bolum.delete(0, tk.END)
    messagebox.showinfo("Başarılı", "Öğrenci başarıyla eklendi!")

def guncelle_liste():
    listbox.delete(0, tk.END)
    for i, s in enumerate(students, start=1):
        listbox.insert(tk.END, f"{i}. {s['Ad']} - {s['Numara']} - {s['Bölüm']}")

def sil():
    secili = listbox.curselection()
    if not secili:
        messagebox.showwarning("Uyarı", "Lütfen silinecek öğrenciyi seçiniz.")
        return
    index = secili[0]
    del students[index]
    dosyaya_yaz(students)
    guncelle_liste()
    messagebox.showinfo("Silindi", "Öğrenci silindi.")

# Başlangıç
students = dosyadan_oku()

# Arayüz
root = tk.Tk()
root.title("Öğrenci Kayıt Sistemi")
root.geometry("500x500")

tk.Label(root, text="Ad Soyad").pack()
entry_ad = tk.Entry(root, width=40)
entry_ad.pack()

tk.Label(root, text="Öğrenci No").pack()
entry_no = tk.Entry(root, width=40)
entry_no.pack()

tk.Label(root, text="Bölüm").pack()
entry_bolum = tk.Entry(root, width=40)
entry_bolum.pack()

tk.Button(root, text="Kaydet", command=kaydet).pack(pady=5)
tk.Button(root, text="Seçili Kaydı Sil", command=sil).pack(pady=5)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)

guncelle_liste()
root.mainloop()

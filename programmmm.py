import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from soal import soal_jawaban

skor = 0
soal_tersedia = soal_jawaban.copy()
nama_pengguna = ""

#Fungsi memperbarui skor
def perbarui_skor():
    label_skor.config(text=f"Skor: {skor}")

#Fungsi cek jawaban
def cek_jawaban(jawaban, jawaban_benar):
    global skor
    if jawaban==jawaban_benar:
        messagebox.showinfo("Hasil", "Benar! Jawaban kamu tepat!")
        skor += 10
    else:
        messagebox.showerror("Hasil", f"Salah! Jawaban yang benar: {jawaban_benar}")
    perbarui_skor()
    tampilkan_soal()

# Fungsi Tampilkan Soal
def tampilkan_soal():
    global soal_tersedia
    if not soal_tersedia:
        messagebox.showinfo("Kuis Selesai", f"Skor Akhir: {skor}")
        simpan_skor()
        utama.quit()
        return
    
    soal = random.choice(soal_tersedia)
    soal_tersedia.remove(soal)
    label_soal.config(text=soal["soal"])

    for i, opsi in enumerate(soal["opsi"]):
        tombol_opsi[i].config(
            text=opsi, 
            bg="lightgray", 
            command=lambda jawaban=opsi: cek_jawaban(jawaban, soal["jawaban"])
        )

# Fungsi Simpan Skor
def simpan_skor():
    with open("skor.txt", "a") as file:
        file.write(f"{nama_pengguna}: Skor Akhir: {skor}\n")

# Fungsi Mulai Kuis
def mulai_kuis():
    global nama_pengguna
    nama_pengguna = masukan_nama.get()
    if nama_pengguna.strip() == "":
        messagebox.showwarning("Peringatan", "Nama tidak boleh kosong!")
        return
    bingkai_nama.place_forget()
    tampilkan_soal()

# Fungsi Perbarui Latar Belakang
def perbarui_latar():
    lebar = utama.winfo_width()
    tinggi = utama.winfo_height()
    gambar_diubah = gambar_latar.resize((lebar, tinggi), Image.Resampling.LANCZOS)
    foto_diubah = ImageTk.PhotoImage(gambar_diubah)
    label_latar.config(image=foto_diubah)
    label_latar.image = foto_diubah

# Membuat Jendela Utama
utama = tk.Tk()
utama.title("Kuis Matematika - Bangun Datar")

# Latar Belakang
gambar_latar = Image.open("background.jpg")
foto_latar = ImageTk.PhotoImage(gambar_latar)

# Tampilkan Latar
label_latar = tk.Label(utama, image=foto_latar)
label_latar.place(x=0, y=0, relwidth=1, relheight=1)

# Bingkai Input Nama
bingkai_nama = tk.Frame(utama, bg="dodgerblue", padx=10, pady=10)
bingkai_nama.place(relwidth=1, relheight=1)

# Label Input Nama
label_nama = tk.Label(bingkai_nama, text="Masukkan Nama:", 
                      font=("Arial", 16, "bold"), fg="white", bg="dodgerblue")
label_nama.pack(pady=20)

# Kotak Masukan Nama
masukan_nama = tk.Entry(bingkai_nama, font=("Arial", 14), width=30)
masukan_nama.pack(pady=10)

# Tombol Mulai
tombol_mulai = tk.Button(bingkai_nama, text="Mulai Kuis", font=("Arial", 12), 
                         bg="lightgreen", command=mulai_kuis)
tombol_mulai.pack(pady=20)

# Bingkai Header
bingkai_header = tk.Frame(utama, bg="dodgerblue", padx=10, pady=10)
bingkai_header.place(relwidth=1, y=10)

# Judul Aplikasi
judul_aplikasi = tk.Label(bingkai_header, text="Kuis Matematika - Bangun Datar", 
                          font=("Arial", 16, "bold"), fg="white", bg="dodgerblue")
judul_aplikasi.pack()

# Tampilkan Skor
label_skor = tk.Label(bingkai_header, text=f"Skor: {skor}", font=("Arial", 12), fg="white", bg="dodgerblue")
label_skor.pack()

# Bingkai Pertanyaan
bingkai_soal = tk.Frame(utama, bg="white", padx=10, pady=10)
bingkai_soal.place(relx=0.5, rely=0.5, anchor="center")

# Label Soal
label_soal = tk.Label(bingkai_soal, text="", font=("Arial", 14), wraplength=400, justify="center", bg="white")
label_soal.pack(pady=20)

# Tombol Jawaban
tombol_opsi = []
for _ in range(4):
    tombol = tk.Button(bingkai_soal, text="", font=("Arial", 12), width=30, 
                       bg="lightblue", activebackground="skyblue")
    tombol.pack(pady=5)
    tombol_opsi.append(tombol)

# Perbarui Latar Saat Ukuran Berubah
utama.bind("<Configure>", lambda event: perbarui_latar())

# Jalankan Aplikasi
utama.mainloop()

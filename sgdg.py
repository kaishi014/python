"""Sandi Penggalang Putra — aplikasi latihan 5 jenis sandi."""  # Penjelasan singkat isi file

from __future__ import annotations  # Supaya tipe data modern (list[dict]) aman di Python 3.11

import random  # Dipakai untuk mengacak urutan soal dan pilihan jawaban
import tkinter as tk  # Pustaka tampilan jendela, tombol, dan teks (sudah ada di Python)
from tkinter import font as tkfont  # Dipakai untuk mengatur ukuran dan jenis huruf


HIJAU_TUA = "#14261c"  # Warna latar jendela (hijau hutan tua)
HIJAU = "#1f3d2b"  # Warna batang header di atas
HIJAU_MUDA = "#2f6b45"  # Warna tombol pilihan jawaban
KHAKI = "#c9a227"  # Warna judul dan tombol utama
KRIM = "#f4ead0"  # Warna teks penjelasan
PUTIH = "#f7f3e8"  # Warna teks soal
MERAH = "#c0392b"  # Warna nyawa
EMAS = "#f1c40f"  # Warna skor
ABU = "#8aa08d"  # Warna teks sekunder

SOAL = [  # Daftar 5 soal; tiap item adalah kamus (dict)
    {  # Soal 1: sandi jam
        "jenis": "Sandi Jam",  # Nama jenis sandi, tampil di header
        "tanya": "Ubah sandi jam ini menjadi kata (tiap huruf berjarak 5 menit):\n08.25 - 07.20 - 07.30 - 08.40",  # REGU
        "opsi": ["REGU", "RAWA", "TALI", "API"],  # Empat pilihan jawaban
        "jawab": "REGU",  # Kunci: 08.25=R  07.20=E  07.30=G  08.40=U
        "hint": "A=07.00, B=07.05, dan seterusnya tiap 5 menit. Contoh: R=08.25.",  # Petunjuk singkat
    },  # Selesai soal jam
    {  # Soal 2: sandi nomor
        "jenis": "Sandi Nomor",  # Huruf diganti angka abjad
        "tanya": "Sandi nomor (A=1 ... Z=26):\n11 - 15 - 13 - 16 - 1 - 19",  # 11=K 15=O 13=M 16=P 1=A 19=S
        "opsi": ["KOMPAS", "KAPAK", "KEMAH", "KALIAN"],  # Pilihan, satu yang benar
        "jawab": "KOMPAS",  # Kunci jawaban soal nomor
        "hint": "11=K  15=O  13=M  16=P  1=A  19=S",  # Bantuan menghitung huruf
    },  # Selesai soal nomor
    {  # Soal 3: sandi koordinat
        "jenis": "Sandi AZ",  # Huruf dipasangkan dari ujung alfabet
        "tanya": "Ubah sandi AZ ini menjadi kata:\nG Z O R",  # TALI dikodekan menjadi GZOR
        "opsi": ["TALI", "TENTU", "TARA", "KITA"],  # Pilihan jawaban
        "jawab": "TALI",  # G=T  Z=A  O=L  R=I
        "hint": "A=Z, B=Y, dan seterusnya sampai M=N. Contoh: TALI menjadi GZOR.",  # Petunjuk sandi AZ
    },  # Selesai soal sandi AZ
    {  # Soal 4: sandi Morse
        "jenis": "Sandi Morse",  # Titik dan strip
        "tanya": "Ubah Morse ini menjadi kata:\n.--.   .-.   .-   --   ..-   -.-   .-",  # PRAMUKA
        "opsi": ["PRAMUKA", "PENGALANG", "PERKEMAH", "PEMBINA"],  # Pilihan
        "jawab": "PRAMUKA",  # Kunci Morse
        "hint": "P=.--.  R=.-.  A=.-  M=--  U=..-  K=-.-",  # Tabel huruf yang dipakai
    },  # Selesai soal Morse
    {  # Soal 5: sandi semaphore
        "jenis": "Sandi AN",  # Sandi geser dengan pasangan A=N
        "tanya": "Ubah sandi AN ini menjadi kata:\nN C V",  # API dikodekan menjadi NCV
        "opsi": ["API", "AIR", "TALI", "REGU"],  # Pilihan
        "jawab": "API",  # Kunci sandi AN
        "hint": "A=N, B=O, dan seterusnya; setelah Z kembali ke A.",  # Petunjuk singkat
    },  # Selesai soal sandi AN
]  # Selesai daftar soal

KETERANGAN = [  # Teks penjelasan lengkap, dipakai di halaman keterangan
    (  # Pasangan (judul, isi) untuk sandi jam
        "Sandi Jam",  # Judul bagian
        "A=07.00, B=07.05, dan setiap huruf berikutnya maju 5 menit.\n"  # Aturan
        "C=07.10  D=07.15  E=07.20  F=07.25  G=07.30  H=07.35\n"  # C sampai H
        "I=07.40  J=07.45  K=07.50  L=07.55  M=08.00  N=08.05\n"  # I sampai N
        "O=08.10  P=08.15  Q=08.20  R=08.25  S=08.30  T=08.35\n"  # O sampai T
        "U=08.40  V=08.45  W=08.50  X=08.55  Y=09.00  Z=09.05",  # U sampai Z
    ),  # Selesai keterangan jam
    (  # Keterangan sandi nomor
        "Sandi Nomor",  # Judul
        "Huruf diganti nomor urut abjad. A=1 sampai Z=26.\nContoh: 1-16-9 = API",  # Aturan + contoh
    ),  # Selesai keterangan nomor
    (  # Keterangan sandi koordinat
        "Sandi AZ",  # Judul
        "Pasangkan huruf dari ujung alfabet: A=Z, B=Y, C=X, dan seterusnya sampai M=N.\n"  # Aturan
        "N=M, O=L, P=K, Q=J, R=I, S=H, T=G, U=F, V=E, W=D, X=C, Y=B, Z=A.\n"  # Pasangan sisanya
        "Contoh: TALI menjadi GZOR. Gunakan pasangan yang sama untuk membaca kembali.",  # Contoh
    ),  # Selesai keterangan sandi AZ
    (  # Keterangan Morse
        "Sandi Morse",  # Judul
        "Titik (.) singkat, strip (-) panjang.\n"  # Aturan
        "A=.-  I=..  K=-.-  M=--  P=.--.  R=.-.  U=..-",  # Huruf yang muncul di soal
    ),  # Selesai keterangan Morse
    (  # Keterangan semaphore
        "Sandi AN",  # Judul
        "Setiap huruf diganti huruf 13 langkah sesudahnya.\n"  # Aturan
        "A=N  B=O  C=P  D=Q  E=R  F=S  G=T  H=U  I=V  J=W  K=X  L=Y  M=Z\n"  # A sampai M
        "N=A  O=B  P=C  Q=D  R=E  S=F  T=G  U=H  V=I  W=J  X=K  Y=L  Z=M\n"  # N sampai Z
        "Contoh: API menjadi NCV. Untuk membaca kembali, gunakan pasangan yang sama.",  # Contoh
    ),  # Selesai keterangan sandi AN
]  # Selesai daftar keterangan


class SandiPutra:  # Kelas utama aplikasi; semua layar ada di sini
    def __init__(self, root: tk.Tk) -> None:  # Dipanggil sekali saat program mulai
        self.root = root  # Simpan jendela utama supaya bisa dipakai fungsi lain
        self.root.title("Sandi Penggalang Putra")  # Tulisan di batang judul Windows
        self.root.geometry("820x620")  # Ukuran awal jendela: lebar 820, tinggi 620
        self.root.minsize(760, 560)  # Jendela tidak boleh lebih kecil dari ini
        self.root.configure(bg=HIJAU_TUA)  # Cat latar belakang jendela

        self.judul_font = tkfont.Font(family="Segoe UI", size=24, weight="bold")  # Huruf judul besar
        self.sub_font = tkfont.Font(family="Segoe UI", size=13)  # Huruf sedang untuk soal
        self.teks_font = tkfont.Font(family="Segoe UI", size=12)  # Huruf isi biasa
        self.tombol_font = tkfont.Font(family="Segoe UI", size=12, weight="bold")  # Huruf tombol
        self.kecil_font = tkfont.Font(family="Segoe UI", size=10)  # Huruf petunjuk / status

        self.skor = 0  # Nilai awal pemain
        self.nyawa = 3  # Kesempatan salah, maksimal 3
        self.nomor = 0  # Indeks soal yang sedang dikerjakan (0 sampai 4)
        self.soal_acak: list[dict] = []  # Tempat menyimpan 5 soal setelah diacak
        self.bingkai: tk.Frame | None = None  # Frame layar yang sedang tampil; None = belum ada
        self.status = tk.StringVar(value="")  # Teks status (benar/salah) yang bisa diubah
        self.sedang_latihan = False  # True jika pemain sedang mengerjakan soal
        self.buka_menu()  # Setelah siap, tampilkan menu awal

    def reset(self) -> None:  # Mengembalikan permainan ke kondisi awal
        self.skor = 0  # Skor mulai dari nol
        self.nyawa = 3  # Nyawa diisi penuh lagi
        self.nomor = 0  # Kembali ke soal pertama
        self.soal_acak = list(SOAL)  # Salin daftar soal (supaya data asli tidak rusak)
        random.shuffle(self.soal_acak)  # Acak urutan 5 soal
        self.status.set("5 jenis sandi. Kerjakan dengan teliti.")  # Pesan pembuka

    def bersihkan(self) -> tk.Frame:  # Hapus layar lama, buat frame baru
        if self.bingkai is not None:  # Kalau sudah ada layar sebelumnya
            self.bingkai.destroy()  # Buang layar lama supaya tidak numpuk
        self.bingkai = tk.Frame(self.root, bg=HIJAU_TUA)  # Buat wadah layar baru
        self.bingkai.pack(fill="both", expand=True)  # Isi seluruh jendela
        return self.bingkai  # Kembalikan frame baru ke pemanggil

    def header(self, induk: tk.Frame, judul: str) -> None:  # Batang atas: judul, nyawa, skor
        bar = tk.Frame(induk, bg=HIJAU, padx=16, pady=10)  # Wadah header
        bar.pack(fill="x")  # Lebar penuh
        tk.Label(bar, text=judul, font=self.sub_font, fg=KHAKI, bg=HIJAU).pack(side="left")  # Judul kiri
        kanan = tk.Frame(bar, bg=HIJAU)  # Wadah nyawa dan skor
        kanan.pack(side="right")  # Tempel di kanan header
        tk.Label(  # Label nyawa
            kanan,  # Letakkan di sisi kanan header
            text=f"Nyawa  {'♥ ' * self.nyawa}{'♡ ' * (3 - self.nyawa)}",  # Hati penuh / kosong
            font=self.sub_font,  # Huruf sedang
            fg=MERAH,  # Warna merah
            bg=HIJAU,  # Latar sama dengan header
        ).pack(side="left", padx=10)  # Jarak dari skor
        tk.Label(kanan, text=f"Skor  {self.skor}", font=self.sub_font, fg=EMAS, bg=HIJAU).pack(  # Label skor
            side="left"  # Di kanan nyawa
        )  # Selesai pack skor

    def tombol(self, induk: tk.Widget, teks: str, perintah, lebar: int = 24) -> None:  # Tombol utama khaki
        tk.Button(  # Buat tombol
            induk,  # Ditempel di wadah yang diberikan
            text=teks,  # Tulisan di tombol
            command=perintah,  # Fungsi yang dijalankan saat diklik
            font=self.tombol_font,  # Huruf tebal
            bg=KHAKI,  # Warna tombol
            fg=HIJAU_TUA,  # Warna tulisan
            activebackground=EMAS,  # Warna saat ditekan
            relief="flat",  # Tanpa tepi 3D
            padx=14,  # Jarak dalam kiri-kanan
            pady=8,  # Jarak dalam atas-bawah
            width=lebar,  # Lebar tombol dalam karakter
            cursor="hand2",  # Kursor jadi tangan
        ).pack(pady=6)  # Jarak antar tombol

    def tombol_opsi(self, induk: tk.Widget, teks: str, perintah) -> None:  # Tombol pilihan A/B/C/D
        tk.Button(  # Buat tombol jawaban
            induk,  # Ditempel di area soal
            text=teks,  # Teks pilihan, misalnya REGU
            command=perintah,  # Dipanggil saat dipilih
            font=self.teks_font,  # Huruf isi
            bg=HIJAU_MUDA,  # Latar hijau muda
            fg=PUTIH,  # Tulisan terang
            activebackground=KHAKI,  # Berubah khaki saat ditekan
            activeforeground=HIJAU_TUA,  # Tulisan gelap saat ditekan
            relief="flat",  # Tampilan datar
            anchor="w",  # Teks rata kiri
            padx=16,  # Padding samping
            pady=10,  # Padding vertikal
            cursor="hand2",  # Kursor tangan
        ).pack(fill="x", pady=5)  # Lebar penuh, jarak 5 piksel

    def buka_menu(self) -> None:  # Layar pertama: judul dan 3 tombol
        self.sedang_latihan = False  # Belum mulai mengerjakan soal
        frame = self.bersihkan()  # Buat layar kosong
        tengah = tk.Frame(frame, bg=HIJAU_TUA)  # Wadah di tengah jendela
        tengah.place(relx=0.5, rely=0.46, anchor="center")  # Posisi hampir tengah
        tk.Label(tengah, text="SANDI PENGGALANG PUTRA", font=self.judul_font, fg=KHAKI, bg=HIJAU_TUA).pack()  # Judul
        tk.Label(  # Subjudul 5 jenis sandi
            tengah,  # Di bawah judul
                     text="Jam  •  Nomor  •  Sandi AZ  •  Morse  •  Sandi AN",  # Daftar jenis
            font=self.teks_font,  # Huruf isi
            fg=ABU,  # Warna abu
            bg=HIJAU_TUA,  # Latar sama
        ).pack(pady=(8, 22))  # Jarak atas 8, bawah 22
        self.tombol(tengah, "Mulai", self.mulai)  # Mulai latihan
        self.tombol(tengah, "Keterangan Sandi", self.buka_keterangan)  # Buka penjelasan
        self.tombol(tengah, "Cara Main", self.buka_cara)  # Buka aturan main

    def buka_cara(self) -> None:  # Layar aturan permainan
        frame = self.bersihkan()  # Ganti layar
        self.header(frame, "Cara Main")  # Header dengan judul
        isi = tk.Frame(frame, bg=HIJAU_TUA, padx=36, pady=20)  # Area teks aturan
        isi.pack(fill="both", expand=True)  # Isi sisa jendela
        for teks in (  # Ulangi untuk setiap baris aturan
            "Ada 5 soal. Tiap soal memakai jenis sandi yang berbeda.",  # Aturan 1
                        "Jenisnya: jam, nomor, sandi AZ, Morse, dan sandi AN.",  # Aturan 2
            "Nyawa 3. Jawaban salah mengurangi 1 nyawa.",  # Aturan 3
            "Jawaban benar +10. Selesai jika 5 soal tuntas atau nyawa habis.",  # Aturan 4
            "Urutan soal dan pilihan jawaban diacak setiap main.",  # Aturan 5
        ):  # Selesai daftar aturan
            tk.Label(  # Tampilkan satu baris
                isi, text=f"•  {teks}", font=self.teks_font, fg=KRIM, bg=HIJAU_TUA, anchor="w"  # Bullet + teks
            ).pack(fill="x", pady=5)  # Lebar penuh, jarak 5
        self.tombol(isi, "Kembali", self.buka_menu, lebar=16)  # Kembali ke menu

    def buka_keterangan(self) -> None:  # Layar penjelasan 5 sandi
        frame = self.bersihkan()  # Ganti layar
        self.header(frame, "Keterangan Sandi")  # Header
        isi = tk.Frame(frame, bg=HIJAU_TUA, padx=36, pady=12)  # Area isi
        isi.pack(fill="both", expand=True)  # Isi jendela
        for judul, teks in KETERANGAN:  # Ambil judul dan penjelasan satu per satu
            tk.Label(isi, text=judul, font=self.sub_font, fg=KHAKI, bg=HIJAU_TUA, anchor="w").pack(  # Judul jenis
                fill="x", pady=(8, 2)  # Jarak atas lebih besar
            )  # Selesai judul
            tk.Label(  # Isi keterangan
                isi, text=teks, font=self.kecil_font, fg=KRIM, bg=HIJAU_TUA, justify="left", anchor="w"  # Rata kiri
            ).pack(fill="x")  # Lebar penuh
        if self.sedang_latihan:  # Kalau pemain sedang di tengah soal
            self.tombol(isi, "Kembali ke Soal", self.buka_soal, lebar=18)  # Jangan ulangi dari awal
        else:  # Kalau dibuka dari menu
            self.tombol(isi, "Kembali", self.buka_menu, lebar=16)  # Kembali ke menu

    def mulai(self) -> None:  # Tombol Mulai ditekan
        self.reset()  # Reset skor, nyawa, acak soal
        self.sedang_latihan = True  # Tandai sedang latihan
        self.buka_soal()  # Tampilkan soal pertama

    def buka_soal(self) -> None:  # Tampilkan 1 soal, atau pindah ke hasil
        if self.nyawa <= 0:  # Nyawa habis
            self.buka_hasil(False)  # Kalah
            return  # Stop, jangan gambar soal
        if self.nomor >= len(self.soal_acak):  # Semua soal sudah dijawab
            self.buka_hasil(True)  # Menang / tuntas
            return  # Stop

        soal = self.soal_acak[self.nomor]  # Ambil soal sesuai nomor sekarang
        frame = self.bersihkan()  # Layar baru
        self.header(frame, f"{soal['jenis']}    ({self.nomor + 1}/5)")  # Contoh: Sandi Jam (1/5)

        isi = tk.Frame(frame, bg=HIJAU_TUA, padx=36, pady=16)  # Area soal
        isi.pack(fill="both", expand=True)  # Isi sisa ruang
        tk.Label(isi, textvariable=self.status, font=self.kecil_font, fg=ABU, bg=HIJAU_TUA).pack(  # Status benar/salah
            anchor="w"  # Rata kiri
        )  # Selesai label status
        tk.Label(  # Teks pertanyaan
            isi,  # Di area soal
            text=soal["tanya"],  # Ambil dari data soal
            font=self.sub_font,  # Huruf sedang
            fg=PUTIH,  # Warna terang
            bg=HIJAU_TUA,  # Latar
            justify="left",  # Jika banyak baris, rata kiri
        ).pack(anchor="w", pady=(12, 8))  # Jarak dari status
        tk.Label(  # Petunjuk di bawah soal
            isi,  # Area yang sama
            text=f"Petunjuk: {soal['hint']}",  # Gabung kata Petunjuk + hint
            font=self.kecil_font,  # Huruf kecil
            fg=KHAKI,  # Warna khaki
            bg=HIJAU_TUA,  # Latar
            justify="left",  # Rata kiri
        ).pack(anchor="w", pady=(0, 12))  # Jarak ke tombol opsi

        opsi = list(soal["opsi"])  # Salin pilihan supaya data asli tidak diacak permanen
        random.shuffle(opsi)  # Acak urutan A/B/C/D
        for teks in opsi:  # Buat satu tombol per pilihan
            self.tombol_opsi(isi, teks, lambda t=teks, s=soal: self.jawab(t, s))  # t=teks menyimpan nilai loop
        self.tombol(isi, "Lihat Keterangan", self.buka_keterangan, lebar=18)  # Buka penjelasan tanpa reset

    def jawab(self, pilihan: str, soal: dict) -> None:  # Dipanggil saat pemain klik opsi
        if pilihan == soal["jawab"]:  # Bandingkan dengan kunci
            self.skor += 10  # Tambah 10 poin
            self.status.set(f"Benar. {soal['jenis']} terbuka. +10")  # Pesan sukses
        else:  # Jawaban salah
            self.nyawa -= 1  # Kurangi nyawa
            self.status.set(f"Belum tepat. Jawaban: {soal['jawab']}")  # Tunjukkan kunci
            if self.nyawa <= 0:  # Kalau nyawa habis sekarang
                self.buka_hasil(False)  # Langsung kalah
                return  # Jangan lanjut ke soal berikutnya
        self.nomor += 1  # Maju ke soal berikutnya
        self.buka_soal()  # Gambar soal baru / hasil

    def buka_hasil(self, tuntas: bool) -> None:  # Layar akhir menang atau kalah
        self.sedang_latihan = False  # Latihan sudah selesai
        frame = self.bersihkan()  # Layar baru
        tengah = tk.Frame(frame, bg=HIJAU_TUA)  # Wadah tengah
        tengah.place(relx=0.5, rely=0.46, anchor="center")  # Posisi tengah
        judul = "SANDI TUNTAS" if tuntas else "BELUM TUNTAS"  # Judul tergantung hasil
        warna = KHAKI if tuntas else MERAH  # Khaki jika lulus, merah jika gagal
        tk.Label(tengah, text=judul, font=self.judul_font, fg=warna, bg=HIJAU_TUA).pack()  # Tampilkan judul
        tk.Label(  # Tampilkan skor
            tengah, text=f"Skor: {self.skor} / 50", font=self.sub_font, fg=EMAS, bg=HIJAU_TUA  # Maksimal 50
        ).pack(pady=8)  # Jarak 8 piksel
        if tuntas and self.skor == 50:  # 5 benar semua
            pesan = "Lencana Putra: semua sandi dikuasai."  # Pesan sempurna
        elif tuntas:  # Selesai tapi ada yang salah
            pesan = "Lulus. Ulangi yang masih salah supaya makin hafal."  # Pesan lulus
        else:  # Nyawa habis
            pesan = "Nyawa habis. Seorang Pramuka tabah — coba lagi."  # Pesan kalah
        tk.Label(tengah, text=pesan, font=self.teks_font, fg=KRIM, bg=HIJAU_TUA).pack(pady=(0, 18))  # Tampilkan pesan
        self.tombol(tengah, "Main Lagi", self.mulai, lebar=18)  # Ulang dari soal acak baru
        self.tombol(tengah, "Menu", self.buka_menu, lebar=18)  # Kembali ke menu


def main() -> None:  # Titik masuk program
    root = tk.Tk()  # Buat jendela kosong
    SandiPutra(root)  # Pasang aplikasi ke jendela itu
    root.mainloop()  # Tunggu klik pengguna sampai jendela ditutup


if __name__ == "__main__":  # True hanya jika file ini dijalankan langsung (bukan di-import)
    main()  # Mulai aplikasi

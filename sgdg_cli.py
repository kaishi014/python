"""Latihan Sandi Penggalang Putra versi CLI untuk terminal, termasuk di HP."""

from __future__ import annotations

import random


SOAL = [
    {
        "jenis": "Sandi Jam",
        "tanya": "Ubah sandi jam ini menjadi kata (tiap huruf berjarak 5 menit):\n"
        "08.25 - 07.20 - 07.30 - 08.40",
        "opsi": ["REGU", "RAWA", "TALI", "API"],
        "jawab": "REGU",
        "hint": "A=07.00, B=07.05, dan seterusnya tiap 5 menit. Contoh: R=08.25.",
    },
    {
        "jenis": "Sandi Nomor",
        "tanya": "Sandi nomor (A=1 sampai Z=26):\n11 - 15 - 13 - 16 - 1 - 19",
        "opsi": ["KOMPAS", "KAPAK", "KEMAH", "KALIAN"],
        "jawab": "KOMPAS",
        "hint": "11=K, 15=O, 13=M, 16=P, 1=A, 19=S.",
    },
    {
        "jenis": "Sandi AZ",
        "tanya": "Ubah sandi AZ ini menjadi kata:\nG Z O R",
        "opsi": ["TALI", "TENTU", "TARA", "KITA"],
        "jawab": "TALI",
        "hint": "A=Z, B=Y, dan seterusnya sampai M=N. TALI menjadi GZOR.",
    },
    {
        "jenis": "Sandi Morse",
        "tanya": "Ubah Morse ini menjadi kata:\n.--.   .-.   .-   --   ..-   -.-   .-",
        "opsi": ["PRAMUKA", "PENGALANG", "PERKEMAH", "PEMBINA"],
        "jawab": "PRAMUKA",
        "hint": "P=.--., R=.-., A=.-, M=--, U=..-, K=-.-.",
    },
    {
        "jenis": "Sandi AN",
        "tanya": "Ubah sandi AN ini menjadi kata:\nN C V",
        "opsi": ["API", "AIR", "TALI", "REGU"],
        "jawab": "API",
        "hint": "A=N, B=O, dan seterusnya; setelah Z kembali ke A.",
    },
]

KETERANGAN = [
    (
        "Sandi Jam",
        "A=07.00, B=07.05, dan setiap huruf berikutnya maju 5 menit.\n"
        "C=07.10  D=07.15  E=07.20  F=07.25  G=07.30  H=07.35\n"
        "I=07.40  J=07.45  K=07.50  L=07.55  M=08.00  N=08.05\n"
        "O=08.10  P=08.15  Q=08.20  R=08.25  S=08.30  T=08.35\n"
        "U=08.40  V=08.45  W=08.50  X=08.55  Y=09.00  Z=09.05",
    ),
    (
        "Sandi Nomor",
        "Huruf diganti nomor urut abjad. A=1 sampai Z=26.\n"
        "Contoh: 1-16-9 = API",
    ),
    (
        "Sandi AZ",
        "Pasangkan huruf dari ujung alfabet: A=Z, B=Y, C=X, dan seterusnya sampai M=N.\n"
        "N=M, O=L, P=K, Q=J, R=I, S=H, T=G, U=F, V=E, W=D, X=C, Y=B, Z=A.\n"
        "Contoh: TALI menjadi GZOR. Gunakan pasangan yang sama untuk membaca kembali.",
    ),
    (
        "Sandi Morse",
        "Titik (.) singkat, strip (-) panjang.\n"
        "A=.-  I=..  K=-.-  M=--  P=.--.  R=.-.  U=..-",
    ),
    (
        "Sandi AN",
        "Setiap huruf diganti huruf 13 langkah sesudahnya.\n"
        "A=N  B=O  C=P  D=Q  E=R  F=S  G=T  H=U  I=V  J=W  K=X  L=Y  M=Z\n"
        "N=A  O=B  P=C  Q=D  R=E  S=F  T=G  U=H  V=I  W=J  X=K  Y=L  Z=M\n"
        "Contoh: API menjadi NCV. Untuk membaca kembali, gunakan pasangan yang sama.",
    ),
]


def baca_pilihan(prompt: str, pilihan_validas: set[str]) -> str:
    while True:
        pilihan = input(prompt).strip()
        if pilihan in pilihan_validas:
            return pilihan
        print("Pilihan tidak tersedia. Coba lagi.")


def tampilkan_keterangan() -> None:
    print("\nKETERANGAN SANDI")
    print("=" * 40)
    for judul, isi in KETERANGAN:
        print(f"\n{judul}")
        print(isi)
    input("\nTekan Enter untuk kembali ke menu...")


def tampilkan_cara_main() -> None:
    print("\nCARA MAIN")
    print("=" * 40)
    print("Ada 5 soal dengan jenis sandi yang berbeda.")
    print("Pilih jawaban dengan mengetik nomor 1 sampai 4.")
    print("Nyawa tersedia 3. Jawaban salah mengurangi 1 nyawa.")
    print("Jawaban benar mendapat 10 poin. Skor maksimal 50.")
    print("Urutan soal dan pilihan jawaban diacak setiap permainan.")
    input("\nTekan Enter untuk kembali ke menu...")


def mainkan() -> None:
    skor = 0
    nyawa = 3
    soal_acak = list(SOAL)
    random.shuffle(soal_acak)

    print("\nLATIHAN DIMULAI")
    for nomor, soal in enumerate(soal_acak, start=1):
        if nyawa <= 0:
            break

        print("\n" + "-" * 40)
        print(f"Soal {nomor}/5 | {soal['jenis']}")
        print(f"Nyawa: {nyawa}/3 | Skor: {skor}")
        print(soal["tanya"])
        print(f"Petunjuk: {soal['hint']}")

        opsi_acak = list(soal["opsi"])
        random.shuffle(opsi_acak)
        for nomor_opsi, teks in enumerate(opsi_acak, start=1):
            print(f"  {nomor_opsi}. {teks}")

        pilihan = baca_pilihan("Jawaban [1-4]: ", {"1", "2", "3", "4"})
        jawaban = opsi_acak[int(pilihan) - 1]
        if jawaban == soal["jawab"]:
            skor += 10
            print("Benar! +10 poin.")
        else:
            nyawa -= 1
            print(f"Belum tepat. Jawaban yang benar: {soal['jawab']}.")
        print(f"Nyawa tersisa: {nyawa}/3 | Skor: {skor}")

    tuntas = nyawa > 0
    print("\n" + "=" * 40)
    print("HASIL AKHIR")
    print(f"Skor: {skor}/50")
    if tuntas and skor == 50:
        print("Lencana Putra: semua sandi dikuasai.")
    elif tuntas:
        print("Lulus. Ulangi yang masih salah supaya makin hafal.")
    else:
        print("Nyawa habis. Coba lagi.")
    input("\nTekan Enter untuk kembali ke menu...")


def main() -> None:
    while True:
        print("\nSANDI PENGGALANG PUTRA")
        print("1. Mulai latihan")
        print("2. Keterangan sandi")
        print("3. Cara main")
        print("4. Keluar")
        pilihan = baca_pilihan("Pilih menu [1-4]: ", {"1", "2", "3", "4"})

        if pilihan == "1":
            mainkan()
        elif pilihan == "2":
            tampilkan_keterangan()
        elif pilihan == "3":
            tampilkan_cara_main()
        else:
            print("Sampai jumpa!")
            return


if __name__ == "__main__":
    main()
import tkinter as tk

SOAL = [
    (
        "Jarak kota A ke kota B pada peta 5 cm. Skala 1 : 200.000. Berapa jarak sebenarnya (meter)?",
        ["5.000 m", "10.000 m", "15.000 m", "20.000 m"],
        "B",
    ),
    (
        "Jarak sebenarnya 4.500 meter dan skala 1 : 500.000. Berapa jarak pada peta?",
        ["0,45 cm", "0,9 cm", "4,5 cm", "9 cm"],
        "B",
    ),
    (
        "Jarak pada peta 8 cm mewakili 16.000 meter. Pilih penyebut skala yang benar.",
        ["200.000", "1.000.000", "2.000.000", "20.000.000"],
        "A",
    ),
    (
        "Jarak pada peta 6 cm dengan skala 1 : 300.000. Berapa jarak sebenarnya dalam meter?",
        None,
        "18000",
    ),
    (
        "Jarak sebenarnya 7.500 meter digambar sepanjang 15 cm. Berapa penyebut skalanya?",
        None,
        "50000",
    ),
]


def hitung_skala(mode, nilai_pertama, nilai_kedua):
    """Hitung jarak sebenarnya (JS), jarak peta (JP), atau skala (S)."""
    if nilai_pertama <= 0 or nilai_kedua <= 0:
        raise ValueError("Nilai harus lebih besar dari nol.")

    if mode == "JS":
        return nilai_pertama * nilai_kedua / 100
    if mode == "JP":
        return nilai_pertama * 100 / nilai_kedua
    if mode == "S":
        return nilai_kedua * 100 / nilai_pertama
    raise ValueError("Mode perhitungan tidak dikenal.")


def baca_angka(prompt):
    while True:
        teks = input(prompt).strip().replace(",", ".")
        try:
            nilai = float(teks)
            if nilai <= 0:
                print("Nilai harus lebih besar dari nol.")
                continue
            return nilai
        except ValueError:
            print("Masukkan angka yang valid, misalnya 12 atau 12.5.")


def tampilkan_kalkulator():
    print("\n--- Kalkulator Skala ---")
    print("1. Cari jarak sebenarnya (JS)")
    print("2. Cari jarak pada peta (JP)")
    print("3. Cari penyebut skala (S)")
    pilihan = input("Pilih perhitungan [1-3]: ").strip()

    if pilihan == "1":
        mode = "JS"
        label_pertama = "Jarak pada peta (cm)"
        label_kedua = "Penyebut skala (contoh 500000)"
    elif pilihan == "2":
        mode = "JP"
        label_pertama = "Jarak sebenarnya (meter)"
        label_kedua = "Penyebut skala (contoh 500000)"
    elif pilihan == "3":
        mode = "S"
        label_pertama = "Jarak pada peta (cm)"
        label_kedua = "Jarak sebenarnya (meter)"
    else:
        print("Pilihan tidak tersedia.")
        return

    pertama = baca_angka(f"{label_pertama}: ")
    kedua = baca_angka(f"{label_kedua}: ")
    hasil = hitung_skala(mode, pertama, kedua)

    if mode == "JS":
        print(f"Jarak sebenarnya = {hasil:,.2f} meter")
    elif mode == "JP":
        print(f"Jarak pada peta = {hasil:,.2f} cm")
    else:
        print(f"Skala peta = 1 : {hasil:,.0f}")


def cek_jawaban(soal, jawaban):
    if soal[1] is not None:
        return jawaban.strip().upper() == soal[2]
    try:
        nilai = float(jawaban.strip().replace(".", "").replace(",", "."))
        return nilai == float(soal[2])
    except ValueError:
        return False


def mulai_latihan():
    print("\n--- Latihan Soal ---")
    skor = 0
    for nomor, (pertanyaan, pilihan, _) in enumerate(SOAL, start=1):
        print(f"\n{nomor}. {pertanyaan}")
        if pilihan:
            for huruf, opsi in zip("ABCD", pilihan):
                print(f"   {huruf}. {opsi}")
            jawaban = input("Jawaban [A-D]: ")
        else:
            jawaban = input("Jawaban angka: ")

        if cek_jawaban(SOAL[nomor - 1], jawaban):
            print("Benar!")
            skor += 20
        else:
            print(f"Belum tepat. Jawaban: {SOAL[nomor - 1][2]}.")

    print(f"\nSkor kamu: {skor} dari 100")


def tampilkan_penjelasan():
    print("\n--- Penjelasan ---")
    print("Skala membandingkan jarak pada peta dengan jarak sebenarnya.")
    print("Contoh 1 : 200.000 berarti 1 cm pada peta mewakili 200.000 cm sebenarnya.")
    print("Jarak peta dimasukkan dalam cm; jarak sebenarnya dimasukkan dalam meter.")
    print("Rumus: JS (meter) = JP (cm) x penyebut skala / 100")
    print("       JP (cm) = JS (meter) x 100 / penyebut skala")
    print("       Penyebut skala = JS (meter) x 100 / JP (cm)")


def main():
    print("SKALA PETA | Belajar dan Menghitung")
    while True:
        print("\nMenu utama")
        print("1. Kalkulator")
        print("2. Latihan soal")
        print("3. Penjelasan")
        print("0. Keluar")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_kalkulator()
        elif pilihan == "2":
            mulai_latihan()
        elif pilihan == "3":
            tampilkan_penjelasan()
        elif pilihan == "0":
            print("Sampai jumpa!")
            break
        else:
            print("Pilihan tidak tersedia. Masukkan 0, 1, 2, atau 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")
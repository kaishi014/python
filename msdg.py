import tkinter as tk
from tkinter import messagebox, ttk


BG = "#f4f7f6"
SURFACE = "#ffffff"
INK = "#20313b"
MUTED = "#6b7c83"
TEAL = "#147d72"
TEAL_DARK = "#0d5f58"
MINT = "#e1f2ee"
LINE = "#dce7e4"
GOLD = "#d69b35"
ERROR = "#b84c4c"


class KalkulatorSkalaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skala Peta | Belajar dan Menghitung")
        self.root.geometry("760x650")
        self.root.minsize(700, 590)
        self.root.configure(bg=BG)

        self.content = None
        self.calc_mode = tk.StringVar(value="JS")
        self.quiz_vars = {}

        self.setup_style()
        self.show_home()

    def setup_style(self):
        self.title_font = ("Segoe UI", 25, "bold")
        self.heading_font = ("Segoe UI", 17, "bold")
        self.body_font = ("Segoe UI", 10)
        self.button_font = ("Segoe UI", 10, "bold")
        self.small_font = ("Segoe UI", 9)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TScrollbar", background=LINE, troughcolor=BG, bordercolor=BG, arrowcolor=MUTED)

    def clear_page(self):
        if self.content is not None:
            self.content.destroy()
        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(fill=tk.BOTH, expand=True)
        return self.content

    def header(self, parent, title, subtitle=""):
        bar = tk.Frame(parent, bg=SURFACE, padx=30, pady=18, highlightbackground=LINE, highlightthickness=1)
        bar.pack(fill=tk.X)

        left = tk.Frame(bar, bg=SURFACE)
        left.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Label(left, text=title, font=self.heading_font, fg=INK, bg=SURFACE).pack(anchor="w")
        if subtitle:
            tk.Label(left, text=subtitle, font=self.small_font, fg=MUTED, bg=SURFACE).pack(anchor="w", pady=(3, 0))

        tk.Button(
            bar, text="Beranda", command=self.show_home, font=self.button_font,
            bg=MINT, fg=TEAL_DARK, activebackground="#c9e9e1", relief="flat",
            padx=14, pady=7, cursor="hand2"
        ).pack(side=tk.RIGHT)

    def action_button(self, parent, text, command, primary=False, width=22):
        bg = TEAL if primary else SURFACE
        fg = "white" if primary else TEAL_DARK
        active = TEAL_DARK if primary else MINT
        return tk.Button(
            parent, text=text, command=command, font=self.button_font,
            bg=bg, fg=fg, activebackground=active, activeforeground=fg,
            relief="flat", bd=0, padx=12, pady=9, width=width, cursor="hand2"
        )

    def feature_card(self, parent, title, description, action_text, command, accent):
        card = tk.Frame(parent, bg=SURFACE, padx=18, pady=17, highlightbackground=LINE, highlightthickness=1)
        card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=6)
        tk.Frame(card, bg=accent, height=5).pack(fill=tk.X, pady=(0, 14))
        tk.Label(card, text=title, font=("Segoe UI", 12, "bold"), fg=INK, bg=SURFACE).pack(anchor="w")
        tk.Label(card, text=description, font=self.small_font, fg=MUTED, bg=SURFACE,
                 justify="left", wraplength=190, height=4).pack(anchor="w", pady=(7, 12))
        self.action_button(card, action_text, command, primary=accent == TEAL, width=17).pack(anchor="w")

    def show_home(self):
        page = self.clear_page()

        hero = tk.Frame(page, bg=INK, padx=42, pady=34)
        hero.pack(fill=tk.X)
        tk.Label(hero, text="SKALA PETA", font=self.title_font, fg="white", bg=INK).pack(anchor="w")
        tk.Label(hero, text="Hitung lebih mudah. Pahami lebih dalam.", font=("Segoe UI", 12),
                 fg="#b9d6d1", bg=INK).pack(anchor="w", pady=(6, 0))
        tk.Frame(hero, bg=GOLD, height=3, width=58).pack(anchor="w", pady=(20, 0))

        body = tk.Frame(page, bg=BG, padx=28, pady=25)
        body.pack(fill=tk.BOTH, expand=True)
        tk.Label(body, text="Mulai dari sini", font=self.heading_font, fg=INK, bg=BG).pack(anchor="w")
        tk.Label(body, text="Pilih aktivitas yang ingin kamu lakukan.", font=self.body_font,
                 fg=MUTED, bg=BG).pack(anchor="w", pady=(4, 17))

        cards = tk.Frame(body, bg=BG)
        cards.pack(fill=tk.X)
        self.feature_card(cards, "Kalkulator", "Cari jarak sebenarnya, jarak pada peta, atau penyebut skala.",
                          "Buka kalkulator", self.show_calculator, TEAL)
        self.feature_card(cards, "Latihan soal", "Uji pemahamanmu melalui lima soal tentang skala peta.",
                          "Mulai latihan", self.show_quiz, GOLD)
        self.feature_card(cards, "Penjelasan", "Pelajari rumus, satuan, dan cara menggunakan aplikasi ini.",
                          "Lihat penjelasan", self.show_about, "#6c8ebf")

        note = tk.Frame(body, bg=MINT, padx=16, pady=13)
        note.pack(fill=tk.X, pady=(25, 0))
        tk.Label(note, text="Rumus utama", font=("Segoe UI", 10, "bold"), fg=TEAL_DARK, bg=MINT).pack(anchor="w")
        tk.Label(note, text="JS = (JP x penyebut skala) / 100    |    1 cm pada peta = penyebut skala cm sebenarnya",
                 font=self.small_font, fg=TEAL_DARK, bg=MINT).pack(anchor="w", pady=(3, 0))

    def show_about(self):
        page = self.clear_page()
        self.header(page, "Penjelasan aplikasi", "Panduan singkat untuk belajar skala peta")

        body = tk.Frame(page, bg=BG, padx=34, pady=22)
        body.pack(fill=tk.BOTH, expand=True)
        self.info_section(body, "Apa itu skala peta?",
                          "Skala adalah perbandingan jarak pada peta dengan jarak sebenarnya. Contoh skala 1 : 200.000 berarti 1 cm pada peta mewakili 200.000 cm di dunia nyata.")
        self.info_section(body, "Tiga hal yang dapat dicari",
                          "Jarak sebenarnya (JS), jarak pada peta (JP), dan penyebut skala (S). Pilih salah satu mode di halaman Kalkulator, lalu masukkan dua nilai yang tersedia.")
        self.info_section(body, "Satuan yang digunakan",
                          "Jarak pada peta dimasukkan dalam cm, sedangkan jarak sebenarnya dimasukkan dalam meter. Aplikasi otomatis mengubah meter ke cm saat menghitung.")

        panel = tk.Frame(body, bg=SURFACE, padx=18, pady=15, highlightbackground=LINE, highlightthickness=1)
        panel.pack(fill=tk.X, pady=(8, 0))
        tk.Label(panel, text="Cara menggunakan", font=("Segoe UI", 11, "bold"), fg=INK, bg=SURFACE).pack(anchor="w")
        for number, text in enumerate(("Pilih menu Kalkulator atau Latihan soal.", "Isi data dengan angka yang benar.", "Periksa hasil atau skor yang muncul."), 1):
            tk.Label(panel, text=f"{number}.  {text}", font=self.body_font, fg=MUTED, bg=SURFACE).pack(anchor="w", pady=(7, 0))

    def info_section(self, parent, title, text):
        tk.Label(parent, text=title, font=("Segoe UI", 11, "bold"), fg=TEAL_DARK, bg=BG).pack(anchor="w", pady=(0, 4))
        tk.Label(parent, text=text, font=self.body_font, fg=MUTED, bg=BG,
                 wraplength=650, justify="left").pack(anchor="w", pady=(0, 17))

    def show_calculator(self):
        page = self.clear_page()
        self.header(page, "Kalkulator skala", "Masukkan dua nilai untuk mendapatkan hasil perhitungan")

        body = tk.Frame(page, bg=BG, padx=34, pady=20)
        body.pack(fill=tk.BOTH, expand=True)
        tk.Label(body, text="Pilih jenis perhitungan", font=("Segoe UI", 11, "bold"), fg=INK, bg=BG).pack(anchor="w")
        mode_frame = tk.Frame(body, bg=BG)
        mode_frame.pack(fill=tk.X, pady=(9, 20))
        self.mode_buttons = {}
        for text, value in (("Jarak sebenarnya", "JS"), ("Jarak pada peta", "JP"), ("Skala peta", "S")):
            button = tk.Radiobutton(
                mode_frame, text=text, variable=self.calc_mode, value=value,
                command=self.change_calc_mode, font=self.button_font, fg=TEAL_DARK,
                bg=SURFACE, activebackground=MINT, activeforeground=TEAL_DARK,
                selectcolor=TEAL, indicatoron=False, relief="flat", bd=0,
                padx=14, pady=10, cursor="hand2"
            )
            button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
            self.mode_buttons[value] = button

        form = tk.Frame(body, bg=SURFACE, padx=20, pady=17, highlightbackground=LINE, highlightthickness=1)
        form.pack(fill=tk.X)
        self.lbl1 = tk.Label(form, text="", font=self.body_font, fg=INK, bg=SURFACE)
        self.lbl1.pack(anchor="w")
        self.ent1 = tk.Entry(form, font=("Segoe UI", 11), relief="flat", bg="#f4f8f7", fg=INK,
                             highlightbackground=LINE, highlightthickness=1)
        self.ent1.pack(fill=tk.X, pady=(5, 13), ipady=6)
        self.lbl2 = tk.Label(form, text="", font=self.body_font, fg=INK, bg=SURFACE)
        self.lbl2.pack(anchor="w")
        self.ent2 = tk.Entry(form, font=("Segoe UI", 11), relief="flat", bg="#f4f8f7", fg=INK,
                             highlightbackground=LINE, highlightthickness=1)
        self.ent2.pack(fill=tk.X, pady=(5, 15), ipady=6)
        self.action_button(form, "Hitung sekarang", self.hitung_kalkulator, primary=True, width=20).pack(anchor="w")

        self.res_label = tk.Label(body, text="Hasil akan muncul di sini.", font=("Segoe UI", 11, "bold"),
                                  fg=TEAL_DARK, bg=MINT, padx=15, pady=14)
        self.res_label.pack(fill=tk.X, pady=(18, 0))
        self.reset_calc_inputs()
        self.update_calc_inputs()

    def change_calc_mode(self):
        self.reset_calc_inputs()
        self.update_calc_inputs()

    def reset_calc_inputs(self):
        if not hasattr(self, "ent1") or not hasattr(self, "ent2"):
            return
        self.ent1.delete(0, tk.END)
        self.ent2.delete(0, tk.END)
        self.res_label.config(text="Hasil akan muncul di sini.", fg=TEAL_DARK)

    def update_calc_inputs(self):
        if not hasattr(self, "lbl1"):
            return
        mode = self.calc_mode.get()
        if mode == "JS":
            self.lbl1.config(text="Jarak pada peta (JP) dalam cm")
            self.lbl2.config(text="Penyebut skala, contoh 500000")
        elif mode == "JP":
            self.lbl1.config(text="Jarak sebenarnya (JS) dalam meter")
            self.lbl2.config(text="Penyebut skala, contoh 500000")
        else:
            self.lbl1.config(text="Jarak pada peta (JP) dalam cm")
            self.lbl2.config(text="Jarak sebenarnya (JS) dalam meter")
        for value, button in self.mode_buttons.items():
            selected = value == mode
            button.config(bg=TEAL if selected else SURFACE, fg="white" if selected else TEAL_DARK)

    def hitung_kalkulator(self):
        try:
            val1 = float(self.ent1.get())
            val2 = float(self.ent2.get())
            if val1 < 0 or val2 <= 0:
                raise ValueError
            mode = self.calc_mode.get()
            if mode == "JS":
                hasil = val1 * val2 / 100
                text = f"Jarak sebenarnya = {hasil:,.2f} meter"
            elif mode == "JP":
                hasil = val1 * 100 / val2
                text = f"Jarak pada peta = {hasil:,.2f} cm"
            else:
                hasil = val2 * 100 / val1
                text = f"Skala peta = 1 : {hasil:,.0f}"
            self.res_label.config(text=text, fg=TEAL_DARK)
        except (ValueError, ZeroDivisionError):
            self.res_label.config(text="Masukkan angka yang valid dan lebih besar dari nol.", fg=ERROR)

    def show_quiz(self):
        page = self.clear_page()
        self.header(page, "Latihan soal", "Lima soal untuk menguji pemahamanmu")
        canvas = tk.Canvas(page, bg=BG, highlightthickness=0)
        scrollbar = ttk.Scrollbar(page, orient="vertical", command=canvas.yview)
        scrollable = tk.Frame(canvas, bg=BG, padx=30, pady=17)
        scrollable.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable, anchor="nw", width=665)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        soal_data = [
            (1, "Jarak kota A ke kota B pada peta adalah 5 cm. Jika skala peta 1 : 200.000, berapa meter jarak sebenarnya?", ["A. 5.000 m", "B. 10.000 m", "C. 15.000 m", "D. 20.000 m"], "B", "pg"),
            (2, "Jarak sebenarnya antara dua kota adalah 4.500 meter. Jika skala peta 1 : 500.000, jarak pada peta adalah...", ["A. 0,45 cm", "B. 0,9 cm", "C. 4,5 cm", "D. 9 cm"], "B", "pg"),
            (3, "Jarak pada peta 8 cm mewakili jarak sebenarnya 16.000 meter. Skala peta tersebut adalah...", ["A. 1 : 200.000", "B. 1 : 1.000.000", "C. 1 : 2.000.000", "D. 1 : 20.000.000"], "A", "pg"),
            (4, "Jarak kota X dan Y pada peta 6 cm dengan skala 1 : 300.000. Berapa meter jarak sebenarnya? (Masukkan angka saja)", [], "18000", "essay"),
            (5, "Jarak sebenarnya 7.500 meter digambar pada peta sepanjang 15 cm. Berapakah penyebut skala peta tersebut?", [], "50000", "essay"),
        ]
        self.quiz_vars = {}
        for number, question, options, answer, kind in soal_data:
            card = tk.Frame(scrollable, bg=SURFACE, padx=15, pady=13, highlightbackground=LINE, highlightthickness=1)
            card.pack(fill=tk.X, pady=6)
            tk.Label(card, text=f"{number}. {question}", font=("Segoe UI", 10, "bold"), fg=INK,
                     bg=SURFACE, wraplength=610, justify="left").pack(anchor="w")
            var = tk.StringVar()
            self.quiz_vars[number] = (var, answer)
            if kind == "pg":
                for option in options:
                    tk.Radiobutton(card, text=option, variable=var, value=option[0], font=self.small_font,
                                   fg=MUTED, bg=SURFACE, activebackground=SURFACE, selectcolor=MINT).pack(anchor="w", padx=12, pady=2)
            else:
                tk.Entry(card, textvariable=var, font=("Segoe UI", 10), width=20, relief="flat",
                         bg="#f4f8f7", highlightbackground=LINE, highlightthickness=1).pack(anchor="w", padx=12, pady=(9, 2), ipady=4)
        self.action_button(scrollable, "Selesai dan cek jawaban", self.cek_jawaban, primary=True, width=25).pack(pady=17)

    def cek_jawaban(self):
        score = sum(20 for var, answer in self.quiz_vars.values() if var.get().strip().upper() == answer.upper())
        messagebox.showinfo("Hasil latihan", f"Skor kamu: {score} dari 100\n\nTerus berlatih untuk menguasai skala peta.")


if __name__ == "__main__":
    root = tk.Tk()
    KalkulatorSkalaApp(root)
    root.mainloop()
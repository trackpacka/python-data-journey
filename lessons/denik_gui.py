import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

HESLO = "Nssjmv1ps1"

def uloz_zapis():
    text = textove_pole.get("1.0", tk.END).strip()
    if text:
        cas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("denik.txt", "a", encoding="utf-8") as soubor:
            soubor.write(f"[{cas}]\n{text}\n\n")
        textove_pole.delete("1.0", tk.END)
        status_label.config(text="✅ Zápis byl uložen.")
    else:
        status_label.config(text="⚠️ Zápis je prázdný!")

def zobraz_zapisy():
    try:
        with open("denik.txt", "r", encoding="utf-8") as soubor:
            obsah = soubor.read()
    except FileNotFoundError:
        obsah = "Zatím nemáš žádné zápisy."

    nove_okno = tk.Toplevel(okno)
    nove_okno.title("Zápisy v deníku")
    nove_okno.configure(bg="#1e1e1e")
    nove_okno.geometry("600x400")

    text_widget = tk.Text(nove_okno, wrap=tk.WORD, bg="#2d2d2d", fg="#ffffff", insertbackground="white")
    text_widget.insert(tk.END, obsah)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def hledat_zapis():
    hledany_text = simpledialog.askstring("Hledat", "Zadej hledaný text:")
    if not hledany_text:
        return

    try:
        with open("denik.txt", "r", encoding="utf-8") as soubor:
            vsechny_zapisy = soubor.readlines()
    except FileNotFoundError:
        messagebox.showinfo("Výsledek", "Zatím nemáš žádné zápisy.")
        return

    vysledky = [radek for radek in vsechny_zapisy if hledany_text.lower() in radek.lower()]

    nove_okno = tk.Toplevel(okno)
    nove_okno.title("Výsledky hledání")
    nove_okno.configure(bg="#1e1e1e")
    nove_okno.geometry("600x300")

    text_widget = tk.Text(nove_okno, wrap=tk.WORD, bg="#2d2d2d", fg="#ffffff", insertbackground="white")
    if vysledky:
        text_widget.insert(tk.END, "".join(vysledky))
    else:
        text_widget.insert(tk.END, "Nenalezeny žádné odpovídající zápisy.")
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def smazat_zapisy():
    potvrzeni = messagebox.askyesno("Potvrzení", "Opravdu chceš smazat všechny zápisy?")
    if potvrzeni:
        open("denik.txt", "w", encoding="utf-8").close()
        status_label.config(text="🗑️ Všechny zápisy byly smazány.")

def prihlaseni():
    zadane_heslo = simpledialog.askstring("Přihlášení", "Zadej heslo:", show="*")
    if zadane_heslo == HESLO:
        spustit_aplikaci()
    else:
        messagebox.showerror("Chyba", "Nesprávné heslo. Aplikace bude ukončena.")
        okno.destroy()

def spustit_aplikaci():
    global textove_pole, status_label

    styl = ttk.Style()
    styl.theme_use("clam")
    styl.configure("TButton", background="#3c3f41", foreground="white", font=("Segoe UI", 10), padding=6)
    styl.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 12))
    styl.configure("TFrame", background="#1e1e1e")

    hlavni_frame = ttk.Frame(okno)
    hlavni_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    nadpis = ttk.Label(hlavni_frame, text="📝 Můj deník", font=("Segoe UI", 18, "bold"))
    nadpis.pack(pady=(0, 10))

    textove_pole = tk.Text(hlavni_frame, height=10, width=60, bg="#2d2d2d", fg="white", insertbackground="white", font=("Consolas", 11))
    textove_pole.pack(pady=10)

    tlacitka_frame = ttk.Frame(hlavni_frame)
    tlacitka_frame.pack(pady=5)

    ttk.Button(tlacitka_frame, text="💾 Uložit zápis", command=uloz_zapis).grid(row=0, column=0, padx=5)
    ttk.Button(tlacitka_frame, text="📖 Zobrazit zápisy", command=zobraz_zapisy).grid(row=0, column=1, padx=5)
    ttk.Button(tlacitka_frame, text="🔍 Hledat", command=hledat_zapis).grid(row=0, column=2, padx=5)
    ttk.Button(tlacitka_frame, text="🗑️ Smazat vše", command=smazat_zapisy).grid(row=0, column=3, padx=5)

    status_label = ttk.Label(hlavni_frame, text="", font=("Segoe UI", 10, "italic"))
    status_label.pack(pady=10)

# Spuštění
okno = tk.Tk()
okno.title("Přihlášení do deníku")
okno.configure(bg="#1e1e1e")
okno.geometry("500x200")

prihlaseni()
okno.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox


def choose_image_file() -> str | None:
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    path = filedialog.askopenfilename(
        title="Choose an image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.webp"),
            ("All files",   "*.*"),
        ]
    )

    root.destroy()
    return path or None


def show_info(title: str, message: str) -> None:
    _transient_root(lambda r: messagebox.showinfo(title, message))


def show_error(title: str, message: str) -> None:
    _transient_root(lambda r: messagebox.showerror(title, message))


def _transient_root(callback):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    callback(root)
    root.destroy()
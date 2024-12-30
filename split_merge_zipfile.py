import os
from tkinter import Tk, Button, Label, filedialog, messagebox
from tkinter import ttk

def split_zip_file(file_path, part_size_mb, output_dir):
    """Разбивает ZIP-файл на части и сохраняет их в указанной директории."""
    part_size = part_size_mb * 1024 * 1024  # Размер части в байтах
    base_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        part_num = 0
        while chunk := f.read(part_size):
            part_filename = os.path.join(output_dir, f"{base_name}.part{part_num}")
            with open(part_filename, 'wb') as part_file:
                part_file.write(chunk)
            part_num += 1
    messagebox.showinfo("Разделение завершено", f"Файл разделен на {part_num} частей и сохранен в {output_dir}.")

def merge_zip_file(part_files, output_file):
    """Объединяет части ZIP-файла обратно в исходный файл."""
    with open(output_file, 'wb') as merged_file:
        for part_file in part_files:
            with open(part_file, 'rb') as f:
                merged_file.write(f.read())
    messagebox.showinfo("Соединение завершено", f"Файл восстановлен: {output_file}")

def select_file_to_split():
    file_path = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")])
    if file_path:
        output_dir = filedialog.askdirectory(title="Выберите папку для сохранения частей")
        if output_dir:
            split_zip_file(file_path, part_size_mb=5, output_dir=output_dir)  # Указываем размер части (например, 5 МБ)

def select_files_to_merge():
    part_files = filedialog.askopenfilenames(filetypes=[("Part files", "*.part*")])
    if part_files:
        output_file = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
        if output_file:
            merge_zip_file(part_files, output_file)

from tkinter import Tk, ttk

def create_gui():
    root = Tk()
    root.title("Разделение и соединение ZIP-файлов")
    root.configure(bg="#011026")

    # Вычисление размеров экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Вычисление размеров окна (четверть экрана)
    window_width = screen_width // 3
    window_height = screen_height // 3

    # Вычисление позиции окна (центр экрана)
    x_position = screen_width // 5
    y_position = screen_height // 5

    # Установка размеров и позиции окна
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Настройка стилей
    style = ttk.Style()
    style.theme_use("clam")

    # Настройка цветов
    style.configure("TLabel", background="#011026", foreground="#ffffff", font=("Bookman", 25))
    style.configure("TButton", background="#011026", foreground="#ffffff", font=("Bookman", 15), padding=15)
    style.map("TButton", 
               background=[("active", "#041e47")],
               foreground=[("active", "#ffffff")])

    # Создание виджетов
    label = ttk.Label(root, text="Выберите действие:")
    label.pack(pady=20)
  
    split_button = ttk.Button(root, text="Разделить ZIP-файл", command=select_file_to_split)
    split_button.pack(pady=5)

    merge_button = ttk.Button(root, text="Соединить части ZIP-файла", command=select_files_to_merge)
    merge_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()


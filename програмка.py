import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")
        
        self.dir_path = tk.StringVar()
        
        tk.Label(root, text="Выберите каталог:").pack(pady=5)
        tk.Entry(root, textvariable=self.dir_path, width=50).pack(pady=5)
        tk.Button(root, text="Обзор", command=self.browse_directory).pack(pady=5)
        tk.Button(root, text="Переименовать файлы", command=self.rename_files).pack(pady=10)

        self.filter_var = tk.StringVar()
        tk.Label(root, text="Фильтр по расширению (например, .txt):").pack(pady=5)
        tk.Entry(root, textvariable=self.filter_var, width=20).pack(pady=5)
        
        self.sort_option = tk.StringVar(value='name')
        tk.Label(root, text="Сортировка по:").pack(pady=5)
        tk.Radiobutton(root, text="Имени", variable=self.sort_option, value='name').pack()
        tk.Radiobutton(root, text="Дате", variable=self.sort_option, value='date').pack()
        

    def browse_directory(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.dir_path.set(folder_selected)

    def rename_files(self):
        directory = self.dir_path.get()
        filter_ext = self.filter_var.get()
        pattern = simpledialog.askstring("Паттерн", "Введите паттерн для переименования (например, 'file_{}'):").strip()
        
        if not directory or not pattern:
            messagebox.showerror("Ошибка", "Выберите каталог и введите паттерн!")
            return
        
        try:
            files = self.get_files(directory, filter_ext)
            if self.sort_option.get() == 'name':
                files.sort()  # Сортировка по имени
            else:
                files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))  # Сортировка по дате

            for index, file in enumerate(files):
                old_path = os.path.join(directory, file)
                new_file_name = pattern.format(index + 1) + os.path.splitext(file)[1]  # Оставляем расширение
                new_path = os.path.join(directory, new_file_name)
                os.rename(old_path, new_path)

            messagebox.showinfo("Успех", f"{len(files)} файлов переименовано.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    def get_files(self, directory, filter_ext):
        """ Получение файлов с учетом фильтра. """
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filter_ext and not filename.endswith(filter_ext):
                    continue
                files.append(filename)
        return files

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()

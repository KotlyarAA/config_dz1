import os
import sys
import zipfile
import shutil
from pathlib import Path

class ShellEmulator:
    def __init__(self, computer_name, zip_path):
        self.computer_name = computer_name
        self.zip_path = zip_path
        self.current_dir = '/'
        self.file_system_root = Path('vfs')  # Виртуальная файловая систе

        try:
            self.myzip = zipfile.ZipFile(self.zip_path, 'r')  # Открываем ZIP файл
        except FileNotFoundError:
            print(f"Error: ZIP file {self.zip_path} not found")
            exit(1)

        #Распаковываем архив
        self._unzip_file_system()

    def _unzip_file_system(self):
        if self.file_system_root.exists():
            shutil.rmtree(self.file_system_root)  # Удаляем старую папку vfs
        with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.file_system_root)  # Распаковываем содержимое в папку vfs

    def _get_prompt(self):
        username = os.getenv('USER') or 'user'  # Получаем имя пользователя или используем 'user' по умолчанию
        return f"{username}@{self.computer_name}:{self.current_dir}$ "

    def run(self):
        while True:
            try:
                command = input(f"{self.computer_name}:{self.current_dir}$ ").strip()
                if command:
                    self.execute_command(command)
            except (EOFError, KeyboardInterrupt):
                print("\nExiting shell emulator.")
                break

    def execute_command(self, command):
        parts = command.split()
        cmd = parts[0]

        if cmd == "ls":
            self.ls()
        elif cmd == "cd":
            if len(parts) > 1:
                self.cd(parts[1])
            else:
                print("cd: missing argument")
        elif cmd == "exit":
            print("Exiting shell emulator.")
            sys.exit(0)
        elif cmd == "tac":
            if len(parts) > 1:
                self.tac(parts[1])
            else:
                print("tac: missing argument")
        elif cmd == "who":
            self.who()
        else:
            print(f"{cmd}: command not found")

    def ls(self):
        path = self.file_system_root / self.current_dir.lstrip('/')
        if path.is_dir():
            result = [item.name for item in path.iterdir()]
            for item in result:
                print(item)
            return result
        else:
            print(f"ls: cannot access '{self.current_dir}': No such directory")
            return []


    def cd(self, new_dir):
        """Смена директории."""
        
        # Переход на уровень выше
        if new_dir == "..":
            # Возвращаем родительский каталог
            self.current_dir = os.path.dirname(self.current_dir.rstrip('/'))
            return self.current_dir

        # Строим путь к новой директории
        potential_dir = os.path.join(self.current_dir, new_dir).lstrip('/')

        # Проверяем, что новая директория существует в ZIP-архиве
        if any(name.startswith(potential_dir + '/') for name in self.myzip.namelist() if name.endswith('/')):
            # Если директория существует, нормализуем путь
            self.current_dir = os.path.normpath('/' + potential_dir)
            return self.current_dir
        else:
            # Если директория не существует, выводим сообщение об ошибке
            print(f"cd: {new_dir}: No such directory")
            return self.current_dir

    def tac(self, file_path):
        file = self.file_system_root / self.current_dir.lstrip('/') / file_path
        if file.exists() and file.is_file():
            with open(file, 'r') as f:
                lines = f.readlines()
                result = ''.join(reversed(lines)).strip()  # Читаем строки и реверсируем их
                print(result)  # Печатаем результат
                return result
        else:
            print(f"tac: {file_path}: No such file")
            return None

    def who(self):
        username = os.getenv('USER') or 'user'  # Получаем имя пользователя или используем 'user' по умолчанию
        result = f"User: {username} (simulated)"
        print(result)
        return result

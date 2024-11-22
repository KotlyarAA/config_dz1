import os  # Добавьте этот импорт для работы с файловой системой
import sys
from shell_emulator import ShellEmulator

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_shell_emulator.py <computer_name> <zip_path>")
        sys.exit(1)

    computer_name = sys.argv[1]
    zip_path = sys.argv[2]

    # Проверяем существование zip-файла
    if not os.path.exists(zip_path):
        print(f"Error: {zip_path} does not exist.")
        sys.exit(1)

    emulator = ShellEmulator(computer_name, zip_path)
    emulator.run()

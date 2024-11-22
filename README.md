**1. Общее описание**

Этот скрипт представляет собой эмулятор командной оболочки на Python. Виртуальная файловая система (VFS) создается на основе содержимого ZIP-архива, который распаковывается в локальную директорию. Эмулятор позволяет пользователю выполнять команды, такие как ls, cd, tac, who и exit, для взаимодействия с виртуальной файловой системой. Этот инструмент имитирует базовые функции командной строки, используя Python для обработки файлов и директорий.

**2. Описание всех функций и настроек**

**Класс ShellEmulator**

Основной класс программы, отвечающий за эмуляцию оболочки и управление виртуальной файловой системой.

**Инициализация**

__init__(self, computer_name, zip_path)

- computer_name — имя компьютера, отображаемое в приглашении командной строки.
  
- zip_path — путь к ZIP-архиву с файлами и папками. Распаковывает содержимое ZIP-архива в директорию vfs. Создает структуру, которая имитирует файловую систему.

**Методы**

- _unzip_file_system(self)

Удаляет старую папку vfs, если она существует. Распаковывает содержимое ZIP-файла в директорию vfs, создавая виртуальную файловую систему.
- _get_prompt(self)

Возвращает строку приглашения командной строки, включающую имя пользователя и текущую директорию.

- run(self)

Основной цикл программы. Ожидает ввода команды от пользователя, вызывает соответствующие методы и обрабатывает завершение работы через exit, EOF или прерывание.
- execute_command(self, command)

Разбирает введенную команду и вызывает соответствующую функцию:

ls — список содержимого текущего каталога.

cd — смена текущего каталога.

tac — вывод содержимого файла в обратном порядке строк.

who — информация о текущем пользователе.

exit — завершение работы.

 -ls(self)

Выводит содержимое текущего каталога. Если каталог не существует, выводит сообщение об ошибке.
- cd(self, new_dir)

Меняет текущий рабочий каталог:
Переход на уровень выше при вводе ...
Проверяет существование каталога в VFS.
Обновляет текущий путь или выводит сообщение об ошибке.
- tac(self, file_path)

Читает файл и выводит его содержимое в обратном порядке строк. Если файл не найден, сообщает об ошибке.
- who(self)

Выводит имя текущего пользователя или "user", если имя недоступно.

**3. Описание команд для сборки проекта**

**Предварительные требования**

Python версии 3.6 или выше.
Установленные модули: os, sys, zipfile, shutil, pathlib.

**Запуск проекта**

Создайте ZIP-архив для VFS

Запустите программу


_python run_shell_emulator.py <computer_name> <zip_path>_

- <computer_name>: любое имя для отображения в приглашении командной строки.
- <zip_path>: путь к ZIP-архиву с VFS.


**4. Пример использования**
![image](https://github.com/user-attachments/assets/37c448bb-8b9a-4be2-b429-77ff18b24ef1)

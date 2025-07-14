import sys
from pathlib import Path
from colorama import init, Fore


init()

if len(sys.argv) < 2:
    print("Помилка: вкажіть шлях до директорії як аргумент.")
    sys.exit(1)

directory_path = Path(sys.argv[1])


if not directory_path.exists():
    print("Помилка: шлях не існує.")
    sys.exit(1)

if not directory_path.is_dir():
    print("Помилка:шлях не є дерикторією.")
    sys.exit(1)


def print_structure(path:Path, indent:str = ""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}[{item.name}]")
            print_structure(item, indent +"    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")


print_structure(directory_path)


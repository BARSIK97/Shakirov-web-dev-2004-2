import os
import sys

def search_file_recursive(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            with open(os.path.join(root, filename), 'r') as file:
                for _ in range(5):
                    line = file.readline()
                    if not line:
                        break
                    print(line, end='')

            return

    print(f"Файл {filename} не найден")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python file_search.py C:\test_sort")
    else:
        search_file_recursive(os.path.dirname(__file__), sys.argv[1])
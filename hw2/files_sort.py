import os

def sort_file(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()
    
    extension_mapping = {}
    for file in files:
        filename, ext = os.path.splitext(file)
        if ext in extension_mapping:
            extension_mapping[ext].append(filename)
        else:
            extension_mapping[ext] = [filename]
    
    for ext, filenames in extension_mapping.items():
        print('\n'.join([f + ext for f in filenames]))

directory_path = input("Введите путь до директории: ")
if os.path.isdir(directory_path):
    sort_file(directory_path)
else:
    print("Неверный путь до директории")
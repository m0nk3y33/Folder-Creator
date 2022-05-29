import os, re
import shutil

pattern = "_(.*?)_"

with os.scandir('D:\ZDJĘCIA - NOWE') as entries:
    for entry in entries:

        substring = re.search(pattern, entry.name).group(1)

        print(substring)
        print(entry.name)

        original = r'D:\ZDJĘCIA - NOWE/' + entry.name

        target = r'F:\Gotowe/' + substring + "/" + entry.name

        if not os.path.exists(substring):
            os.makedirs(r"F:\Gotowe/" + substring, exist_ok=True)
            shutil.copyfile(original, target)

# KOPIOWANIE PLIKÓW I WSADZANIE DO FOLDERÓW TWORZĄC NAZWY Z PLIKU

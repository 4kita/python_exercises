import pathlib

file_path = pathlib.Path.home() / 'my_folder' / "my_file.txt"

print(pathlib.Path.exists(file_path))

print(file_path.name)

print(file_path.parent)
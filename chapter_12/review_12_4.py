from pathlib import Path
import shutil

mf_path = Path.home() / "my_folder"

# print(mf_path.exists())

Paths = [
    mf_path / "file1.txt",
    mf_path / "file2.txt",
    mf_path / "image1.png"
]

for path in Paths:
    path.parent.mkdir(exist_ok=True)
    path.touch()

# for path in Paths:
#     print(path.exists())

# im_path = mf_path / "images"
# im_path.mkdir(exist_ok=True)

source = mf_path / "image1.png"
destination = mf_path / "images" / "image1.png"
(mf_path / "images").mkdir(exist_ok=True)
source.replace(destination)


shutil.rmtree(mf_path)
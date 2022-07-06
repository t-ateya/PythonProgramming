from pathlib import Path
from zipfile import ZipFile
from time import ctime
import shutil

#source = Path("ecommerce/__init__.py")
#target = Path() / "__init__.py"

# target.write_text(source.read_text())
#shutil.copy(source, target)

"""
with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)
"""

with ZipFile("files.zip") as zip:
    print(zip.namelist())

from pathlib import Path

import promptlib


def select_folder_promptlib(prompt):
    print(prompt)
    pl = promptlib.Files()
    folder_path = pl.dir()
    return folder_path

with open("config.cfg", "r") as file:
    resource_path = file.readline()

if resource_path == "": #converting string to PATH object
        resource_path = Path(__file__).parent
else:
    resource_path = Path(resource_path).expanduser().resolve()

tfpath = resource_path / "tfpath.TFL"
disabledmodspath = resource_path / "disabledModsPath.TFL"

if resource_path == "":
    print("The resource path is empty, please input path now.")
    resource_path = select_folder_promptlib("Where do you want me to install to, leave blank and it will setup here in this root folder. ")

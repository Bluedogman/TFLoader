import os
import sys
from pathlib import Path

import promptlib  # I love you


def select_folder_promptlib(prompt):
    print(prompt)
    pl = promptlib.Files()
    folder_path = pl.dir()
    return folder_path


def save_resource_paths(): #saving the path to the tf2 game folder in a file so it can be used in the main file
    resource_path = select_folder_promptlib("Where do you want me to install to, leave blank and it will setup here in this root folder. ")

    if resource_path == "":
        resource_path = Path(__file__).parent
    else:
        resource_path = Path(resource_path).expanduser().resolve()
    
    if not resource_path.is_absolute():
        print("youre dumb")
        return

    resource_path = resource_path / "resources"
    print(resource_path)
    tfpath = resource_path / "tfpath.TFL"
    disabledmodspath = resource_path / "disabledModsPath.TFL"
    resource_path_file = resource_path / "resourcePath.TFL"
    resource_path.mkdir(exist_ok=True)

    if not disabledmodspath.exists():
        print("Why isnt that file there...")
        with open(disabledmodspath, "w") as f:
            f.write("")

    tf2_path = input("What is the path to tf2? ")
    with open(tfpath, "w") as f:
        f.write(tf2_path)

def main(): #Gui logic, running it, calling other stuff, just idk man
    save_resource_paths()

main()
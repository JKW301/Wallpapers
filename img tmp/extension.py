import os
import shutil

folder_current = os.getcwd()
folder_src = os.path.expandvars("%localappdata%\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets")


def effacer_png(folder):
    for file in os.listdir(folder):
        path_to_file = os.path.join(folder, file)
        if os.path.isfile(path_to_file) and file.endswith('.png'):
            os.remove(path_to_file)
            print(f"File {file} has been deleted.")

def copy_paste_add_extension(source, destination):
    for file in os.listdir(source):
        path_to_file_source = os.path.join(source, file)
        if os.path.isfile(path_to_file_source) and not file.endswith('.png'):
            shutil.copy(path_to_file_source, os.path.join(destination, file + ".png"))
            print(f"File {file} copied with png extension.")


effacer_png(folder_current)

copy_paste_add_extension(folder_src, folder_current)
def display_ascii():
    logo = """

   ▄▄ ▄███▄
▄▀▀▀▀ ▄▄▄ ▀▀▀▀▄
█▒▒▒▒█░░░█▒▒▒▒█
█▒▒▒▒▀▄▄▄▀▒▒▒▒█
▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀
    """
    print(logo)

display_ascii()


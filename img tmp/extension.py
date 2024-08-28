import os
import shutil

#  The script should execute in the destination directory of the converted images to .png.
#  The script will delete all the .png files in the destination directory.

# folder_courant est le folder de destination
folder_current = os.getcwd()

# The folder_src is the folder where the images are stored. It is the folder where the images are stored before being converted to .png.
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
    tete_de_mort = """

   ▄▄ ▄███▄
▄▀▀▀▀ ▄▄▄ ▀▀▀▀▄
█▒▒▒▒█░░░█▒▒▒▒█
█▒▒▒▒▀▄▄▄▀▒▒▒▒█
▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀
    """
    print(tete_de_mort)

display_ascii()


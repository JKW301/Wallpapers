import os
from PIL import Image

directory = '../'

for filename in os.listdir(directory):
    if filename.endswith('.img'):
        img_path = os.path.join(directory, filename)
        
        with Image.open(img_path) as img:
            png_path = os.path.splitext(img_path)[0] + '.png'
            
            img.save(png_path)
            print(f'Converti : {filename} en {os.path.basename(png_path)}')

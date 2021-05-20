import sys
import os
from PIL import Image

#gran first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#chack is new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filname in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filname}')
    clean_name = os.path.splitext(filname)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')
#print(image_folder, output_folder)


#loop through pokedex
#convert images to png
#save to the new folder
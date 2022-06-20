from dino_ds_api import dino_ds_api as new_image
from GAN_core import GAN_core as who_is

img = new_image('dino_random') # выгрузка случайной фотографии с динозавром
species = who_is(img) # определение вида динозавра по фотографии

if species == 'T-rex':
    print('Selectel')
else:
    print(species)

print(dino_weight(img)) #

